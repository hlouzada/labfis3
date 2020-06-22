import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('parte1-dados')

f = np.array([labfloat(k[0],k[1]) for k in dados])
epsilon = np.array([labfloat(k[2],k[3]) for k in dados])
Vr = np.array([labfloat(k[4],k[5]) for k in dados])

R = labfloat(10,1)

N1 = 760
l1 = labfloat(15e-2, 1e-2)
r1 = labfloat(2.25e-2, 0.01e-2)
n1 = N1/l1

N2 = 2100
l2 = labfloat(6e-2,1e-2)
r2 = labfloat(0.75e-2,0.01e-2)
n2 = N2/l2

mu0 = 1.26e-6

I = Vr/R
omega = 2*np.pi*f
omegaI = omega*I

for name in ["f","epsilon","Vr","I","omega","omegaI"]:
    print(name+":", eval(name))


with open("parte1-tabela.txt", "w") as out:
    out.write("\t ".join(["f","epsilon","Vr","I","omega","omega*I"])+"\n")
    for j in range(len(f)):
        out.write("\t ".join([str(f[j]),str(epsilon[j]),str(Vr[j]),str(I[j]),str(omega[j]),str(omegaI[j])]) + "\n")


L12_teo = mu0*n1*n2*l2*(np.pi*r2**2)

print("L12 teorico:", L12_teo)

x = [float(x) for x in omegaI]
y = [float(y) for y in epsilon]

relacao = lambda x,alpha,beta: alpha*x + beta
cmodel = lmfit.Model(relacao)
params = cmodel.make_params(alpha=float(L12_teo),beta=0)
result = cmodel.fit(y, params, x=x)
res = result.fit_report()

#print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

L12_exp = labfloat(coefs[0][1],coefs[0][3])
print("L12 experimental:", L12_exp)

print("L12 eperimental == L12 teorico:", L12_exp == L12_teo)
#%%
xs = np.linspace(50,1050,2000)
ys = np.array([relacao(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])


plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$L\omega I + \beta$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(omegaI, epsilon, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

eval("plt.figtext(.707,.145,r'$L = "+L12_exp.tex()+"\,mH$',fontsize=10,ha='center')")


plt.ylabel(r'$\epsilon\,(V)$',fontsize=10)
plt.xlabel(r'$\omega I\,(AS^{-1})$',fontsize=10)
plt.title(r'Tensão Induzida',fontsize=15)
plt.legend()

plt.savefig('parte1-grafico.png')
plt.show()


plt.figure()