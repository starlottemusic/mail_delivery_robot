from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, right_ultrasonic, left_ultrasonic, line_color_sensor, mail_color_sensor, section

def detect():
    global section
    mail_color = mail_color_sensor.color()
    print(mail_color)
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
    
    if section == 1:
        ev3.speaker.play_file("sounds/letters.wav")
    wait(100)
    return # Mail delivery program; this is the ONLY part of the program which should use wait