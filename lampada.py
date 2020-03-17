import matplotlib.pyplot as plt
import numpy as np
import lmfit

v, i = np.loadtxt('lampada').T


plt.scatter(i,v, label='Dados', color='#212121', s=25,zorder=5)

plt.ylabel(r'Tensão (V)',fontsize=10)
plt.xlabel(r'Corrente (mA)',fontsize=10)
plt.title(r'Lampada Incandescente',fontsize=15)

plt.legend()

plt.savefig('Lampada_default.pdf')
plt.show()


i[18:] *= 0.8754321

print(v)
print(i)

lampOhm = lambda i,Ro,a,To,k: i*Ro*((1-a*To)/1-Ro*a*k*i**2)

lmodel = lmfit.Model(lampOhm)

params = lmodel.make_params(Ro=0.05384615385,To=299.15,a=0.00001,k=100)

result = lmodel.fit(v, params, i=i)

print(result.fit_report())

plt.figure()

plt.plot(i,result.best_fit,'-',label=r'$i_oR_o\frac{1-\alpha T_o}{1-R_o\alpha ki^2}$',linewidth=1.8,color='#adadad',zorder=0)

plt.scatter(i,v, label='Dados', color='#212121', s=25,zorder=5)

plt.ylabel(r'Tensão (V)',fontsize=10)
plt.xlabel(r'Corrente (mA)',fontsize=10)
plt.title(r'Lampada Incandescente',fontsize=15)
#plt.figtext(.5,.930,'Resistor 1', fontsize=18, ha='center')



#plt.figtext(.30,.266,r"$a = 6.4\cdot 10^{-06} \pm 0.4\cdot 10^{-06}$",fontsize=10,ha='center')
#plt.figtext(.30,.223,r"$b = 21.12 \pm 0.07$",fontsize=10,ha='center')
plt.legend()

plt.savefig('Lampada.pdf')
plt.show()

r = v/i

flampOhm = lambda i,To,k: To/(k*i**2)

flmodel = lmfit.Model(lampOhm)

fparams = lmodel.make_params(To=299.15,a=0.00004,k=459)

fresult = lmodel.fit(r, params, i=i)

print(result.fit_report())

plt.figure()

plt.scatter(i,r, label='Dados', color='#212121', s=25,zorder=5)

plt.plot(i,fresult.best_fit,'-',label=r'$\frac{T_o}{Ki^2}$',linewidth=1.8,color='#adadad',zorder=0)


plt.ylabel(r'Rresistência (k\Ohm)',fontsize=10)
plt.xlabel(r'Corrente (mA)',fontsize=10)
plt.title('Lampada Incandescente',fontsize=15)

plt.legend()
plt.savefig('lampada2.pdf')
plt.show()