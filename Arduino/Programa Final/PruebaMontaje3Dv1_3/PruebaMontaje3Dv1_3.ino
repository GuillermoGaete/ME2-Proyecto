//#define WITH_LCD
#define WITH_MOTOR

#ifdef WITH_LCD
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);
#endif

#ifdef WITH_MOTOR
#include <AFMotor.h>
#define PASOS_POR_VUELTA 256
#define PASOS_POR_MOVIMIENTO PASOS_POR_VUELTA/20
/*
  El primer parametro son la cantidad de pasos por vuelta 256
*/
AF_Stepper motor(PASOS_POR_VUELTA, 2);
#endif

#define HIGH_RES 8
#define LOW_RES 64
#define TURN_ARROUND 128

enum serialStates {
  RESET = 0,
  READING
};

enum moveStates {
  READY = 0,
  MOVING,
  FINISH
};

enum moveOrders {
  NOT = 0,
  RIGHT,
  LEFT,
  TURN,
  TO_ZERO
};

serialStates serialState = RESET;
moveStates moveState = READY;
int pasosPorMovimiento = LOW_RES;

void setup()
{
#ifdef WITH_LCD
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.print("Inicializando..");
  delay(1000);
#endif


#ifdef WITH_MOTOR
  motor.setSpeed(100);
  //Cantidad de pasos, Direccion y Modo
  while ( !digitalRead(A0) )
  {
    motor.step(5, FORWARD, SINGLE);
  }
#endif

  Serial.begin(9600);
}

void loop()
{
  moveOrders order = serialStateMachine();
  moveStateMachine(order);
}


moveOrders serialStateMachine() {
  moveOrders order = NOT;
  switch (serialState) {
    case RESET: {
        Serial.println("reset");
        serialState = READING;

#ifdef WITH_LCD
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Reading:");
        lcd.setCursor(0, 1);
#endif

      } break;
    case READING: {
        if (Serial.available() > 0) {
          // read all the available characters
          char message = Serial.read();
          if (message == 'r') {
            order = RIGHT;
            Serial.println("ack r");
          } else if (message == 'l') {
            order = LEFT;
            Serial.println("ack l");
          } else if (message == 'z') {
            order = TO_ZERO;
            Serial.println("ack z");
          } else if (message == 't') {
            order = TURN;
            Serial.println("ack b");
          } else if (message == 'h') {
            pasosPorMovimiento = HIGH_RES;
            order = NOT;
            Serial.println("ack h");
          } else if (message == 'p') {
            pasosPorMovimiento = LOW_RES;
            order = NOT;
            Serial.println("ack p");
          } else {
            Serial.println("Unknow");
          }

#ifdef WITH_LCD
          lcd.write(message);
#endif
        }
      } break;
    default:
      // statements
      break;
  }
  return order;
}

void moveStateMachine(moveOrders order) {
  static int steps;
  switch (moveState) {
    case READY: {
        if (order != NOT) {
          String sDir = "to right";
          if (order == TO_ZERO) {
            sDir = "to zero";
            while ( !digitalRead(A0) )
            {
              motor.step(5, FORWARD, SINGLE);
            }
            moveState = MOVING;
          } else if (order == LEFT) {
            sDir = "to left";
            moveState = MOVING;
            motor.step(pasosPorMovimiento, FORWARD, SINGLE);
            delay(1000);
          } else if (order == RIGHT) {
            sDir = "to righ";
            moveState = MOVING;
            motor.step(pasosPorMovimiento, BACKWARD, SINGLE);
            delay(1000);
          } else if (order == TURN) {
            sDir = "turn";
            moveState = MOVING;
            motor.step(TURN_ARROUND, FORWARD, SINGLE);
            delay(1000);
          }
#ifdef WITH_LCD
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("Moving:" + sDir);
#endif
        }
      } break;
    case MOVING: {
        moveState = FINISH;
      } break;
    case FINISH: {
        Serial.println("finish");
#ifdef WITH_LCD
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Reading:");
#endif
        moveState = READY;
      } break;
    default:
      // statements
      break;
  }
}
