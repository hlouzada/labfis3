import matplotlib.pyplot as plt
import numpy as np
import lmfit
from labfis import labfloat

vc, vi = np.loadtxt('fonte').T

print(vc)
print(vi)

cor = vi/4.7
rc = vc/cor
re = rc + 4.7
ptot = re*cor**2

print(cor)
print(rc)
print(re)
print(ptot)

with open("tabelafonte.txt", "w") as out:
    out.write("\t ".join(["Vc","Vi","I","Rc","Re","Ptot"])+"\n")
    for i in range(len(vc)):
        out.write("\t ".join([str(vc[i]),str(vi[i]),str(cor[i]),str(rc[i]),str(re[i]),str(ptot[i])]) + "\n")
"""
plt.figue()

plt.plot(r4, result.best_fit,'-',label=r'$(\frac{R_2}{R_1+R_2}-\frac{R_3}{R_3+R_4})\,V$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(r4, vg, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$R_4\,(\Omega)$',fontsize=10)
plt.ylabel(r'$V_G\,(V)$',fontsize=10)
plt.title(r'Ponte de Wheastone',fontsize=15)

plt.legend()

plt.savefig('ponte.png')
plt.show()


plt.figue()

plt.plot(r4, result.best_fit,'-',label=r'$(\frac{R_2}{R_1+R_2}-\frac{R_3}{R_3+R_4})\,V$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(r4, vg, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$R_4\,(\Omega)$',fontsize=10)
plt.ylabel(r'$V_G\,(V)$',fontsize=10)
plt.title(r'Ponte de Wheastone',fontsize=15)

plt.legend()

plt.savefig('ponte.png')
plt.show()


plt.figue()

plt.plot(r4, result.best_fit,'-',label=r'$(\frac{R_2}{R_1+R_2}-\frac{R_3}{R_3+R_4})\,V$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(r4, vg, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$R_4\,(\Omega)$',fontsize=10)
plt.ylabel(r'$V_G\,(V)$',fontsize=10)
plt.title(r'Ponte de Wheastone',fontsize=15)

plt.legend()

plt.savefig('ponte.png')
plt.show()


plt.figue()

plt.plot(r4, result.best_fit,'-',label=r'$(\frac{R_2}{R_1+R_2}-\frac{R_3}{R_3+R_4})\,V$',linewidth=1.8,color='#adadad',zorder=0)

plt.rcParams.update({'font.size': 10})

plt.scatter(r4, vg, label='Dados', color='#212121', s=25,zorder=5)

plt.xlabel(r'$R_4\,(\Omega)$',fontsize=10)
plt.ylabel(r'$V_G\,(V)$',fontsize=10)
plt.title(r'Ponte de Wheastone',fontsize=15)

plt.legend()

plt.savefig('ponte.png')
plt.show()
"""