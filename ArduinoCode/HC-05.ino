#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_BME280.h>
#include <SoftwareSerial.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_MPU6050 mpu;
Adafruit_BME280 bme;
unsigned long startTime;

SoftwareSerial BTSerial(0, 1); // RX, TX pins for HC-05

void setup() {
  Serial.begin(115200);
  BTSerial.begin(115200); // Adjust baud rate as per your HC-05 module configuration

  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  Wire.begin();
  if (!mpu.begin()) {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
    while (1);
  }

  startTime = millis(); // Record the start time
}

void loop() {
  //Serial.println("hello world");
  // Continue running the loop until 20 seconds have elapsed
  if (millis() - startTime <= (60000*5)) {
    unsigned long currentTime = millis(); // Get the current time in milliseconds
    
    // Read MPU6050 sensor data
    sensors_event_t accel, gyro, temp;
    mpu.getEvent(&accel, &gyro, &temp);

    // Construct CSV string
    String dataString = String(currentTime) + "," +
                        String(accel.acceleration.x) + "," +
                        String(accel.acceleration.y) + "," +
                        String(accel.acceleration.z) + "," +
                        String(gyro.gyro.x) + "," +
                        String(gyro.gyro.y) + "," +
                        String(gyro.gyro.z) + "," +
                        String(bme.readTemperature()) + "," +
                        String(bme.readPressure() / 100.0F) + "," +
                        String(bme.readAltitude(SEALEVELPRESSURE_HPA)) + "," +
                        String(bme.readHumidity());

    // Send CSV string over Bluetooth
    Serial.println(dataString);

    
  } else {
    Serial.println("Program finished after 20 seconds.");
    while (1); // End the program
  }
  delay(5);
}
