#I/usr/bin/env python3
import ev3dev.ev3 as motor
import time
import math

Kp = 0.9
Ki = 0
Kd = 0
W = 180
T = 0.025

def saturation(u):
    if u>=100:
        return 100
    if u<=-100:
        return -100
    return u

motor_a = motor.LargeMotor(motor.OUTPUT_A)
filename = "P"+str(Kp)+"I"+str(Ki)+"D"+str(Kd)
f = open(filename, 'w')
e_before=0
t_before=0
s_i=0
startTime = time.time()
startPos = motor_a.position

while ((time.time() - startTime) < 10):
    t1 = time.time()
    e_curr=W-(motor_a.position-startPos)
    
    s_i+=(e_curr+e_before)*((T)/2)
    vol=Kp*(e_curr)+Kd*(e_curr-e_before)/(T)+Ki*s_i
    e_before=e_curr
    #t_before=time.time()

    currentTime = time.time() - startTime
    motor_pose = motor_a.position - startPos
    motor_vel = motor_a.speed
    motor_a.run_direct(duty_cycle_sp = saturation(vol))
    f.write(str(currentTime) + " " + str(motor_pose) + " " + str (motor_vel) + "\n")
    t2 = time.time()
    if (t2-t1) < T:
        time.sleep(T-(t2-t1))
    else:
        print("TI DAUN")

f.close()
motor_a.stop()
