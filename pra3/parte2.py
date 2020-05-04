import numpy as np
from labfis import labfloat
import matplotlib.pyplot as plt

vo = labfloat(9,1)

c1 = labfloat(913e-6,1e-6)
c2 = labfloat(1958e-6,1e-6)

vi = labfloat(9,1)
vf = labfloat(2.88,0.01)

qi = lambda c1,vi: c1*vi
qf = lambda c1,c2,vf: (c1+c2)*vf
ui = lambda c1,vi: 1/2*c1*vi**2
uf = lambda c1,c2,vf: 1/2*(c1+c2)*vf**2

res = [qi(c1,vi),qf(c1,c2,vf),ui(c1,vi),uf(c1,c2,vf)]

print("Carga e Energia Armazenada Antes do Contato:")
print("Qi = {0}\nUi = {2}".format(*res))
print()
print("Carga e Energia Armazenada Depois do Contato:")
print("Qf = {1}\nUf = {3}".format(*res))

dados = np.loadtxt('associacao')

c1 = np.array([labfloat(k[0],k[1]) for k in dados])
c2 = np.array([labfloat(k[2],k[3]) for k in dados])

vi = np.array([labfloat(k[4],k[5]) for k in dados])
vf = np.array([labfloat(k[6],k[7]) for k in dados])

#print(c1,c2,vi,vf,sep='\n')

Qi = qi(c1,vi)
Qf = qf(c1,c2,vf)
Ui = ui(c1,vi)
Uf = uf(c1,c2,vf)

with open("tabelacapacitor.txt", "w") as out:
    out.write("\t ".join(["Qi","Ui","Qf","Uf"])+"\n")
    for i in range(len(Qi)):
        out.write("\t ".join([str(Qi[i]),str(Ui[i]),str(Qf[i]),str(Uf[i])]) + "\n")

print()

print("Carga e Energia Armazenada Antes do Contato:")
print("Qi: {0}".format(Qi),"Ui: {0}".format(Ui),sep='\n')
print()
print("Carga e Energia Armazenada Depois do Contato:")
print("Qf: {0}".format(Qf),"Uf: {0}".format(Uf),sep='\n')

uiuf = Ui/Uf
c2c1 = c2/c1

plt.figure()

plt.rcParams.update({'font.size': 10})

#plt.plot(xs, 10**ys, '-',label=r'$V_o(1-e^{\frac{-t}{RC}})$',linewidth=1.8,color='#adadad',zorder=0)
plt.plot(c2c1, uiuf, 'o', label='Dados', color='#212121', markersize=5, zorder=5)

#eval("plt.figtext(.312,.145,r'$C = "+C.tex(2,0)+"\,F$',fontsize=10,ha='center')")

plt.xlabel(r'$C_1\,/\,C_2$',fontsize=10)
plt.ylabel(r'$U_1\,/\,U_2$',fontsize=10)
plt.title(r'Conservação do Capacitor',fontsize=15)
plt.legend()

plt.savefig('energiafacao.png')

plt.show()