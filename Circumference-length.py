"""
Variation of volume wrt to circumference and length for the negative values and positive values
Although in real life it would be impossible to have negative values, it is interesting to observe the variation nonetheless
"""

import matplotlib.pyplot as plt
import numpy as np
import math

hmax,cmax,hmin,cmin,rc,vc= 0,0,0,0,0,0
H,C,va,ra,voe,roe,vot,rot,vd,ro=[],[],[],[],[],[],[],[],[],[]

print("\nVolume variation wrt length and circumference for integers.")
h=float(input("\nEnter the starting value for length: " ))
ci=float(input("Enter the starting value for circumference: "))
hf=float(input("Enter the final value for length: "))
cf=float(input("Enter the final value for circumference: "))
print("\nPlease wait while the values are calculated and plotted ...")

c=ci
while h<hf:
    while c<cf:
        v=(((2*h*c)+h-(c*c))/(4*math.pi))
        r=(h/c)
        if v<=0:
            vol = (((2 * h * c) + h - (c * c))/(4*math.pi))
            vd.append(v)
            ro.append(r)
            if vol==min(vd):
                hmin=h
                cmin=c
        if v>0 and r>0 and r<0.8:
            vol=(((2*h*c)+h-(c*c))/(4*math.pi))
            voe.append(vol)
            roe.append(r)
        if v>0 and r>=0.8 and r<=2:
            vol=(((2*h*c)+h-(c*c))/(4*math.pi))
            va.append(vol)
            ra.append(r)
            if vol==max(va):
                hmax=h
                cmax=c
        if v>0 and r>2:
            vol=(((2*h*c)+h-(c*c))/(4*math.pi))
            vot.append(vol)
            rot.append(r)
        H.append(h)
        C.append(c)
        c+=0.05
    c=ci
    h+=0.05


print("\nFor the ratio where V(c+1)<V(h+1)")
print("x values:",len(ro))
print("y values:",len(vd))

print("\nFor the ratio where V(c+1)>V(h+1)")
print("0<r<0.8: x values: "+str(len(roe))+"; y values: "+str(len(voe)))
print("0.8<r<2: x values: "+str(len(ra))+"; y values: "+str(len(va)))
print("r>2    : x values: "+str(len(rot))+"; y values: "+str(len(vot)))

print("\nTotal values: "+str(len(ro)+len(ra)+len(roe)+len(rot)))

print("\nFor maximum volume increase for V(c+1)>V(h+1)[i.e., where increasing the circumference is better]: \nRatio: "
      +str(ra[va.index(max(va))])+";\nLength: "+str(hmax)+";\nCircumference: "+str(cmax)+";\nVolume increase: "+str(max(va)))

print("\nFor maximum volume increase for V(c+1)<V(h+1)[i.e., where increasing the length is better]: \nRatio: "
      +str((ro[vd.index(min(vd))]))+";\nLength: "+str(hmin)+";\nCircumference: "+str(cmin)+";\nVolume increase: "+str(min(vd)))

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(ro, vd, color='red', marker='x', s=0.1, label='Vd<0')
ax.scatter(ra,va, color='green', marker='x', s=0.1, label='Vd>0: 0.8<=r<=2')
ax.scatter(roe,voe, color='blue', marker='x', s=0.1,  label='Vd>0: 0<r<0.8')
ax.scatter(rot,vot, color='blue', marker='x', s=0.1, label='Vd>0: r>2')
ax.legend(loc='best', frameon=True, fancybox=False)
ax.set_title('Vd=V(c+1)-V(h+1) wrt ratio, r(h/c)');
ax.grid(True)
plt.show()