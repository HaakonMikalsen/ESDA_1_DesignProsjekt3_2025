import matplotlib.ticker as mticker 
import codecs
import csv
import numpy as np
import matplotlib.pyplot as plt



dataFile = codecs.open(r"./data.csv", encoding="utf-8", errors="ignore")


skiplinesStart = 1
skiplinesend = 2000
f,x,y1,y2,org = np.array(list(csv.reader(dataFile.readlines()[skiplinesStart:skiplinesend])),dtype=float).T
dataFile.close()









# plt.gca().set_yscale('log')
# plt.gca().set_xscale('log')

plt.style.use("seaborn-v0_8-dark")
plt.title("Fourier analyse av x(t)")
plt.plot(f,x,color="blue",label="x(f)")
plt.grid()
plt.axhline(color = "black")
plt.axvline(color = "black")
plt.axvline(x=720,color = "red",linestyle ="--",linewidth=1,label="720Hz")
# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f '))
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f Hz'))
plt.xlabel("frekvens [Hz]")
plt.ylabel("Amplitude")



plt.legend(frameon=True,edgecolor="dimgray",facecolor="lavender")
# plt.legend()
plt.savefig("xf.png")
plt.show()