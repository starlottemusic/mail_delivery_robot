#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, right_ultrasonic, gyro_sensor, line_color_sensor, mail_color_sensor, section, mail_delivered
import math
import movement_helper

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 1.2

subsection = 0

def tick():
    global subsection, section

    if subsection == 0: # Drive forwards until the line is detected.
        driver.drive(100, 0)
        if line_color_sensor.color() == Color.BLACK:
            driver.stop()
            subsection += 1

    elif subsection == 1: # Turn such that the line is roughly underneath the light sensor.
        if movement_helper.smart_turn(90, -90):
            subsection += 1

    
    elif subsection == 2: # Follow the line.
        turn_rate = PROPORTIONAL_GAIN * (line_color_sensor.reflection() - threshold)
        driver.drive(100 / ((abs(math.sqrt(turn_rate))) + 1), turn_rate)
        if line_color_sensor.color() == Color.RED | Color.GREEN:
            subsection += 1

    elif subsection == 3: # Follow the centerpoint of red and green; once the final checkpoint is hit, proceed forwards.
        if ColorSensor.color() == Color.GREEN:
            driver.drive(100, -5)
        if ColorSensor.color() == Color.RED:
            driver.drive(100, 5)
        if ColorSensor.color() == Color.BLUE:
            driver.drive(100, 0)