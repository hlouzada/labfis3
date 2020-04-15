import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from labfis import labfloat

vc,vce,vi,vie = np.loadtxt('fonte').T

vc = np.array([labfloat(vc[j],vce[j]) for j in range(len(vc))])

vi = np.array([labfloat(vi[j],vie[j]) for j in range(len(vi))])

print(vc)
print(vi)

cor = vi/4.7
rc = vc/cor
re = rc + 4.7
pext = re*cor**2

print(cor)
print(rc)
print(re)
print(pext)

with open("tabelafonte.txt", "w") as out:
    out.write("\t ".join(["Vc","Vi","I","Rc","Re","Pe"])+"\n")
    for i in range(len(vc)):
        out.write("\t ".join([str(vc[i]),str(vi[i]),str(cor[i]),str(rc[i]),str(re[i]),str(pext[i])]) + "\n")

maxs, _ = find_peaks(pext)

pextm = max([pext[j]for j in maxs])

print(pextm)

ii = np.where(np.array([val.mean for val in pext]) == pextm.mean)[0]

print(ii)

ri = re[ii].tolist()

print(ri)

pdissin = ri*cor**2

ptot = pdissin + pext

putil = rc*cor**2
efic = putil/ptot

print(pdissin)
print(ptot)
print(putil)
print(efic)

plt.rcParams.update({'font.size': 10})

plt.scatter(re, ptot, label=r'$P_{total}$', marker='D', color='#212121')
plt.scatter(re, pdissin, label=r'$P_{diss_{int}}$', marker='o', color='#212121')
plt.scatter(re, putil, label=r'$P_{util}$', marker='^', color='#212121')
plt.scatter(re, pext, label=r'$P_{diss_{ext}}$', marker='+', color='#212121')

eval("plt.figtext(.495,.838,r'$max(P_{diss_{ext}}) ="+pextm.tex(2,0)+"\, \Omega\,A^2$',fontsize=10,ha='center')")
eval("plt.figtext(.495,.800,r'$\Rightarrow R_e = R_i = "+ri[0].tex()+"\, \Omega$',fontsize=10,ha='center')")

plt.xlabel(r'$R_e\,(\Omega)$',fontsize=10)
plt.ylabel(r'$P\,\,(\Omega\,A^2)$',fontsize=10)
plt.title(r'Potência X Resistência Externa',fontsize=15)

plt.legend()

plt.savefig('fontepots.png')
plt.show()

plt.scatter(re, efic, label='Dados', color='#212121', linewidth=1.8)

plt.xlabel(r'$R_e\,(\Omega)$',fontsize=10)
plt.ylabel(r'$P_{util}\,\,/\,\,P_{total}$',fontsize=10)
plt.title(r'Eficiência de Trânsferencia de Potência',fontsize=15)

plt.legend()

plt.savefig('fonteeficiencia.png')
plt.show()