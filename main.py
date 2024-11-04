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

from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, right_ultrasonic, gyro_sensor, line_color_sensor, mail_color_sensor, section, mail_delivered
import hallway_1
import hallway_2
import can_turnabout
import line_follower
import mailbox_handler

# The green text after each hashtag is a comment.
# This block of text is ignored by the actual code, so it can be used to annotate code for yourself and others.
# It's generally a good habit to leave comments about what your code does, because you WILL forget otherwise.

while True: # Loops this section of code constantly

    # print("left" + str(left_ultrasonic.distance()))
    # print("right" + str(right_ultrasonic.distance()))
    # print("gyro" + str(gyro_sensor.angle()))
    # print(mail_color_sensor.color())

    mailbox_handler.detect() # Run mailbox detection at the start of each repetition

    if section == 0: # Iterate over all possible values of section; run that checkpoint's program
        hallway_1.tick()
    elif section == 1:
        hallway_2.tick()
    elif section == 2:
        can_turnabout.tick()
    elif section == 3:
        if mail_delivered == 4:
            ev3.speaker.say("All mail has been delivered. I hope I did well!")
            break
        line_follower.tick()