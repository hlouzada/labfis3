import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('carga')

vc = np.array([k[0] for k in dados])
t = np.array([k[2] for k in dados])

print(vc)
print(t)

vo = 2.2

logvomvc = vo - vc

print(logvomvc)

capacitor = lambda t,Vo,Tal: Vo*(1-np.exp(-t/Tal))
cmodel = lmfit.Model(capacitor)
params = cmodel.make_params(Vo=vo,Tal=106e-6*97e3)
result = cmodel.fit(vc, params, t=t)
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

xs = np.linspace(1.5,34,200)
ys = np.array([capacitor(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])


plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$V_o(1-e^{\frac{-t}{\tau}})$',linewidth=1.8,color='#adadad',zorder=0)
plt.scatter(t, vc, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$t\,(s)$',fontsize=10)
plt.ylabel(r'$V_c\,(V)$',fontsize=10)
plt.title(r'Comportamento do Capacitor',fontsize=15)
plt.legend()

plt.savefig('capacitor.png')
plt.show()


capacitor = lambda t,b,a: -a*t + b
cmodel = lmfit.Model(capacitor)
params = cmodel.make_params(b=-np.log10(vo),a=1/(100e-6*97e3))
result = cmodel.fit(np.log10(vo - vc)[0:-2], params, t=t[0:-2])
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

#print(coefs)

Tal = 1/labfloat(coefs[1][1],coefs[1][3])

R = labfloat(97e3,1e3)

C = Tal / R

print("C = {0}".format(C))

xsl = np.linspace(t[0],t[-1],200)
ysl = np.array([capacitor(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])


plt.figure()

plt.rcParams.update({'font.size': 10})

plt.yscale('log')

plt.plot(xsl, 10**ysl,'-',label=r'$V_o(1-e^{\frac{-t}{RC}})$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(t, logvomvc, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

eval("plt.figtext(.312,.145,r'$C = "+C.tex(2,0)+"\,F$',fontsize=10,ha='center')")

plt.xlabel(r'$t\,(s)$',fontsize=10)
plt.ylabel(r'$log(V_o - V_c)\,(V)$',fontsize=10)
plt.title(r'Descarga do Capacitor',fontsize=15)
plt.legend()

plt.savefig('capacitorlog.png')

plt.show()