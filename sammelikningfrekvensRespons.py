import codecs
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 


dataFilter1 = codecs.open(r"./filter 1 v2.csv", encoding="utf-8", errors="ignore")


skiplinesStart = 27
skiplinesend = -1
f,sin,H_1,fase = np.array(list(csv.reader(dataFilter1.readlines()[skiplinesStart:skiplinesend])),dtype=float).T
dataFilter1.close()



dataFilter2 = codecs.open(r"./filter 2 v2.csv", encoding="utf-8", errors="ignore")


skiplinesStart = 27
f,sin,H,fase = np.array(list(csv.reader(dataFilter2.readlines()[skiplinesStart:skiplinesend])),dtype=float).T
dataFilter2.close()






def fToW(f):
    return f*2*np.pi

def v2(f,R,L,C):
    w = fToW(f)
    return R/np.sqrt((R**2) + ((w*L)/(1-w**2 * L *C)**2))

def toDB(xout):
    return 20*np.log10(xout)

R = 1e3
L = 0.098
resonansFrekvens = 720
C = 500e-9



f_verdier = np.linspace(np.min(f),np.max(f),10000)
H1Teoretisk = v2(f_verdier,R,L,C)

R = 1e3
L = 0.105
resonansFrekvens = 720
C = 474e-9



f_verdier = np.linspace(np.min(f),np.max(f),10000)
HTeoretisk = v2(f_verdier,R,L,C)*H1Teoretisk









plt.style.use("seaborn-v0_8-dark")
plt.gca().set_xscale("log")

plt.title("Teoretiske og målte frekvensrespons til filter")
plt.plot(f,H_1,color="green",label="H_1/H_2(w) målt")
plt.plot(f,H,color="orange",label="H(w) målt")
plt.plot(f_verdier,H1Teoretisk,color="green",label="H_1/H_2(w) teoretisk",linestyle="--")
plt.plot(f_verdier,HTeoretisk,color="orange",label="H(w) teoretisk",linestyle="--")
plt.grid()
plt.axhline(color = "black")
plt.axvline(color = "black")
plt.axvline(x=720,color = "red",linestyle ="--",linewidth=1,label="720Hz/resonansfrekvens")
# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f '))
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f Hz'))
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f dB'))
plt.xlabel("frekvens [Hz]")
plt.ylabel("Demping")



plt.legend(frameon=True,edgecolor="dimgray",facecolor="lavender")
# plt.legend()
plt.savefig("hplot.png")
plt.show()