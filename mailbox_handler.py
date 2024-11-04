from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, right_ultrasonic, gyro_sensor, line_color_sensor, mail_color_sensor, section, mail_delivered

def detect():
    global section
    mail_color = mail_color_sensor.color()
    if section == int(0):
        if mail_color == Color.RED:
            deliver_mail()
    elif section == int(1):
        if mail_color == Color.GREEN:
            deliver_mail()
    elif section == int(2):
            if mail_color == Color.BLUE:
                deliver_mail()
    elif section == int(3):
            if mail_color == Color.YELLOW:
                deliver_mail()
        
def deliver_mail():
    driver.stop()
    mail_delivered += 1
    driver.straight(-10) # Adjust value as needed with testing
    ev3.speaker.say("Delivering mail")
    mail_motor.run_angle(-180, 360)
    wait(5000)
    ev3.speaker.say("Have a good day")
    driver.straight(100)
    return