import matplotlib.pyplot as plt
import numpy as np
import lmfit

v, i = np.loadtxt('diodo').T

print(v)
print(i)

lampOhm = lambda V,Io,b,T: Io*np.e**(b*V)

lmodel = lmfit.Model(lampOhm)

params = lmodel.make_params(Io=5.73*10**-6,b=21.3)

result = lmodel.fit(i, params, V=v)

print(result.fit_report())

#print("a = {0} +- {2} b = {1} +- {3}" .format(*params,*np.sqrt(np.diag(pcov))))

plt.plot(v,result.best_fit,'-',label=r'$i_oe^{\frac{e}{k_bT}v}$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(v,i, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'Tensão $(V)$',fontsize=10)
plt.ylabel(r'Corrente $(mA)$',fontsize=10)
plt.title(r'Diodo',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')



plt.figtext(.30,.266,r"$i_o = 6.4\cdot 10^{-06} \pm 0.4\cdot 10^{-06} \,\,A$",fontsize=10,ha='center')
plt.figtext(.30,.223,r"$\frac{e}{k_bT} = 21.12 \pm 0.07 \,\,CJK^{-1}$",fontsize=10,ha='center')
plt.legend()

plt.savefig('diodo.png')
plt.show()

'''
#plt.savefig('amortecido.png')
plt.show()

plt.figure()

plt.plot(tm,yd/ym[0],label=r'$e^{-\gamma t}$')
plt.scatter(tm,abs(ym/ym[0]),label=r'$|A_i/A_o|$')
plt.yscale("log")
plt.xlabel(r'tempo (s)',fontsize=10)
plt.ylabel(r'posição (m)',fontsize=10)
plt.title('Amplitude normalizada',fontsize=15)
plt.legend()
plt.savefig('amortecidolog.png')
plt.show()
'''