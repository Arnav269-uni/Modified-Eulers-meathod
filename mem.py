import numpy as np
import sympy as sp
x,y=sp.symbols("x,y")
f_ip="x+y"
f=sp.sympify(f_ip)
lam_f=sp.lambdify((x,y),f,'numpy')
x0=0
y0=1
xn=0.4
h=0.1
xarr=np.arange(x0,xn+h,h)
yarr=np.zeros(100)
ycv=np.zeros(100)
yarr[0]=y0
for i in range(1,len(xarr)):
    c=1
    yarr[i]=yarr[i-1]+h*lam_f(xarr[i-1],yarr[i-1])
    print(f"y(x1)={yarr[i]}")
    ycv[i-1]=yarr[i]
    print(f"y{i}={yarr[i]}")
    while True:
        ycv[c]=yarr[i-1]+(h/2)*(lam_f(xarr[i-1],yarr[i-1])+lam_f(xarr[i],yarr[c-1])) 
        
        if(abs(ycv[c]-ycv[c-1])<0.00005):
            
            print(f"final solution is {ycv[c]}")
            yarr[i]=ycv[c]
            break
        else:
            print(f"{c} corrected value is: {ycv[c]}")
            c=c+1
            continue




