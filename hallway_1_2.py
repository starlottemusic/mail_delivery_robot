from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, sub_ev3, left_motor, right_motor, mail_motor, driver, drivespeed, section, left_ultrasonic, right_ultrasonic, line_color_sensor

def tick():
    sub_ev3.speaker.set_volume(10)
    sub_ev3.speaker.beep()
