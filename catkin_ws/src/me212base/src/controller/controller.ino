// Zack Bright        - zbright  _ mit _ edu,    Sept 2015
// Daniel J. Gonzalez - dgonz    _ mit _ edu,    Sept 2015
// Fangzhou Xia       - xiafz    _ mit _ edu,    Sept 2015
// Peter KT Yu        - peterkty _ mit _ edu,    Sept 2016
// Ryan Fish          - fishr    _ mit _ edu,    Sept 2016

#include "Arduino.h"
#include "helper.h"
#include <ServoTimer2.h>

EncoderMeasurement  encoder(26);      // encoder handler class, set the motor type 53 or 26 here
RobotPose           robotPose;        // robot position and orientation calculation class
PIController        wheelVelCtrl;     // velocity PI controller class
SerialComm          serialComm;       // serial communication class
ServoTimer2         myservo;          // create servo object
unsigned long       prevTime = 0;
void endEffectorMotion(int);
void pickBox();
void dropBox();
void prePickPicka();
void pickPicka();
void dropPicka();

boolean usePathPlanner = true;

void setup() {
    Serial.begin(115200);       // initialize Serial Communication
    encoder.init();             // connect with encoder
    wheelVelCtrl.init();        // connect with motor
    myservo.attach(2);         // attaches servo to pin 10
    delay(1e3);                 // delay 1000 ms so the robot doesn't drive off without you

}


void loop() {
    //timed loop implementation
    unsigned long currentTime = micros();
    
    if (currentTime - prevTime >= PERIOD_MICROS) {
      
        // 1. Check encoder
        encoder.update(); 

        // 2. Update position
        robotPose.update(encoder.dThetaL, encoder.dThetaR); 

        // 3. Send odometry through serial communication
        serialComm.send(robotPose); 
        serialComm.receiveSerialData();

        // 4. Send the velocity command to wheel velocity controller
        wheelVelCtrl.doPIControl("Left",  serialComm.desiredWV_L, encoder.v_L); 
        wheelVelCtrl.doPIControl("Right", serialComm.desiredWV_R, encoder.v_R);
        
        endEffectorMotion(serialComm.task);
        serialComm.task = 0;
        prevTime = currentTime; // update time
    } 
}
    
// Decide what motion to use for gripper task
// 1: pickBox
// 2: dropBox
// 3: prePickPicka
// 4: pickPicka
// 5: dropPicka

void endEffectorMotion(int task)
{
  switch (task) {
      case 1:
        pickBox();
        break;
      case 2:
        dropBox();
        break; 
      case 3:
        prePickPicka();
        break;
      case 4:
        pickPicka();
        break;
      case 5:
        dropPicka();
        break;
  } 
}

void pickBox() {
  // moves from initial postion the picked box position
    myservo.write(1600);    // Move servo         
    delay(600);          // Set Move time  
    myservo.write(1500);    // Stop servo                 
}

void dropBox() {
  // moves from the gripped postion for the box to the initial position
    myservo.write(1350);    // Move servo         
    delay(450);          // Set Move time           
    myservo.write(1500);    // Stop servo         
}

void prePickPicka() {
  // moves from initial postion to the pre position for picking the picka
    //myservo.write(105);    // Move servo         
    //delay(450);          // Set Move time           
    //myservo.write(90);    // Stop servo         
}

void pickPicka() {
  // moves from initial postion the picked picka position
    myservo.write(1600);    // Move servo         
    delay(1000);          // Set Move time           
    myservo.write(1500);    // Stop servo         
}

void dropPicka() {
  // moves from the gripped postion for the picka to the initial position
    myservo.write(1350);    // Move servo         
    delay(700);          // Set Move time           
    myservo.write(1500);    // Stop servo         
}


