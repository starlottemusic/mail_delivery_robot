#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
mail_motor = Motor(Port.C)
driver = DriveBase(left_motor, right_motor, wheel_diameter=85.6, axle_track=163)
drivespeed = 40
section = 0
mail_delivered = 1

gyro_sensor = GyroSensor(Port.S1)
right_ultrasonic = UltrasonicSensor(Port.S2)
line_color_sensor = ColorSensor(Port.S3)
mail_color_sensor = ColorSensor(Port.S4)

ev3.speaker.set_volume(100)