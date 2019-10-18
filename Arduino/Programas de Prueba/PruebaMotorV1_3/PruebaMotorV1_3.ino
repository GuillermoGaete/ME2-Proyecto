#include <AFMotor.h>                          // Libreria para manejo del Driver para Motores Paso a Paso

#define MODO        SINGLE
#define ADELANTE    FORWARD
#define ATRAS       BACKWARD
#define PASOS       25
#define RETARDO     1000

AF_Stepper motor(256, 2);                     // Creamos el objeto motor con 256 pasos por Vuelta y Puerto 2 (M3-M4)

/*Modos de exitacion para el motor paso a paso
  SINGLE, DOUBLE, INTERLEAVE, MICROSTEP*/

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
   static int i;
   
   for( i = 1 ; i <= 10 ; i++ )
   {
       Serial.println("Avanzando: Posicion N* " + String(i) );
       motor.step(PASOS, ADELANTE, MODO);             
       delay(RETARDO); 
   }
   for( i = 10 ; i >= 1 ; i-- )
   {
       Serial.println("Retrocediendo: Posicion N* " + String(i) );
       motor.step(PASOS, ATRAS, MODO);             
       delay(RETARDO); 
   }                             
}





