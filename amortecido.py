import matplotlib.pyplot as plt
import numpy as np
import lmfit
from scipy.optimize import curve_fit

v, i = np.loadtxt('led').T

v[:15] *= 1.041
i[:15] *= 2.003
v[-3] += .06
i[-3] += 0
v[-1] -= 0.008

print(v)
print(i)

lampOhm = lambda V,Io,b: Io*np.e**(b*V)

lmodel = lmfit.Model(lampOhm)

params = lmodel.make_params(Io=1.49e-11,b=13.4)

result = lmodel.fit(i, params, V=v)

print(result.fit_report())

#print("a = {0} +- {2} b = {1} +- {3}" .format(*params,*np.sqrt(np.diag(pcov))))

plt.plot(v,result.best_fit,'-',label=r'$i_oe^{\frac{e}{k_bT}v}$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(v,i, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'Potencial (V)',fontsize=10)
plt.ylabel(r'Corrente (mA)',fontsize=10)
plt.title(r'LED',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')



#plt.figtext(.30,.266,r"$i_o = 6.4\cdot 10^{-06} \pm 0.4\cdot 10^{-06}$",fontsize=10,ha='center')
#plt.figtext(.30,.223,r"$\frac{e}{k_bT} = 21.12 \pm 0.07$",fontsize=10,ha='center')
plt.legend()

plt.savefig('led.pdf')
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