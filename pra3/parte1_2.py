import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('carga2')

vc = np.array([k[0] for k in dados])
t = np.array([k[2] for k in dados])

print(vc)
print(t)

vo = 10
tal = 106e-6*224e3

capacitor = lambda t,Vo,Tal: Vo*np.exp(-t/Tal)
cmodel = lmfit.Model(capacitor)
params = cmodel.make_params(Vo=vo,Tal=tal)
result = cmodel.fit(vc, params, t=t)
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

xs = np.linspace(1.5,34,200)
ys = np.array([capacitor(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])

plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$V_o e^{\frac{-t}{\tau}}$',linewidth=1.8,color='#adadad',zorder=0)
plt.scatter(t, vc, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$t\,(s)$',fontsize=10)
plt.ylabel(r'$V\,(V)$',fontsize=10)
plt.title(r'Comportamento do Capacitor',fontsize=15)
plt.legend()

plt.savefig('capacitor2.png')
plt.show()


plt.figure()

plt.rcParams.update({'font.size': 10})

plt.yscale('log')

capacitor = lambda t,Vo,Tal: np.log10(Vo) -t/Tal*np.log10(np.e)
cmodel = lmfit.Model(capacitor)
params = cmodel.make_params(Vo=vo,Tal=tal)
result = cmodel.fit(np.log10(vc), params, t=t)
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

Tal = labfloat(coefs[1][1],coefs[1][3])

R = labfloat(224e3,1e3)

C = Tal / R

print("C = {0}".format(C))

xs = np.linspace(1.5,34,200)
ys = np.array([capacitor(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])

plt.plot(xs, 10**ys, '-',label=r'$V_o e^{\frac{-t}{RC}}$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(t, vc, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

eval("plt.figtext(.312,.145,r'$C = "+C.tex(2,0)+"\,F$',fontsize=10,ha='center')")

plt.xlabel(r'$t\,(s)$',fontsize=10)
plt.ylabel(r'$V\,(V)$',fontsize=10)
plt.title(r'Descarga do Capacitor',fontsize=15)
plt.legend()

plt.savefig('capacitorlog2.png')

plt.show()