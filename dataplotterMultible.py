import codecs
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


dataFile = codecs.open(r"./data.csv", encoding="utf-8", errors="ignore")


skiplinesStart = 1
skiplinesend = 5000
f,x,y1,y2,org = np.array(list(csv.reader(dataFile.readlines()[skiplinesStart:skiplinesend])),dtype=float).T
dataFile.close()





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


f_verdier = np.linspace(0,5000,10000)
v2Verdier = v2(f_verdier,R,L,C)

plt.style.use("seaborn-v0_8-dark")

plt.gca().set_yscale('log')
# plt.gca().set_xscale('log')

plt.title("Frekvensspektrum of x og y1 og y2")
plt.plot(f,y2,color="blue", label="y2/ŷ(f)",alpha=1)
plt.plot(f,y1,color="red", label="y1(f)",alpha=0.5)
plt.plot(f,x,color="green", label="x(f)",alpha=0.2)
plt.xlabel("Frekvens")
plt.ylabel("Amplitude")
plt.grid()
plt.axvline(color = "black")
plt.axhline(color = "black")
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f Hz'))
plt.legend(frameon=True,edgecolor="dimgray",facecolor="lavender")
plt.savefig("xy1y.png",dpi=1000)
plt.show()