import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('hall')

v = np.array([labfloat(k[0],k[1]) for k in dados])
i =np.array([labfloat(k[2],k[3]) for k in dados])

print("V:", v)
print("I:", i)

mo = 4*np.pi*1e-7
n = 760/labfloat(0.148,0.001)

print("n:",n)

vh = v - labfloat(9.4e-3,0.1e-3)
b = mo*i*n

print("Vh:", vh)
print("B:", b)


with open("tabelahall.txt", "w") as out:
    out.write("\t ".join(["I","V","Vh","B"])+"\n")
    for j in range(len(i)):
        out.write("\t ".join([str(i[j]),str(v[j]),str(vh[j]),str(b[j])]) + "\n")

y = [float(y) for y in vh]
x = [float(x) for x in b]

campo = lambda x,alpha,beta: alpha*x - beta
cmodel = lmfit.Model(campo)
params = cmodel.make_params(alpha=np.mean(v)[0]/(mo*n[0]*np.mean(i)[0]),beta=9.4e-3)
result = cmodel.fit(y, params, x=x)
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

xs = np.linspace(0,0.01,200)
ys = np.array([campo(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])

calibracao = labfloat(coefs[0][1],coefs[0][3])

with open("calibracao.txt", "w") as out:
    out.write(str(calibracao[0]) + "\t " + str(calibracao[1]))

print("Calibração da sonda de Hall = {0}".format(calibracao))

plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$\alpha x - \beta$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(b, vh, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

eval("plt.figtext(.707,.145,r'$\\alpha = "+calibracao.tex()+"\,VT^{-1}$',fontsize=10,ha='center')")


plt.ylabel(r'$V_{Hall}\,(V)$',fontsize=10)
plt.xlabel(r'$B\,(T)$',fontsize=10)
plt.title(r'Sonda de Hall',fontsize=15)
plt.legend()

plt.savefig('hall.png')
plt.show()


plt.figure()