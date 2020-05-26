import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('helmholtz')
calibracao = np.loadtxt('calibracao.txt')

calibracao = labfloat(*calibracao)

z = np.array([labfloat(k[0],k[1]) for k in dados])
vh = np.array([labfloat(k[2],k[3]) for k in dados])

print("z:", z)
print("Vh:", vh)

mo = 4*np.pi*1e-7

b = vh/calibracao

print("B:", b)

i = labfloat(1,1)
a = labfloat(0.14,0.01)
N = 130

with open("tabelahelmholtz.txt", "w") as out:
    out.write("\t ".join(["z","Vh","B"])+"\n")
    for j in range(len(z)):
        out.write("\t ".join([str(z[j]),str(vh[j]),str(b[j])]) + "\n")


y = [float(y) for y in b]
x = [float(x) for x in z]

campo = lambda z,a,m: ((m*a**2)/2)*(1/((z-a/2)**2+a**2)**(3/2)+1/((z+a/2)**2+a**2)**(3/2))
cmodel = lmfit.Model(campo)
params = cmodel.make_params(m=float(mo*i),a=a[0])
result = cmodel.fit(y, params, z=x)
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

print("B(z=0)",campo(0,labfloat(coefs[0][1],coefs[0][3]),labfloat(coefs[1][1],coefs[1][3])))
print(8/5**(3/2)*(mo*N*i/a))

xs = np.linspace(0,0.2,200)
ys = np.array([campo(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])

plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$\frac{\mu_o I a^2}{2}(\frac{1}{(((z-a)/2)^2+a^2)^{3/2}}-\frac{1}{(((z+a)/2)^2+a^2)^{3/2}})$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(z, b, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

plt.xlabel(r'$z\,(m)$',fontsize=10)
plt.ylabel(r'$B\,(T)$',fontsize=10)
plt.title(r'Campo Magnético de Helmholtz',fontsize=15)
plt.legend()

plt.savefig('helmholtz.png')
plt.show()


plt.figure()