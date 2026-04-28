import h5py
import numpy as np
import matplotlib.pyplot as plt

data = h5py.File("/home/swilder/test/D9.6-2D_Ray-By-Ray-Neutrino_000-500km.h5", "r")
#e
LN_E_e = data["Number Luminosity"]["Eulerian-Lab Frame"]["nu_e"][:]
LN_L_e = data["Number Luminosity"]["Lagrangian-Comoving Frame"]["nu_e"][:]
#ebar
LN_E_e_b = data["Number Luminosity"]["Eulerian-Lab Frame"]["nu_e_b"][:]
LN_L_e_b = data["Number Luminosity"]["Lagrangian-Comoving Frame"]["nu_e_b"][:]
#x
LN_E_x = data["Number Luminosity"]["Eulerian-Lab Frame"]["nu_x"][:]
LN_L_x = data["Number Luminosity"]["Lagrangian-Comoving Frame"]["nu_x"][:]
#xbar
LN_E_x_b = data["Number Luminosity"]["Eulerian-Lab Frame"]["nu_x_b"][:]
LN_L_x_b = data["Number Luminosity"]["Lagrangian-Comoving Frame"]["nu_x_b"][:]
time_pb = data["Time"]["Post Bounce Time"][:]

fig, axs = plt.subplots(nrows = 4, ncols = 2, figsize=(15, 30), layout = "constrained")#make this a grid
for i in np.arange(180):
    axs[0, 0].plot(time_pb, LN_L_e[:, 0, i], linestyle = "-")
    axs[0, 1].plot(time_pb, LN_E_e[:, 0, i], linestyle = "-")
    axs[1, 0].plot(time_pb, LN_L_e_b[:, 0, i], linestyle = "-")
    axs[1, 1].plot(time_pb, LN_E_e_b[:, 0, i], linestyle = "-")
    axs[2, 0].plot(time_pb, LN_L_x[:, 0, i], linestyle = "-")
    axs[2, 1].plot(time_pb, LN_E_x[:, 0, i], linestyle = "-")
    axs[3, 0].plot(time_pb, LN_L_x_b[:, 0, i], linestyle = "-")
    axs[3, 1].plot(time_pb, LN_E_x_b[:, 0, i], linestyle = "-")
for i in np.arange(4):
    axs[i, 0].grid(which = "both")
    axs[i, 0].minorticks_on()
    axs[i, 0].grid(visible =True, which='minor', color="#7B7B7B", linestyle='-', alpha=0.2)
    axs[i, 1].grid(which = "both")
    axs[i, 1].minorticks_on()
    axs[i, 1].grid(visible =True, which='minor', color="#7B7B7B", linestyle='-', alpha=0.2)
    if i == 0:
        axs[i, 0].set_title("nu_e", fontsize = "small", loc = "left")
        axs[i, 1].set_title("nu_e", fontsize = "small", loc = "left")
    elif i == 1:
        axs[i, 0].set_title("nu_e_b", fontsize = "small", loc = "left")
        axs[i, 1].set_title("nu_e_b", fontsize = "small", loc = "left")
    elif i == 2: 
        axs[i, 0].set_title("nu_x", fontsize = "small", loc = "left")
        axs[i, 1].set_title("nu_x", fontsize = "small", loc = "left")
    else: 
        axs[i, 0].set_title("nu_x_b", fontsize = "small", loc = "left")
        axs[i, 1].set_title("nu_x_b", fontsize = "small", loc = "left")
fig.supxlabel("Time (s)", fontsize = 16)
axs[0, 0].set_title("Lagrangian")
axs[0, 1].set_title("Eulerian")
plt.show()
fig.savefig("nuplots.png")
