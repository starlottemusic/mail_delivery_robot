from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, left_ultrasonic, right_ultrasonic, line_color_sensor, gyro_sensor, section

i = 0 # i increases by 1 each time "tick" is called. It gives us a way to measure roughly how long the program has been running.
def tick():
    i += i
    global section # Tells method to use external variable, eg. section (allows to be redefined at end)

    if line_color_sensor.color == Color.BLUE & i > 500:
        section = 1