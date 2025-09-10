import numpy as np
import matplotlib.pyplot as plt


def deriv(h, pos):
    cos_FD = (np.cos(pos + h)-np.cos(pos))/h
    cos_CD = (np.cos(pos + h/2)-np.cos(pos - h/2))/h
    cos_ED = (8*(np.cos(pos+h/4) - np.cos(pos-h/4)) - (np.cos(pos+h/2) - np.cos(pos-h/2)))/3/h

    exp_FD = (np.exp(pos + h)-np.exp(pos))/h
    exp_CD = (np.exp(pos + h/2)-np.exp(pos - h/2))/h
    exp_ED = (8*(np.exp(pos+h/4) - np.exp(pos-h/4)) - (np.exp(pos+h/2) - np.exp(pos-h/2)))/3/h

    return (cos_FD, cos_CD, cos_ED, exp_FD, exp_CD, exp_ED)

def rel_error(cal, real):
    return np.abs((cal-real)/real)

positions = np.array([0.1, 1, 100])

cos = -np.sin(positions)
exp = np.exp(positions)

h = np.logspace(-16, 1)

fig0, axs0 = plt.subplots(3, 2)

for i in range(3):

    cosF, cosC, cosE, expF, expC, expE = deriv(h, positions[i])

    axs0[i,0].semilogx(h, cosF, label='Cos Forward')
    axs0[i,0].semilogx(h, cosC, label='Cos Center')
    axs0[i,0].semilogx(h, cosE, label='Cos Extrap')
    axs0[i,0].set_xlabel('h value')
    axs0[i,0].set_ylabel(f'Derivatives at x={positions[i]}')
    axs0[0,0].set_title(f'Derivative')
    axs0[i,0].legend()
    
    axs0[i,1].loglog(h, rel_error(cosF, cos[i]), label='Error Forward')
    axs0[i,1].loglog(h, rel_error(cosC, cos[i]), label='Error Center')
    axs0[i,1].loglog(h, rel_error(cosE, cos[i]), label='Error Extrap')
    axs0[i,1].set_xlabel('h value')
    axs0[0,1].set_title(f'Relative Error')
    axs0[i,1].legend()

fig0.suptitle("Cosine")

plt.savefig("cos.png")

fig1, axs1 = plt.subplots(3, 2)

for i in range(3):

    cosF, cosC, cosE, expF, expC, expE = deriv(h, positions[i])

    axs1[i,0].loglog(h, expF, label='Exp Forward')
    axs1[i,0].loglog(h, expC, label='Exp Center')
    axs1[i,0].loglog(h, expE, label='Exp Extrap')
    axs1[i,0].set_xlabel('h value')
    axs1[i,0].set_ylabel(f'Derivatives at x={positions[i]}')
    axs1[0,0].set_title(f'Derivative')
    axs1[i,0].legend()

    axs1[i,1].loglog(h, rel_error(expF, exp[i]), label='Error Forward')
    axs1[i,1].loglog(h, rel_error(expC, exp[i]), label='Error Center')
    axs1[i,1].loglog(h, rel_error(expE, exp[i]), label='Error Extrap')
    axs1[i,1].set_xlabel('h value')
    axs1[0,1].set_title(f'Relative Error')
    axs1[i,1].legend()


fig1.suptitle("Exponential")

plt.savefig("exp.png")





