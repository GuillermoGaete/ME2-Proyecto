/*Modos de exitacion para el motor paso a paso
  SINGLE, DOUBLE, INTERLEAVE, MICROSTEP*/

#include <AFMotor.h> // Libreria para manejo del Driver

#define MODO        SINGLE
#define ADELANTE    FORWARD
#define ATRAS       BACKWARD
#define PASOS       25
#define RETARDO     1000

AF_Stepper motor(256, 2); // Creamos el objeto motor con 256 pasos Puerto 2

int input;

void setup()
{
    pinMode(A0,INPUT);     //Configuracion de GPIOs
    Serial.begin(9600);    //Inicio de comunicacion Serie  
    motor.setSpeed(100);   //Defino la velocidad del motor en RPM
    
    Serial.println("Medidas Electronicas II"); delay(1000); //Mensaje de inicio
    Serial.println("Medicion de Antena Path"); delay(500); Serial.println("");
    
    Serial.print("Buscando Posicion Inicial.."); Serial.println("");  
    
    while( digitalRead(A0) )
    {
      motor.step(5, ADELANTE, SINGLE);
    }

    Serial.println(""); delay(500); 
    Serial.println("Listo !");  Serial.println(""); delay(500);
}

void loop()
{  
  if ( Serial.available() > 0 ) 
  {
    input=Serial.read();
    
    if (input=='r')
    {
      Serial.println("Movimiento Reloj");  Serial.println(""); 
      motor.step(50, ADELANTE, SINGLE); //Cantidad de pasos, Direccion y Modo  
      
    }
    else if (input=='l')
    {
      Serial.println("Movimiento Contrareloj");  Serial.println(""); 
      motor.step(50, ATRAS, SINGLE); //Cantidad de pasos, Direccion y Modo 
    }
    else if (input=='z')
    {
      Serial.println("Reseteando.."); Serial.println(""); 
      
      while( digitalRead(A0) ) 
      {
          motor.step(5, ADELANTE, SINGLE);
      }
      
      Serial.println("Listo!");  Serial.println(""); 
    }
  }
}
