import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from labfis import labfloat

vc, vi = np.loadtxt('fonte').T

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

ii = np.where(pext == pextm)[0]

ri = np.mean(re[ii])

print(ri)

pdissin = ri*cor**2

ptot = pdissin + pext

putil = rc*cor**2
efic = putil/ptot


plt.rcParams.update({'font.size': 10})

plt.scatter(re, ptot, label=r'$P_{total}$', marker='D', color='#212121')
plt.scatter(re, pdissin, label=r'$P_{diss_{int}}$', marker='o', color='#212121')
plt.scatter(re, putil, label=r'$P_{util}$', marker='^', color='#212121')
plt.scatter(re, pext, label=r'$P_{diss_{ext}}$', marker='+', color='#212121')

eval("plt.figtext(.665,.176,r'$max(P_{diss_{ext}}) ="+str(pextm)+"\, (\Omega\,A^2) \Rightarrow R_e = R_i = "+str(ri)+"\, \Omega$',fontsize=10,ha='center')")

plt.xlabel(r'$R_e\,(\Omega)$',fontsize=10)
plt.ylabel(r'$P\,\,(\Omega\,A^2)$',fontsize=10)
plt.title(r'Potência X Resistência Externa',fontsize=15)

plt.legend()

plt.savefig('fontepots.png')
plt.show()

plt.scatter(re, efic, label='Dados', color='#212121', linewidth=1.8)

plt.xlabel(r'$R_e\,(\Omega)$',fontsize=10)
plt.ylabel(r'$\frac{P_{util}}{P_{total}}$',fontsize=10)
plt.title(r'Eficiência de Trânsferencia de Potência',fontsize=15)

plt.legend()

plt.savefig('fonteeficiencia.png')
plt.show()