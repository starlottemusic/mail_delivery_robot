from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, right_ultrasonic, left_ultrasonic, line_color_sensor, mail_color_sensor, section

subsection = 0
def tick():
    global i, subsection, line_color_sensor, section # Tells method to use external variable, eg. section (allows to be redefined at end)
    # print("left" + str(left_ultrasonic.distance()))
    # print("right" + str(right_ultrasonic.distance()))
    # print("gyro" + str(gyro_sensor.angle()))
    if subsection == 0:
        driver.drive(200, 0)
        if line_color_sensor.color() == Color.RED:
                subsection += 1
    if subsection == 1:
        driver.straight(250)
        driver.turn(-90)
        subsection += 1
    elif subsection == 2:
         driver.drive(200, 0)
         if (right_ultrasonic.distance() < 50) & (left_ultrasonic.distance() < 50):
            driver.straight(100)
            subsection += 1
    elif subsection == 3:
        turn_angle = left_ultrasonic.distance() - right_ultrasonic.distance()
        driver.drive(100, 2 * turn_angle)
        if (mail_color_sensor == Color.RED):
            subsection += 1
    elif subsection == 4:
        driver.drive(100, 0)
        if (line_color_sensor.color == Color.BLUE):
            section += 1