'''
Volume=Pi*radius^2*height
Consider two cylinder with same length,h, radius,r and volume,V.
Now for one cylinder radius is increased by 1 unit and for other length in increased by 1 unit
So now two cylinders have volume of V(r+1) and V(h+1).
where V(r+1)=pi(r+1)^2*h)
simplified v(r+1)=pi(r^2*h+h+2*r*h)
and v(h+1)=pi*r^2*(h+1)
simplified v(h+1)=pi(r^2*h+r^2)
For the difference in the volume between two cylinders after increasing 1 unit
vd=v(r+1)-v(h+1)
simplified vd=pi(h+2*r*h-r^2)

note: code is tested for neg to pos and zero to pos values but not for neg to zero. The vol difference might be wrong
for that range.

Since the strength of material depends on volume, it might be really helpful to understand if structure can be
strengthened by increasing radius or increasing length.
Also if you friend asks if you would increase you penile length by a unit or circumference by a unit, you could now
answer to get the maximum penile volume increment.

'''
