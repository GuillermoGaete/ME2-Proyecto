#include <Stepper.h>

#define STEPS 256

Stepper stepper(STEPS, 7, 6, 5, 4);
 
void setup() 
{
   stepper.setSpeed(50);
}
 
void loop() 
{
   stepper.step(2048); 
}
