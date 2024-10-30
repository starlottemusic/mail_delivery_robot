#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server (this program) must be started before the client (the other program)!

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, right_ultrasonic, left_ultrasonic, line_color_sensor, gyro_sensor, section
import line_follower
import hallway_1
import mailbox_handler
import bluetooth_server_handler

# The green text after each hashtag is a comment.
# This block of text is ignored by the actual code, so it can be used to annotate code for yourself and others.
# It's generally a good habit to leave comments about what your code does, because you WILL forget otherwise.

#while True:
#    mail_motor.run(-180)

bluetooth_server_handler.setup()

while True: # Loops this section of code constantly

    mailbox_handler.detect() # Run mailbox detection at the start of each repetition

    if section == int(0):
        hallway_1.tick()
    elif section == int(1):
        break
    elif section == int(2):
        break
    elif section == int(3):
        line_follower.tick()