
 double data1=0;
double data2=0;
 double data3=0;
 double data4=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  data1 =data1+random(10);
  data2 =data2+random(10);
  data3 =data3+random(10);
  data4 =data4+random(10);
  Serial.print(data1);
  Serial.print(",");
  Serial.print(data2);
  Serial.print(",");
  Serial.print(data3);
  Serial.print(",");
  Serial.println(data4);
  delay(1000);
}
