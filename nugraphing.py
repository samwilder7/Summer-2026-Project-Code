import h5py
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#mpl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
mpl.rcParams.update({'font.size': 20})#,'family':'monospace'})
               
#mpl.rc('font',**{'family':'sans-serif','sans-serif':['fira']})  
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True

mpl.rcParams['pgf.texsystem'] = 'pdflatex'
mpl.rcParams.update({'pgf.rcfonts' : False})

mpl.rcParams['lines.linewidth'] = 3

mpl.rcParams['axes.linewidth'] = 3
mpl.rcParams['xtick.major.size'] = 9
mpl.rcParams['xtick.major.width'] = 3
mpl.rcParams['xtick.minor.size'] = 6
mpl.rcParams['xtick.minor.width'] = 2

mpl.rcParams['ytick.major.size'] = 9
mpl.rcParams['ytick.major.width'] = 3
mpl.rcParams['ytick.minor.size'] = 6
mpl.rcParams['ytick.minor.width'] = 2

mpl.rcParams['xtick.major.pad']='8'

colors = ["#430067", "#94216a", "#ff004d", "#ff8426", "#ffdd34", "#50e112", "#3fa66f", "#365987", "#000000", "#0033ff", "#29adff", "#00ffcc", "#c2c3c7", "#ab5236", "#5f574f"]
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=colors) 

def draw_grid(ax):
   ax.grid(which = "both")
   ax.minorticks_on()
   ax.grid(visible =True, which='minor', color='#999999', linestyle='-', alpha=0.2) 
   return
def draw_prelim(ax):
   ax.text(0.5, 0.5, 'Preliminary', transform=ax.transAxes, fontsize=60, color='gray', alpha=0.5, ha='center', va='center', rotation=30)
   return
#keep fig size ratio (10, 7) for each plot (1 sq)

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

fig, axs = plt.subplots(nrows = 4, ncols = 1, figsize = (10, 28), layout = "constrained")#make this a grid
for i in np.arange(180):
    axs[0].plot(time_pb, LN_L_e[:, 0, i], linestyle = "-")
    axs[0].plot(time_pb, LN_E_e[:, 0, i], linestyle = ":")
    axs[1].plot(time_pb, LN_L_e_b[:, 0, i], linestyle = "-")
    axs[1].plot(time_pb, LN_E_e_b[:, 0, i], linestyle = ":")
    axs[2].plot(time_pb, LN_L_x[:, 0, i], linestyle = "-")
    axs[2].plot(time_pb, LN_E_x[:, 0, i], linestyle = ":")
    axs[3].plot(time_pb, LN_L_x_b[:, 0, i], linestyle = "-")
    axs[3].plot(time_pb, LN_E_x_b[:, 0, i], linestyle = ":")
"""
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
"""
fig.supxlabel(r"$\mathrm{Time \ (s)}$", fontsize = 16)
axs[0].set_ylabel(r"$\mathrm{\frac{dL_{\nu_{e}}}{d\Omega} \ (erg \ s^{-1})}$")
plt.show()
#fig.savefig("nuplots.png")

#take data structures from one file and combine them with a second file (-400 to 200 ms)
#eulerian nu e priority
#data structuring, array indexing, appending
#put all stings in latex (different kinds of spacing)
#trapezoid rule and numerical integration
