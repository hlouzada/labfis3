import matplotlib.pyplot as plt
import numpy as np
from labfis import labfloat
import lmfit

dados = np.loadtxt('parte3-dados')

N1 = np.array([labfloat(k[0],k[1]) for k in dados])
V1 = np.array([labfloat(k[2],k[3]) for k in dados])
N2 = np.array([labfloat(k[4],k[5]) for k in dados])
V2 = np.array([labfloat(k[6],k[7]) for k in dados])


N2N1 = N2/N1
V2V1 = V2/V1


with open("parte3-tabela.txt", "w") as out:
    out.write("\t ".join(["N1","V1","N2","V2","N2/N1","V2/V1"])+"\n")
    for j in range(len(N1)):
        out.write("\t ".join([str(N1[j]),str(V1[j]),str(N2[j]),str(V2[j]),str(N2N1[j]),str(V2V1[j])]) + "\n")


x = [float(x) for x in N2N1]
y = [float(y) for y in V2V1]

relacao = lambda x,alpha,beta: alpha*x + beta
cmodel = lmfit.Model(relacao)
params = cmodel.make_params(alpha=1,beta=0)
result = cmodel.fit(y, params, x=x)
res = result.fit_report()

print(res)

coefs = res[res.find("[[Variables]]")+13:res.find("[[Correlations]]")].split("\n")[1:3]
coefs = [coef.split() for coef in coefs]

alpha = labfloat(coefs[0][1], coefs[0][3])
beta = labfloat(coefs[1][1], coefs[1][3])

print("alpha:", alpha)
print("beta:", beta)
#%%
xs = np.linspace(0,4.25,200)
ys = np.array([relacao(xs[j],float(coefs[0][1]),float(coefs[1][1])) for j in range(len(xs))])


plt.figure()

plt.rcParams.update({'font.size': 10})

plt.plot(xs, ys,'-',label=r'$\alpha x + \beta$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(N2N1, V2V1, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

eval("plt.figtext(.707,.195,r'$\\alpha = "+alpha.tex()+"$',fontsize=10,ha='center')")
eval("plt.figtext(.707,.145,r'$\\beta = "+beta.tex()+"$',fontsize=10,ha='center')")

plt.ylabel(r'$V_2/V_1$',fontsize=10)
plt.xlabel(r'$N_2/N_1$',fontsize=10)
plt.title(r'Relação Entre as Bobinas',fontsize=15)
plt.legend()

plt.savefig('parte3-grafico.png')
plt.show()


plt.figure()