import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

engFormat = EngFormatter()


def fToW(f):
    return f*2*np.pi

def v2(f,R,L,C):
    w = fToW(f)
    return R/np.sqrt((R**2) + ((w*L)/(1-w**2 * L *C)**2))

def toDB(xout):
    return 20*np.log10(xout)

R = 1e3
L = 0.105 #sett fra funnet verdi
resonansFrekvens = 720
C = 1/(L*fToW(resonansFrekvens)**2)
C_CloesetValues = (470+15)*(10**(-9)) #sett fra funnet verdi

print(C)
print(engFormat(C))

# f_verdier = np.linspace(0,20e3,10000)
f_verdier = np.linspace(0,5000,10000)
v2Verdier = v2(f_verdier,R,L,C)
v2VerdierDB = toDB(v2Verdier)

for i in [1,22,100,1000,2000,5000,10_000,100_000,1_000_000]:
    plt.figure(figsize=(12,8))
    plt.tight_layout()
    plt.subplot(2,1,1)
    plt.title(f"bånd stopp med motsand på {i}ohm")
    v2Verdier = v2(f_verdier,i,L,C)
    v2VerdierCAdjusted = v2(f_verdier,i,L,C_CloesetValues)
    v2VerdierDB = toDB(v2Verdier)
    plt.plot(f_verdier,v2Verdier,linestyle="--",color="orange")
    plt.plot(f_verdier,v2VerdierCAdjusted,color="green")
    # plt.plot(f_verdier,v2VerdierDB)
    plt.axhline(y=0,color = "red")
    plt.axvline(x=0,color = "red")
    plt.axvline(x=720,color = "blue",linestyle="--")
    plt.gca().set_xscale("log")
    plt.subplot(2,1,2)
    plt.title(f"2 bånd stopp med motsand på {i}ohm")
    v2Verdier = v2(f_verdier,i,L,C)
    v2VerdierCAdjusted = v2(f_verdier,i,L,C_CloesetValues)**10
    v2VerdierDB = toDB(v2Verdier)
    plt.plot(f_verdier,v2Verdier,linestyle="--",color="orange")
    plt.plot(f_verdier,v2VerdierCAdjusted,color="green")
    # plt.plot(f_verdier,v2VerdierDB)
    plt.axhline(y=0,color = "red")
    plt.axvline(x=0,color = "red")
    plt.axvline(x=720,color = "blue",linestyle="--")
    plt.gca().set_xscale("log")


    plt.show()