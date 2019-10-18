#include <Stepper.h>

#define MODO        SINGLE
#define ADELANTE    FORWARD
#define ATRAS       BACKWARD
#define PASOS       25
#define RETARDO     1000

#define STEPS 256

Stepper motor(STEPS, 7, 6, 5, 4);

void setup()
{
    Serial.begin(9600);                       //Inicio de comunicacion Serie  
    
    motor.setSpeed(100);                      //Defino la velocidad del motor en RPM
    
    //Mensaje de inicio
    Serial.println("Medidas Electronicas II"); delay(1000);
    Serial.println("Prueba de Motor");         delay(500); 
    Serial.println("Tipo de paso: Simple");    delay(500);
    Serial.print("Iniciando");delay(500);Serial.print(".");delay(500);Serial.print(".");delay(500);Serial.print(".");delay(500); Serial.println(" "); delay(500);           
}

void loop()
{  
    motor.step(PASOS);   
    delay(1000);    
}



