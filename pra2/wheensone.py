import matplotlib.pyplot as plt
import numpy as np
import lmfit
from labfis import labfloat

r4, vg = np.loadtxt('ponte').T

print(r4)
print(vg)

ponte = lambda R4,R1,R2,R3,V: (R2/(R1+R2)-R3/(R3+R4))*V

pmodel = lmfit.Model(ponte)

params = pmodel.make_params(R1=150,R2=323,R3=222,V=10)

result = pmodel.fit(vg, params, R4=r4)

res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:5]

coefs = [coef.split() for coef in coefs]

Va = labfloat(float(coefs[3][1]),float(coefs[3][3]))
R3a = labfloat(float(coefs[2][1]),float(coefs[2][3]))
R2a = labfloat(float(coefs[1][1]),float(coefs[1][3]))
R1a = labfloat(float(coefs[0][1]),float(coefs[0][3]))
Vga = labfloat(0)

R4V0 = R3a*((1/(R2a/(R1a+R2a)-Vga/Va)) - 1)

su = "%.16f" % R4V0.uncertainty
i = su.find(".")
if i == -1:
    r = - len(su) + 1
    u = round(R4V0.uncertainty, r)
else:
    r = -i
    r += 1
    for digit in su:
        if digit == "0":
            r += 1
        elif digit != ".":
            u = round(R4V0.uncertainty, r)
u = round(R4V0.uncertainty, r)

R4V0 = "({:g} ± {:g})".format(R4V0.mean,u)

print()

print("R_4 for Vg = 0: {0}".format(R4V0))

plt.plot(r4, result.best_fit,'-',label=r'$(\frac{R_2}{R_1+R_2}-\frac{R_3}{R_3+R_4})\,V$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(r4, vg, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$R_4\,(\Omega)$',fontsize=10)
plt.ylabel(r'$V_G\,(V)$',fontsize=10)
plt.title(r'Ponte de Wheastone',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')



eval("plt.figtext(.665,.176,r'$V_G = 0 \, V \Rightarrow R_4 = "+R4V0+"\, \Omega$',fontsize=10,ha='center')")
#plt.figtext(.30,.223,r"$\frac{e}{k_bT} = 21.12 \pm 0.07 \,\,CJK^{-1}$",fontsize=10,ha='center')
plt.legend()

plt.savefig('ponte.png')
plt.show()