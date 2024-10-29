from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, left_ultrasonic, right_ultrasonic, line_color_sensor, gyro_sensor, section
from bluetooth_server_handler import mbox

def detect():
    print(mbox.read())
    return
    global section
    mail_color = mbox.read()
    if section == 0 & mail_color == Color.RED:
        deliver_mail()
    elif section == 1 & mail_color == Color.GREEN:
        deliver_mail()
    elif section == 2 & mail_color == Color.BLUE:
        deliver_mail()
    elif section == 3 & mail_color == Color.YELLOW:
        deliver_mail()
        
def deliver_mail():
    driver.brake()
    if section == 1:
        ev3.speaker.play_file("sounds/letters.wav")
    wait(100)
    return # Mail delivery program; this is the ONLY part of the program which should use wait