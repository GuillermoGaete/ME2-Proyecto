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
    Serial.println("Prueba de Motor");        //Mensaje de inicio
    Serial.println("Tipo de paso: Single");    //Imprimo el modo de trabajo
    motor.setSpeed(100);                      //Defino la velocidad del motor en RPM
}

void loop()
{  
   motor.step(25, FORWARD, SINGLE);           //Cantidad de pasos, Direccion y Modo de trabajo     
   delay(1000);                               //Retardo
}





