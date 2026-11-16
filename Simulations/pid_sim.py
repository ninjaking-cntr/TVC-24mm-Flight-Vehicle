import math
import matplotlib.pyplot as plt

#numbers
T=10.6  #thrust, N
L=0.15  #lever arm, m 
I=0.006 #moment of inertia, kg·m²
k_aero=-30 #aerodynamic indstability,1/s^2
Kp=1.0
Kd=0.09
t_burn=0.5 #motor burn time, s

dt=0.001 #time step, s
t_end=1.5 #run length, s

#Starting State
theta=math.radians(2) #tilt,radians
omega=0.0 #spin rate, rad/s
delta_actual=0.0

times=[]
tilts=[]

t=0.0
tau=0.03 #servos time constant,s
delta_max=math.radians(7)
while t < t_end:
    delta=Kp*theta+Kd*omega
    if delta > delta_max:
        delta = delta_max
    elif delta < -delta_max:
        delta = -delta_max
    delta_actual=delta_actual+(delta-delta_actual)*dt/tau
    if t<t_burn:
        thrust=T
    else:
        thrust=0
    torque=thrust*math.sin(delta_actual)*L
    alpha=-torque/I+k_aero*theta #(watch sign: put a minus in front)
    omega=omega+alpha*dt
    theta=theta+omega*dt
    times.append(t)
    tilts.append(math.degrees(theta))
    t=t+dt

print("Final tilt:", tilts[-1], "degrees")

plt.plot(times,tilts)
plt.xlabel("Time(s)")
plt.ylabel("Tilt(deg)")
plt.show()
