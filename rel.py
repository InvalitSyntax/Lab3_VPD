#I/usr/bin/env python3
import ev3dev.ev3 as motor
import time

def saturation(u):
    if u>=100:
        return 100
    if u<=-100:
        return -100
    return u

U = 50
def rel(e, u=U):
    if e>=0:
        return u
    if e<=0:
        return -u

motor_a = motor.LargeMotor(motor.OUTPUT_A)
W = 180
filename = "py_rel"+str(U)
f = open(filename, 'w')
startTime = time.time()
startPos = motor_a.position
while ((time.time() - startTime) < 10):
    e=W-(motor_a.position-startPos)
    
    vol=rel(e)

    currentTime = time.time() - startTime
    motor_pose = motor_a.position - startPos
    motor_vel = motor_a.speed
    motor_a.run_direct(duty_cycle_sp = saturation(vol))
    f.write(str(currentTime) + " " + str(motor_pose) + " " + str (motor_vel) + "\n")
    
f.close()

motor_a.stop()
