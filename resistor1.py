import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import numpy as np

v, i = np.loadtxt('resistor1').T

print(v)
print(i)

plt.scatter(i,v, label='Dados', color='#212121', s=25,zorder=5)


leiohm = lambda i,R,vo: R*i+vo

params, pcov = curve_fit(leiohm, i, v, (i[0],v[0]))

print(*params)

print("R = {0} +- {2} Vo = {1} =- {3}" .format(*params,*np.sqrt(np.diag(pcov))))

vf = leiohm(i,*params)


plt.plot(i,vf,'-',label=r'$Ri+V_o$',linewidth=1.8,color='#adadad',zorder=0)

plt.ylabel(r'Tensão (V)',fontsize=10)
plt.xlabel(r'Corrente (mA)',fontsize=10)
plt.title(r'Resistor',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')
plt.figtext(.75,.196,r"$R = 0.9879 \pm 0.0006 \,\,k\Omega$",fontsize=10,ha='center')
plt.figtext(.75,.153,r"$V_o = 0.0018 \pm 0.0003 \,\,V$",fontsize=10,ha='center')
plt.legend()

plt.savefig('resistor1.pdf')
plt.show()

'''
#plt.savefig('amortecido.pdf')
plt.show()

plt.figure()

plt.plot(tm,yd/ym[0],label=r'$e^{-\gamma t}$')
plt.scatter(tm,abs(ym/ym[0]),label=r'$|A_i/A_o|$')
plt.yscale("log")
plt.xlabel(r'tempo (s)',fontsize=10)
plt.ylabel(r'posição (m)',fontsize=10)
plt.title('Amplitude normalizada',fontsize=15)
plt.legend()
plt.savefig('amortecidolog.pdf')
plt.show()
'''