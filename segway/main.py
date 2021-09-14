#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port

# Initialize the EV3 Brick.
ev3 = EV3Brick()
gyro = GyroSensor(Port.S1)
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

kp = 10
ki = 4
kd = 10

target = 0
integral = 0
derivative = 0
error = 0
prev_error = 0

x = 0

gyro.angle_reset(0)

while True:
    error = target + gyro.angle()
    integral = integral + error
    derivative = error - prev_error
    prev_error = error
    x = kp * error + ki * integral + kd * derivative
    left_motor.dc(x)
    right_motor.dc(x)
