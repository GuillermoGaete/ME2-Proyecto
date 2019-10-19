/*Modos de exitacion para el motor paso a paso
  SINGLE, DOUBLE, INTERLEAVE, MICROSTEP*/

//#include <AFMotor.h> // Libreria para manejo del Driver
#include <LiquidCrystal_I2C.h>


#define DERECHA   4
#define IZQUIERDA 8
#define RESET     12

#define MODO        SINGLE
#define ADELANTE    FORWARD
#define ATRAS       BACKWARD
#define PASOS       25
#define RETARDO     1000

//AF_Stepper motor(256, 2); // Creamos el objeto motor con 256 pasos Puerto 2
LiquidCrystal_I2C lcd(0x27, 16, 2);

int led = 13;
int input;

void setup()
{  
    Serial.begin(9600);    //Inicio de comunicacion Serie  
    lcd.init();
    
    pinMode(led, OUTPUT); 
    digitalWrite(led, LOW);
    
    pinMode(A0,INPUT);     //Configuracion de GPIOs
    
    //motor.setSpeed(100);   //Defino la velocidad del motor en RPM

    lcd.backlight();
    lcd.home();

    lcd.clear();
    lcd.print("Conectando PC..");
    
    while( Serial.available() == 0 )
    {
      digitalWrite(led, !digitalRead(led)); 
      delay(200);         
    }
    Serial.read();
    Serial.println("ack");

    digitalWrite(led, LOW);

    lcd.clear();
    lcd.print("Conectado ! ");
    
    //Serial.println("Medidas Electronicas II"); delay(1000); //Mensaje de inicio
    //Serial.println("Medicion de Antena Path"); delay(500); Serial.println("");
    
    //Serial.print("Buscando Posicion Inicial.."); Serial.println("");  
    
    /* Se coloca en la posicion inicial
    while( !digitalRead(A0) )
    {
      motor.step(5, ADELANTE, SINGLE);
    }
    */

    //Serial.println(""); delay(500); 
    //Serial.println("Listo !");  Serial.println(""); delay(500);
}

void loop()
{  
  int k;
  
  if ( Serial.available() > 0 ) 
  {
    input=Serial.read();

    Serial.println("ack");

    if (input=='r')
    {
      //Serial.println("Movimiento Reloj");  Serial.println(""); 

      lcd.clear();
      lcd.print("Comando: r");
    
      
      for(k=0; k<DERECHA; k++)
      {
        digitalWrite(led, !digitalRead(led)); 
        delay(200);         
      }
      
      //motor.step(50, ADELANTE, SINGLE); //Cantidad de pasos, Direccion y Modo  
      
    }
    else if (input=='l')
    {
      //Serial.println("Movimiento Contrareloj");  Serial.println(""); 

      lcd.clear();
      lcd.print("Comando: l");
      
      for(k=0; k<IZQUIERDA; k++)
      {
        digitalWrite(led, !digitalRead(led)); 
        delay(200);         
      }
      
      //motor.step(50, ATRAS, SINGLE); //Cantidad de pasos, Direccion y Modo 
    }
    else if (input=='z')
    {
      //Serial.println("Reseteando.."); Serial.println(""); 

      lcd.clear();
      lcd.print("Comando: z");
      
      for(k=0; k<RESET; k++)
      {
        digitalWrite(led, !digitalRead(led)); 
        delay(200);         
      }
      
      /*
      while( !digitalRead(A0) ) 
      {
          motor.step(5, ADELANTE, SINGLE);
      }
      */
      
      //Serial.println("Listo!");  Serial.println(""); 
    }
  }
}
