import matplotlib.pyplot as plt
import numpy as np
import math

h,c,hmax,cmax= 0.05,0.05,0,0
H,C,va,ra,voe,roe,vot,rot,vd,ro=[],[],[],[],[],[],[],[],[],[]

while h<10:
    while c<7:
        v=(((2*h*c)+h-(c*c))/math.pi)
        r=(h/c)
        if v<=0:
            vd.append(v)
            ro.append(r)
        if v>0 and r>0 and r<0.8:
            vol=(((2*h*c)+h-(c*c))/math.pi)
            voe.append(vol)
            roe.append(r)
        if v>0 and r>=0.8 and r<=2:
            vol=(((2*h*c)+h-(c*c))/math.pi)
            if vol==100.25:
                hmax=h
                cmax=c
            va.append(vol)
            ra.append(r)
        if v>0 and r>2:
            vol=(((2*h*c)+h-(c*c))/math.pi)
            vot.append(vol)
            rot.append(r)
        H.append(h)
        C.append(c)
        c+=0.05
    c=0.05
    h+=0.05


print("\nFor the ratio where V(c+1)<V(h+1)")
print("x values:",len(ro))
print("y values:",len(vd))

print("\nFor the ratio where V(h+1)>V(c+1)")
print("0<r<0.8: x values: "+str(len(roe))+"; y values: "+str(len(voe)))
print("0.8<r<2: x values: "+str(len(ra))+"; y values: "+str(len(va)))
print("r>2    : x values: "+str(len(rot))+"; y values: "+str(len(vot)))

print("\nFor maximum volume increase: \nRatio: "+str(ra[va.index(max(va))])+"; Length: "+str(hmax)+"; Circumference: "+str(cmax))

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(ro, vd, color='red', marker='x', s=0.1, label='Vd<0')
ax.scatter(ra,va, color='green', marker='x', s=0.1, label='Vd>0: 0.8<=r<=2')
ax.scatter(roe,voe, color='blue', marker='x', s=0.1, label='Vd>0: 0<r<0.8')
ax.scatter(rot,vot, color='blue', marker='x', s=0.1, label='Vd>0: r>2')
ax.legend(loc='best', frameon=True, fancybox=False)
ax.set_title('Vd=V(c+1)-V(h+1) wrt ratio, r(h/c)');
plt.grid(True)
plt.show()
