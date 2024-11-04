from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, right_ultrasonic, gyro_sensor, line_color_sensor, mail_color_sensor, section, mail_delivered
import math

driver.drive

def smart_turn(speed, angle):
    """smart_turn(speed (mm/s), angle (deg))

    Uses the gyro sensor to turn at a precise angle along an arc. Returns 'True' when completed"""
    
    driver.drive(speed, angle)
    if gyro_sensor.angle(angle):
        driver.stop
        return True
    return False