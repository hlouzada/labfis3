import matplotlib.pyplot as plt
import numpy as np
import lmfit
from labfis import labfloat

vpot, vr = np.loadtxt('fonte').T

print(vpot)
print(vr)

cor = vr/4.7
rc = vpot/cor
re = rc + 4.7
p = re*cor**2

print(cor)
print(rc)
print(re)
print(p)

with open("tabelafonte.txt", "w") as out:
    out.write("\t ".join(["V_pot","V_r","I","Rc","Re","P"])+"\n")
    for i in range(len(vpot)):
        out.write("\t ".join([str(vpot[i]),str(vr[i]),str(cor[i]),str(rc[i]),str(re[i]),str(p[i])]) + "\n")
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