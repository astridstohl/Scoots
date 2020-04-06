int MotorControl = 5;    // Digital Arduino Pin used to control the motor J3
int MotorControl2 = 4;    // Digital Arduino Pin used to control the motor J4
int MotorControl3 = 6;    // Digital Arduino Pin used to control the motor J2
int MotorControl4 = 7;    // Digital Arduino Pin used to control the motor J1

// the setup routine runs once when you press reset:
void setup()  {
  pinMode(MotorControl, OUTPUT); // declare pins 4, 5, 6, and 7 to be an output:
  pinMode(MotorControl2, OUTPUT);
  pinMode(MotorControl3, OUTPUT);
  pinMode(MotorControl4, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop()  {
  // NO3 and COM3 Connected (the motor is running)
  digitalWrite(MotorControl,HIGH); // wait 1000 milliseconds (1 second)
  digitalWrite(MotorControl2,HIGH);
  delay(1200); // wait 1000 milliseconds (1 second)
  // NO3 and COM3 Disconnected (the motor is not running)
  
  
  digitalWrite(MotorControl,LOW);
  digitalWrite(MotorControl2,LOW);
  delay(5000); // wait 5000 milliseconds (5 seconds)


  digitalWrite(MotorControl4,HIGH);
  delay(2000);
  digitalWrite(MotorControl4,LOW);
}
