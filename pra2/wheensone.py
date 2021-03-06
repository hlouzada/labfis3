import matplotlib.pyplot as plt
import numpy as np
import lmfit
from labfis import labfloat

r4, vg = np.loadtxt('ponte').T

print(r4)
print(vg)

ponte = lambda R4,ar,R3,V: (ar-R3/(R3+R4))*V

pmodel = lmfit.Model(ponte)

params = pmodel.make_params(ar=0.7,R3=222,V=10)

result = pmodel.fit(vg, params, R4=r4)

res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:5]

coefs = [coef.split() for coef in coefs]

Va = labfloat(float(coefs[2][1]),float(coefs[2][3]))
R3a = labfloat(float(coefs[1][1]),float(coefs[1][3]))
Ar = labfloat(float(coefs[0][1]),float(coefs[0][3]))
Vga = labfloat(0)

R4V0 = R3a*((1/(Ar-Vga/Va)) - 1)

print()

print("R_4 for Vg = 0: {0}".format(R4V0))

#u = "{:g}".format(u).split("e")

#R4V0 = "({:g}".format(R4V0.mean)+"\pm "+u[0]+")"
R4V0 = "("+"\pm".join(R4V0.split())+")"

xs = np.linspace(50,400,200)
ys =  [ponte(xs[j],float(coefs[0][1]),float(coefs[1][1]),float(coefs[2][1])) for j in range(len(xs))]

plt.plot(xs, ys,'-',label=r'$(\frac{R_2}{R_1+R_2}-\frac{R_3}{R_3+R_x})\,V$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(r4, vg, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$R_x\,(\Omega)$',fontsize=10)
plt.ylabel(r'$V_G\,(V)$',fontsize=10)
plt.title(r'Ponte de Wheatstone',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')



eval("plt.figtext(.665,.176,r'$V_G = 0 \, V \Rightarrow R_x = "+R4V0+"\, \Omega$',fontsize=10,ha='center')")
#plt.figtext(.30,.223,r"$\frac{e}{k_bT} = 21.12 \pm 0.07 \,\,CJK^{-1}$",fontsize=10,ha='center')
plt.legend()

plt.savefig('ponte.png')
plt.show()