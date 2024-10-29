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

from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, left_ultrasonic, right_ultrasonic, line_color_sensor, gyro_sensor, section
import line_follower
import hallway_1
import mailbox_handler
import bluetooth_server_handler

# The green text after each hashtag is a comment.
# This block of text is ignored by the actual code, so it can be used to annotate code for yourself and others.
# It's generally a good habit to leave comments about what your code does, because you WILL forget otherwise.


bluetooth_server_handler.setup()

while True: # Loops this section of code constantly

    mailbox_handler.detect() # Run mailbox detection at the start of each repetition
    
    match section: # This is a Match-Case statement. It checks a variable (in this case, section) against a list of values, and runs the code for the matching value.
        case 0: # Eg. In this example, if section == 0, it runs hallway_1_2.tick()
            hallway_1.tick()
        case 1:
            break # replace w/ second checkpoint for hallway 2
        case 2:
            break # replace w/ can section
        case 3:
            line_follower.tick()