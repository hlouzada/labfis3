import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('parte2-dados')

V = np.array([labfloat(k[0],k[1]) for k in dados])
I = np.array([labfloat(k[2],k[3])*1e-3 for k in dados])

R = labfloat(48.5,0.1)

RL = labfloat(14,1)

print("R_L teorico:", RL)

N = 1000

L = 44

mu0 = 1.26e-6

x = [float(x) for x in I]
y = [float(y) for y in V]

relacao = lambda x,alpha,beta: alpha*x + beta
cmodel = lmfit.Model(relacao)
params = cmodel.make_params(alpha=float(R),beta=0)
result = cmodel.fit(y, params, x=x)
res = result.fit_report()

#print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

R_eq = labfloat(coefs[0][1],coefs[0][3])
print("R equivalente:", R_eq)

RL_exp = R_eq - R

print("R_L experimental:", RL_exp)
print("R_L eperimental == R_L teorico:", RL_exp == RL)

print("R_L eperimental != R_L teorico:", RL_exp != RL)
#%%
xs = np.linspace(0.005,0.08,200)
ys = np.array([relacao(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])


plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$I\,R + \beta$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(I, V, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

eval("plt.figtext(.707,.145,r'$R = "+R_eq.tex()+"\,\\Omega$',fontsize=10,ha='center')")


plt.ylabel(r'$V\,(\Omega A)$',fontsize=10)
plt.xlabel(r'$I\,(A)$',fontsize=10)
plt.title(r'Impedância Resistiva',fontsize=15)
plt.legend()

plt.savefig('parte2-grafico.png')
plt.show()


plt.figure()