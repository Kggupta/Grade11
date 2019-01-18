#include <IRremote.h>

const int IRRecPin = 12;
IRrecv irrecv(IRRecPin);
decode_results results;
unsigned long key_value = 0;
#define Left1Output 3
#define Left2Output 5
#define Right1Output 10
#define Right2Output 9

#define linefollowright 11
#define linefollowleft 7
byte readerright = 0;
byte readerleft = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  irrecv.enableIRIn();
  irrecv.blink13(true);
  pinMode(Left1Output, OUTPUT);
  pinMode(Left2Output, OUTPUT);
  pinMode(Right1Output, OUTPUT);
  pinMode(Right2Output, OUTPUT);
  pinMode(linefollowright,INPUT);
  pinMode(linefollowleft, INPUT);
  pinMode(IRRecPin, INPUT);
}

void loop() {
  if (irrecv.decode(&results)){
    switch(results.value){
      case 0x3D9AE3F7:
      forward();
      break;
      case 0x1BC0157B:
      backward();
      break;
    }
    irrecv.resume(); 
    delay(20);
  }
}

void forward(){
  digitalWrite(Left1Output, LOW);
  digitalWrite(Left2Output,100);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,100);
  delay(50);
  digitalWrite(Left1Output, LOW);
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(10);
}


void backward(){
  digitalWrite(Left1Output, 100);
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, 100);
  digitalWrite(Right2Output,LOW);
  delay(50);
  digitalWrite(Left1Output, LOW);
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(10);
}

void right(){
  digitalWrite(Left1Output, LOW);
  digitalWrite(Left2Output,100);
  digitalWrite(Right1Output, 100);
  digitalWrite(Right2Output,LOW);
  delay(50);
  digitalWrite(Left1Output, LOW);
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(50);
}

void left(){
  digitalWrite(Left1Output, HIGH);
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,HIGH);
  delay(50);
  digitalWrite(Left1Output, LOW);
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
  delay(50);
}

void stopall(){
  digitalWrite(Left1Output, LOW);
  digitalWrite(Left2Output,LOW);
  digitalWrite(Right1Output, LOW);
  digitalWrite(Right2Output,LOW);
}
