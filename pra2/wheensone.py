import matplotlib.pyplot as plt
import numpy as np
import lmfit

r4, v = np.loadtxt('ponte').T

print(r4)
print(v)

ponte = lambda R4,R1,R2,R3,V: (R2/(R1+R2)-R3/(R3+R4))*V

pmodel = lmfit.Model(ponte)

params = pmodel.make_params(R1=150,R2=323,R3=222,V=10)

result = pmodel.fit(v, params, R4=r4)

res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:5]

coefs = [coef.split() for coef in coefs]

Va = float(coefs[3][1])
R3a = float(coefs[2][1])
R2a = float(coefs[1][1])
R1a = float(coefs[0][1])
Vga = 0

R4V0 = R3a*((1/(R2a/(R1a+R2a)-Vga/Va)) - 1)

print("R_4 for Vg = 0: {0}".format(R4V0))

#print("a = {0} +- {2} b = {1} +- {3}" .format(*params,*np.sqrt(np.diag(pcov))))

plt.plot(r4, result.best_fit,'-',label=r'$(\frac{R_2}{R_1+R_2}-\frac{R_3}{R_3+R_4})\,V$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(r4, v, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$R_4\,(\Omega)$',fontsize=10)
plt.ylabel(r'$V_g\,(V)$',fontsize=10)
plt.title(r'Ponte de Wheastone',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')



#plt.figtext(.30,.266,r"$i_o = 6.4\cdot 10^{-06} \pm 0.4\cdot 10^{-06} \,\,A$",fontsize=10,ha='center')
#plt.figtext(.30,.223,r"$\frac{e}{k_bT} = 21.12 \pm 0.07 \,\,CJK^{-1}$",fontsize=10,ha='center')
plt.legend()

plt.savefig('ponte.png')
plt.show()