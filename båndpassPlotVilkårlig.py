import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

def fToW(f):
    return f*2*np.pi

def v2(f,R,L,C):
    w = fToW(f)
    return R/np.sqrt((R**2) + ((w*L)/(1-w**2 * L *C)**2))

def toDB(xout):
    return 20*np.log10(xout)

R = 1e3
L = 0.80 #sett fra funnet verdi
resonansFrekvens = 500
C = 1/(L*fToW(resonansFrekvens)**2)


f_verdier = np.linspace(0,1000,10000)
v2Verdier = v2(f_verdier,R,L,C)
v2VerdierDB = toDB(v2Verdier)

# plt.figure(figsize=(12,8))
plt.style.use("seaborn-v0_8-dark")
plt.axhline(y=0,color = "black",alpha=0.5)
plt.axvline(x=0,color = "black",alpha=0.5)
plt.grid()
plt.plot(f_verdier,v2VerdierDB,color="orange",label="V2(f)")
# plt.gca().set_xscale("log")
plt.title(f"Båndstopp frekvens mot desibell. Vilkårlige verdier")
plt.xlabel("Frekvens")
plt.ylabel("Demping")
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f dB'))
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f Hz'))
plt.legend(frameon=True,edgecolor="dimgray",facecolor="lavender")
plt.savefig("vilkårligVerdi.png")
plt.show()