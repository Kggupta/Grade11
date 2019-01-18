//Left motor on ports 3 and 5
#define Left1Output 3
#define Left2Output 5

//Right motor on ports 10 and 9
#define Right1Output 10
#define Right2Output 9

//Line follow sensors
#define linefollowright 11 //Right line follower
#define linefollowleft 7 //Left line follower

// Variables to store what the linefollow sensor detects
byte readerright = 0;//Initialize as 0 for right reader
byte readerleft = 0;//Initialize as 0 for left reader
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);//Serial monitor with 9600 baud rate
  
  //Declaring modes for all motor signals going to L239D controller
  pinMode(Left1Output, OUTPUT);
  pinMode(Left2Output, OUTPUT);
  pinMode(Right1Output, OUTPUT);
  pinMode(Right2Output, OUTPUT);
  
  //Setting the mode for the linefollower pins as input so that they can read what the sensor detects
  pinMode(linefollowright,INPUT);
  pinMode(linefollowleft, INPUT);
}

void loop() {
    readerright = digitalRead(linefollowright); //Update the variable storing the state of the linefollower
    readerleft = digitalRead(linefollowleft);
    
    //Output what the line sensor is reading to the serial monitor 
    Serial.println(digitalRead(readerright));
    Serial.println(digitalRead(readerleft));
    
    if(readerleft == 1 && readerright == 0){//If the left sensor detects black
      right();//Turn right
    }else if(readerleft == 0 && readerright == 1){//If the right sensor detects black
      left();//Turn left
    }else if (readerleft == 0 && readerright == 0){//If both sensors detect not black
      forward();//Go forwars
    }else if (readerleft == 1 && readerright == 1){//If both sensors see black
      stopall();//Stop
    }
    delay(50);//Small delay so that it does not try to change states too quick
}

void forward(){//Function for moving forwaed
  digitalWrite(Left1Output, LOW);//Send signal to left motor to turn forward
  digitalWrite(Left2Output,100);
  digitalWrite(Right1Output, LOW);//Signal to right motor to turn forward
  digitalWrite(Right2Output,100);
  delay(50);//Continue for 50ms
  digitalWrite(Left1Output, LOW);//Stop all motors. This allows for more accurate adjustments from the robot
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(10);//Stay off for 10ms (60ms including main delay in void loop())
}//End of forward


void backward(){//Function for moving backward
  digitalWrite(Left1Output, 100);//Send signal to left motor to turn backward
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, 100);//Send signal to right motor to turn backward
  digitalWrite(Right2Output,LOW);
  delay(50);//Continue for 50ms
  digitalWrite(Left1Output, LOW);//Stop all motors. Allows for more accurate adjustments
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(10);//Stay off for a short period of time
}//End of backward

void right(){//Function to turn right
  digitalWrite(Left1Output, LOW);//Set left motor as moving forward
  digitalWrite(Left2Output,100);
  digitalWrite(Right1Output, 100);//Right motor as turning back
  digitalWrite(Right2Output,LOW);
  delay(50);//Continue for 50ms
  digitalWrite(Left1Output, LOW);//Stop all motors. Allows for more accurate adjustments
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(50);//Stay off for a short period of time
}//End of turning right

void left(){//Funtion to turn left
  digitalWrite(Left1Output, 100);//Set left motor as moving back
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);//Set right motor as moving forward
  digitalWrite(Right2Output,100);
  delay(50);//Continue for 50ms
  digitalWrite(Left1Output, LOW);//Stop all motors. Allows for accurate adjustments
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(50);//Stay off for a short time
}

void stopall(){//Function to stop all motors
  digitalWrite(Left1Output, LOW);//Turn all signal to motors off
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
}//End of stopping all motors
