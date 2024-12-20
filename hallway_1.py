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
PROPORTIONAL_GAIN = 5
def tick():
    global subsection, section # Tells method to use external variable, eg. section (allows to be redefined at end)

    if subsection == 0: # First subsection; drive straight at exactly 50mm from the wall until floor is red, then advance to next.
        turn_angle = math.sqrt(right_ultrasonic.distance() - 50) # VERY rough PID estimate; sqrt of proportional difference to dampen extremes.
        driver.drive(200, PROPORTIONAL_GAIN * turn_angle)
        if line_color_sensor.color() == Color.RED:
                subsection += 1

    elif subsection == 1: # Drive straight to roughly center with the hallway, then turn 90 degrees left using the gyro.
        driver.straight(250)
        subsection += 1

    elif subsection == 2: # Turn 90 degrees CCW using the gyro for stability.
        if movement_helper.smart_turn(0, -90):
            subsection += 1

    elif subsection == 3: # Drive forwards until ultrasonic sensor detects wall, indicating a hallway.
         driver.drive(200, 0)
         if (right_ultrasonic.distance() < 50):
            driver.straight(100) # Drive further for sensor consistency; adjust to minimum needed.
            subsection += 1

    elif subsection == 4: # Navigate hallway until mail is delivered.
        turn_angle = math.sqrt(right_ultrasonic.distance() - 30)
        driver.drive(100, PROPORTIONAL_GAIN * turn_angle)
        if (mail_delivered == 1):
            subsection += 1

    elif subsection == 5: # Drive forwards until checkpoint 2 is reached (PID no longer used to avoid issues when exiting hallway)
        driver.drive(100, 0)
        if (line_color_sensor.color == Color.BLUE):
            driver.stop()
            section += 1