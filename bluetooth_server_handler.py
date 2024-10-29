# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.media.ev3dev import SoundFile, ImageFile
from init import ev3, left_motor, right_motor, mail_motor, driver, drivespeed, left_ultrasonic, right_ultrasonic, line_color_sensor, gyro_sensor, section

def setup():
    server = BluetoothMailboxServer()
    mbox = TextMailbox('mail_color', server)

    # The server must be started before the client!
    print('waiting for connection...')
    ev3.speaker.play_file("sounds/ready_to_pair.wav")
    server.wait_for_connection()
    print('connected!')
    ev3.speaker.play_file("sounds/connected.wav")