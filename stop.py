#I/usr/bin/env python3
import ev3dev.ev3 as motor
import time
motor_a = motor.LargeMotor(motor.OUTPUT_A)
motor_a.stop()