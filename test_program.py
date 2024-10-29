#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialization
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
mail_motor = Motor(Port.C)
driver = DriveBase(left_motor, right_motor, wheel_diameter=85.6, axle_track=163)
drivespeed = 40

# Movement Program
driver.straight(500)
ev3.speaker.beep()

driver.straight(-500)
ev3.speaker.beep()

driver.turn(360)

ev3.speaker.beep()

driver.turn(-360)
ev3.speaker.beep()

# Mail Program
driver.curve
mail_motor.run_angle(360, 360, Stop.HOLD, True)