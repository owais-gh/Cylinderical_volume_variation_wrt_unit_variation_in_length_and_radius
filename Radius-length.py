"""
Variation of volume difference when radius and length are considered
Although in real life it would be impossible to have negative values, it is interesting to observe the variation nonetheless
"""

import matplotlib.pyplot as plt
import numpy as np
import math

hmax,hmax0,hmax2,cmax,cmax0,cmax2,hmin,cmin,hmin1,cmin1,rc,vc= 0,0,0,0,0,0,0,0,0,0,0,0
H,C,va,ra,voe,roe,vot,rot,vd,ro=[],[],[],[],[],[],[],[],[],[]

print("\nVolume variation wrt length and radius for integers.")
h=float(input("\nEnter the starting value for length: " ))
ci=float(input("Enter the starting value for radius: "))
hf=float(input("Enter the final value for length: "))
cf=float(input("Enter the final value for radius: "))
print("\nPlease wait while the values are calculated and plotted ...")

c=ci
while h<hf:
    while c<cf:
        v=(((2*h*c)+h-(c*c))*math.pi)
        r=(h/c)
        if v<=0:
            vol = ((2 * h * c) + h - (c * c))*math.pi
            vd.append(v)
            ro.append(r)
            if vol==min(vd):
                hmin=h
                cmin=c
            if vol==max(vd):
                hmin1=h
                cmin1=c
        if v>0 and r>0 and r<0.8:
            vol=((2*h*c)+h-(c*c))*math.pi
            voe.append(vol)
            roe.append(r)
            if vol==max(voe):
                hmax0=h
                cmax0=c
        if v>0 and r>=0.8 and r<=2:
            vol=((2*h*c)+h-(c*c))*math.pi
            va.append(vol)
            ra.append(r)
            if vol==max(va):
                hmax=h
                cmax=c
        if v>0 and r>2:
            vol=((2*h*c)+h-(c*c))*math.pi
            vot.append(vol)
            rot.append(r)
            if vol==max(vot):
                hmax2=h
                cmax2=c
        H.append(h)
        C.append(c)
        c+=0.05
    c=ci
    h+=0.05


maxvol=max(max(voe),max(va),max(vot))
if maxvol==max(voe):
    rat=roe[voe.index(max(voe))]
    hx=hmax0
    cx=cmax0
if maxvol==max(va):
    rat=ra[va.index(max(va))]
    hx=hmax
    cx=cmax
if maxvol==max(vot):
    rat=rot[vot.index(max(vot))]
    hx=hmax2
    cx=cmax2
lowvol=max(abs(max(vd)),abs(min(vd)))
if lowvol==abs(max(vd)):
    ratl=ro[vd.index(max(vd))]
    hlx=hmin1
    clx=cmin1
if lowvol==abs(min(vd)):
    ratl=ro[vd.index(min(vd))]
    hlx=hmin
    clx=cmin


print("\nFor the ratio where V(rad+1)<V(h+1)")
print("x values:",len(ro))
print("y values:",len(vd))

print("\nFor the ratio where V(h+1)>V(rad+1)")
print("0<r<0.8: x values: "+str(len(roe))+"; y values: "+str(len(voe)))
print("0.8<r<2: x values: "+str(len(ra))+"; y values: "+str(len(va)))
print("r>2    : x values: "+str(len(rot))+"; y values: "+str(len(vot)))

print("Total values: " + str(len(ro) + len(roe) + len(ra) + len(rot)))

print("\nFor maximum volume increase for V(rad+1)>V(h+1)(in 0<r<0.8 range): \nRatio: "
      +str(roe[voe.index(max(voe))])+";\nLength: "+str(hmax0)+";\nRadius: "+str(cmax0)+";\nVolume increase: "+str(max(voe)))

print("\nFor maximum volume increase for V(rad+1)>V(h+1)(in 0.8<r<2 range): "
      "\nRatio: "+str(ra[va.index(max(va))])+";\nLength: "+str(hmax)+";\nRadius: "+str(cmax)+";\nVolume increase: "+str(max(va)))

print("\nFor maximum volume increase for V(rad+1)>V(h+1)(in r<2 range): "
      "\nRatio: "+str(rot[vot.index(max(vot))])+";\nLength: "+str(hmax2)+";\nRadius: "+str(cmax2)+";\nVolume increase: "+str(max(vot)))

print("\nFor maximum volume increase for V(rad+1)>V(h+1)(in 0<r range): "
      "\nRatio: "+str(rat)+";\nLength: "+str(hx)+";\nRadius: "+str(cx)+";\nVolume increase: "+str(maxvol))

print("\nFor maximum volume increase for V(rad+1)<V(h+1)[i.e., where increasing the length is better]: "
      "\nRatio: "+str(ratl)+";\nLength: "+str(hlx)+";\nRadius: "+str(clx)+";\nVolume increase: "+str(lowvol))


fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(ro, vd, color='red', marker='x', s=0.1, label='Vd<0')
ax.scatter(ra,va, color='green', marker='x', s=0.1, label='Vd>0: 0.8<=r<=2')
ax.scatter(roe,voe, color='blue', marker='x', s=0.1, label='Vd>0: 0<r<0.8')
ax.scatter(rot,vot, color='blue', marker='x', s=0.1, label='Vd>0: r>2')
ax.legend(loc='best', frameon=True, fancybox=False)
ax.set_title('Vd=V(r+1)-V(h+1) wrt ratio, r(r/c)');
plt.grid(True)
plt.show()





