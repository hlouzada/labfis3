import matplotlib.pyplot as plt
import numpy as np
import lmfit
T1 = [0.065, 0.069, 0.075]
T2 = [0.088, 0.130, 0.135]
T3 = [0.136, 0.152, 0.164]

X1 = [7,13,19]
X2 = [25, 31, 37]
X3 = [43,49,55]

reg1 = lmfit.models.LinearModel(['x'])
reg2 = lmfit.models.LinearModel(['x'])
reg3 = lmfit.models.LinearModel(['x'])

result1 = reg1.fit(T1, x=X1)
result2 = reg2.fit(T2, x=X2)
result3 = reg3.fit(T3, x=X3)

#print(result.fit_report())

#print("a = {0} +- {2} b = {1} +- {3}" .format(*params,*np.sqrt(np.diag(pcov))))

#plt.plot(v,result.best_fit,'-',label=r'$i_oe^{\frac{e}{k_bT}v}$',linewidth=1.8,color='#adadad',zorder=0)

plt.scatter(X1, T1, color='#212121', s=25,zorder=5)
plt.scatter(X2, T2, color='#212121', s=25,zorder=5)
plt.scatter(X3, T3, color='#212121', s=25,zorder=5)
plt.plot(X1,result1.best_fit,'-.',label='Região 1',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(X2,result2.best_fit,'--',label='Região 2',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(X3,result3.best_fit,':',label='Região 3',linewidth=1.8,color='#adadad',zorder=0)


plt.xlabel(r'Comprimento $(cm)$',fontsize=10)
plt.ylabel(r'Tensão $(V)$',fontsize=10)
plt.title(r'Fita de Alumínio',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')
#plt.figtext(.30,.266,r"$i_o = 6.4\cdot 10^{-06} \pm 0.4\cdot 10^{-06}$",fontsize=10,ha='center')
#plt.figtext(.30,.223,r"$\frac{e}{k_bT} = 21.12 \pm 0.07$",fontsize=10,ha='center')
plt.legend()

plt.savefig('fita.png')
plt.show()