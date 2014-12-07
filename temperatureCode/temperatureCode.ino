
// demo of Starter Kit V2.0 - Grove Temperature Sensor

const int pinTemp = A0;      // pin of temperature sensor

float temperature;
int B=3975;                  // B value of the thermistor
float resistance;

void setup()
{
  
  Serial.begin(9600);  
  float ctemp;
    while(true){
     ctemp = getTemp();
     Serial.println(ctemp);
    }
    
}

float getTemp()
{
    int val = analogRead(pinTemp);                               // get analog value
    resistance=(float)(1023-val)*10000/val;                      // get resistance
    temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;     // calc temperature
       
    delay(6000);          // delay 1s
    return temperature;
}

void loop(){
}
