# Imports
from machine import Pin, PWM
from neopixel import NeoPixel
import time

# Define pins
# LDR
ldr = Pin(34, Pin.IN)
# Neopixel
np = NeoPixel(Pin(5), 16)
# Stepper motor pins
IN1 = Pin(13, Pin.OUT)
IN2 = Pin(12, Pin.OUT)
IN3 = Pin(14, Pin.OUT)
IN4 = Pin(27, Pin.OUT)
# Servo 1 and 2
s1 = PWM(Pin(23), freq=50)
s2 = PWM(Pin(22), freq=50)

# Stepper motor sequence (for spinning the ballerina)
stepper_sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# Function to move the stepper motor
def move_stepper():
    for step in stepper_sequence:
        IN1.value(step[0])
        IN2.value(step[1])
        IN3.value(step[2])
        IN4.value(step[3])
        time.sleep(0.005)

# Main loop
while True:
    # Read LDR value
    ldr_value = ldr.value()
    if ldr_value == 0:
# If light is detected spin the stepper motor, light up neopixel, move servo motors
        for _ in range(500):  
            move_stepper()
        for i in range(16):
            np[i] = (0, 0, 255)
            np.write()
            time.sleep(0.1)
        s1.duty(115)
        s2.duty(40)
        time.sleep(1)
        s1.duty(40)
        s2.duty(115)
        time.sleep(1)

    time.sleep(0.1)
