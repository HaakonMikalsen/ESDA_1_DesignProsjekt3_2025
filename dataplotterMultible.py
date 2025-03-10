import codecs
import csv
import numpy as np
import matplotlib.pyplot as plt



dataFile = codecs.open(r"./data.csv", encoding="utf-8", errors="ignore")


skiplinesStart = 1
skiplinesend = 1000
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


# plt.gca().set_yscale('log')
# plt.gca().set_xscale('log')

plt.title("Forier samlet, justert for magnitude")
plt.plot(f,x,color="blue",label="x(f)")
plt.plot(f,y1,color="orange",label="y_1(f)")
plt.plot(f,y2,color="green", label="y(f)/y_2(f)")
plt.plot(f,y2,color="red", label="orginal")
plt.grid()
plt.axvline(color = "black")
plt.axhline(color = "black")
plt.show()


plt.subplot(1,3,1)
plt.title("Forier samlet, justert for magnitude")
plt.plot(f,x,color="blue",label="x(f)")
# plt.plot(f,y1,color="orange",label="y_1(f)")
# plt.plot(f,y2,color="green", label="y(f)/y_2(f)")
plt.grid()
plt.axvline(color = "black")
plt.axhline(color = "black")



plt.subplot(1,3,2)
plt.title("Forier samlet, justert for magnitude")
plt.plot(f,x,color="blue",label="x(f)")
plt.plot(f,y1,color="orange",label="y_1(f)")
# plt.plot(f,y2,color="green", label="y(f)/y_2(f)")
plt.grid()
plt.axvline(color = "black")
plt.axhline(color = "black")



plt.subplot(1,3,3)
plt.title("Forier samlet, justert for magnitude")
plt.plot(f,x,color="blue",label="x(f)")
# plt.plot(f,y1,color="orange",label="y_1(f)")
plt.plot(f,y2,color="green", label="y(f)/y_2(f)")
plt.grid()
plt.axvline(color = "black")
plt.axhline(color = "black")




plt.legend()
plt.show()