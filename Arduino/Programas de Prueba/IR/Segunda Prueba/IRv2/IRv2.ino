/*---------------------------
IR beam demo
----------------------------*/
#define LED 2
#define BEAM 4

byte i;
void setup()
{
  pinMode(LED,OUTPUT);
  pinMode(BEAM,INPUT);
  digitalWrite(LED,LOW);
}
void loop()
{
  digitalWrite(LED,digitalRead(BEAM));
}
