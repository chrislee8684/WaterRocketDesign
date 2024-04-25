import machine
import time
import MPU6050

import bme280       #importing BME280 library


i2c=machine.I2C(0,sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)    #initializing the I2C method
i2c1 = machine.I2C(1, sda=machine.Pin(2), scl=machine.Pin(3))

# Set up the MPU6050 class 
mpu = MPU6050.MPU6050(i2c1)

# wake up the MPU6050 from sleep
mpu.wake()

while True:
    bme = bme280.BME280(i2c=i2c)          #BME280 object created
    print(bme.values)
    gyro = mpu.read_gyro_data()
    accel = mpu.read_accel_data()
    print("Gyro: " + str(gyro) + ", Accel: " + str(accel))
    time.sleep(0.05)           #delay