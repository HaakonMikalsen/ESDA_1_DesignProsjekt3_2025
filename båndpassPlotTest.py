import numpy as np
import matplotlib.pyplot as plt


def fToW(f):
    return f*2*np.pi

def v2(f,R,L,C):
    w = fToW(f)
    return R/np.sqrt((R**2) + ((w*L)/(1-w**2 * L *C)**2))

def toDB(xout):
    return 20*np.log10(xout)

R = 1e3
L = 1e-1
resonansFrekvens = 720
C = 1/(L*fToW(resonansFrekvens)**2)



# f_verdier = np.linspace(0,20e3,10000)
f_verdier = np.linspace(0,5000,10000)
v2Verdier = v2(f_verdier,R,L,C)
v2VerdierDB = toDB(v2Verdier)

for i in [1,22,100,1000,2000,5000,10_000,100_000,1_000_000]:
    plt.title(f"bånd stopp med motsand på {i}ohm")
    v2Verdier = v2(f_verdier,i,L,C)
    v2VerdierDB = toDB(v2Verdier)
    plt.plot(f_verdier,v2Verdier)
    # plt.plot(f_verdier,v2VerdierDB)
    plt.axhline(y=0,color = "red")
    plt.axvline(x=0,color = "red")
    plt.axvline(x=720,color = "orange")
    plt.gca().set_xscale("log")
    plt.show()