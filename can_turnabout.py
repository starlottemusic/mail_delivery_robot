from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, right_ultrasonic, gyro_sensor, line_color_sensor, mail_color_sensor, section, mail_delivered
import math
import movement_helper

subsection = 0
def tick():
    global subsection, section # Tells method to use external variable, eg. section (allows to be redefined at end)

    if subsection == 0: # Drive forwards until the edge of the checkpoint, then turn 90 degrees CW
        if line_color_sensor.color() == Color.BLUE: 
            driver.drive(100)
            gyro_sensor.reset_angle()
            return
        movement_helper.smart_turn(0, 90)
    
    if subsection == 1: # Drive along a predetermined curve to circumnavigate the can.
        driver.drive(120, -30)
        if (mail_delivered == 3):
            subsection += 1
            
    if subsection == 2: # Turn to face the next checkpoint.
        if movement_helper.smart_turn(0, 90):
            subsection += 1

    if subsection == 3: # Drive to next checkpoint.
        driver.drive(100)
        if (line_color_sensor.color() == Color.BLUE):
            driver.stop()
            section += 1