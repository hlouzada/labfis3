import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('hallterminais')
calibracao = np.loadtxt('calibracao.txt')

calibracao = labfloat(*calibracao)

r = np.array([labfloat(k[0],k[1]) for k in dados])
vh = np.array([labfloat(k[2],k[3]) for k in dados])

print("r:", r)
print("Vh:", vh)

mo = 4*np.pi*1e-7

b = vh/calibracao

print("B:", b)



with open("tabelahall.txt", "w") as out:
    out.write("\t ".join(["r","Vh","B"])+"\n")
    for j in range(len(r)):
        out.write("\t ".join([str(r[j]),str(vh[j]),str(b[j])]) + "\n")


y = [float(y) for y in b]
x = [float(x) for x in r]

campo = lambda r,alpha: alpha/r
cmodel = lmfit.Model(campo)
params = cmodel.make_params(alpha=mo*1*30/(2*np.pi))
result = cmodel.fit(y, params, r=x)
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

xs = np.linspace(0,0.07,200)
ys = np.array([campo(xs[j],float(coefs[0][1])) for j in range(len(xs))])

plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$\frac{\mu_o IN}{2\pi}(\frac{1}{r})$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(r, b, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

plt.xlabel(r'$r\,(m)$',fontsize=10)
plt.ylabel(r'$B\,(T)$',fontsize=10)
plt.title(r'Campo Magnético de um Fio Retlíneio',fontsize=15)
plt.legend()

plt.savefig('campofioretlinio.png')
plt.show()


plt.figure()