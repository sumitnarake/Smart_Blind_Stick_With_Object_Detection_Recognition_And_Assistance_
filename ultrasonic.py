import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set GPIO pin numbers
TRIG_PIN = 18
ECHO_PIN = 24

# Set GPIO pin numbers
TRIG_PIN_1 = 16
ECHO_PIN_1 = 20

# Set GPIO pin numbers
TRIG_PIN_2 = 19
ECHO_PIN_2 = 10

# Set GPIO mode and pin numbering

# Set up the ultrasonic sensor pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Set up the ultrasonic sensor pins
GPIO.setup(TRIG_PIN_1, GPIO.OUT)
GPIO.setup(ECHO_PIN_1, GPIO.IN)

# Set up the ultrasonic sensor pins
GPIO.setup(TRIG_PIN_2, GPIO.OUT)
GPIO.setup(ECHO_PIN_2, GPIO.IN)

def get_distance():
    # Send a pulse to the ultrasonic sensor
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Wait for the ultrasonic sensor to send a pulse back
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calculate the distance in centimeters
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance


def get_distances():
    # Send a pulse to the ultrasonic sensor
    GPIO.output(TRIG_PIN_1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN_1, False)

    # Wait for the ultrasonic sensor to send a pulse back
    while GPIO.input(ECHO_PIN_1) == 0:
        pulse_start_1 = time.time()

    while GPIO.input(ECHO_PIN_1) == 1:
        pulse_end_1 = time.time()

    # Calculate the distance in centimeters
    pulse_duration_1 = pulse_end_1 - pulse_start_1
    distance_1 = pulse_duration_1 * 17150
    distance_1 = round(distance_1, 2)
    
    return distance_1
    
    
def get_distancess():
    # Send a pulse to the ultrasonic sensor
    GPIO.output(TRIG_PIN_2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN_2, False)

    # Wait for the ultrasonic sensor to send a pulse back
    while GPIO.input(ECHO_PIN_2) == 0:
        pulse_start_2 = time.time()

    while GPIO.input(ECHO_PIN_2) == 1:
        pulse_end_2 = time.time()

    # Calculate the distance in centimeters
    pulse_duration_2 = pulse_end_2 - pulse_start_2
    distance_2 = pulse_duration_2 * 17150
    distance_2 = round(distance_2, 2)
    
    return distance_2
    
    
try:
    while True:
        print(get_distance())     
        print(get_distances())     
        print(get_distancess())     
            
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

