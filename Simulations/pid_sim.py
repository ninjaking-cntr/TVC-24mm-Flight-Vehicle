import math
import matplotlib.pyplot as plt

#numbers
T=10.6  #thrust, N
L=0.15  #lever arm, m 
I=0.006 #moment of inertia, kg·m²
delta=math.radians(2) #gimbal angle, rad

dt=0.001 #time step, s
t_end=0.5 #run length, s

#Starting State
theta=0.0 #tilt,radians
omega=0.0 #spin rate, rad/s

times=[]
tilts=[]

t=0.0
while t < t_end:
    torque=T*math.sin(delta)*L
    alpha=-torque/I #(watch sign: put a minus in front)
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
