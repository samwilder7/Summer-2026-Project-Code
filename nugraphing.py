import h5py
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

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


data_000 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_000-500km.h5", "r")
data_005 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_005-500km.h5", "r")
data_010 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_010-500km.h5", "r")
data_015 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_015-500km.h5", "r")
data_020 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_020-500km.h5", "r")
data_025 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_025-500km.h5", "r")
data_030 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_030-500km.h5", "r")
data_035 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_035-500km.h5", "r")

SN_E_e = []
SN_E_e_bar = []
SN_E_x = []
SN_E_x_bar = []
time = []
energy_bins = []

#time
time_000 = data_000["Time"]["Post Bounce Time"][:]
time_005 = data_005["Time"]["Post Bounce Time"][:] 
time_010 = data_010["Time"]["Post Bounce Time"][:]
time_015 = data_015["Time"]["Post Bounce Time"][:] 
time_020 = data_020["Time"]["Post Bounce Time"][:]
time_025 = data_025["Time"]["Post Bounce Time"][:]
time_030 = data_030["Time"]["Post Bounce Time"][:]
time_035 = data_035["Time"]["Post Bounce Time"][:]
time = np.append(time_000, time_005, axis = 0)
time = np.append(time, time_010, axis = 0)
time = np.append(time, time_015, axis = 0)
time = np.append(time, time_020, axis = 0)
time = np.append(time, time_025, axis = 0)
time = np.append(time, time_030, axis = 0)
#time = np.append(time, time_035, axis = 0)

#energy bins
energy_bins = data_000["Energy Bins"]["Center"][:]

#eulerian nu e
SN_E_e_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e = np.append(SN_E_e_000, SN_E_e_005, axis=0)
SN_E_e = np.append(SN_E_e, SN_E_e_010, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_015, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_020, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_025, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_030, axis = 0)
#SN_E_e = np.append(SN_E_e, SN_E_e_035, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar = np.append(SN_E_e_000, SN_E_e_bar_005, axis=0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_010, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_015, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_020, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_025, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_030, axis = 0)
#SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_035, axis = 0)

#eulerian nu x
SN_E_x_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x = np.append(SN_E_x_000, SN_E_x_005, axis=0)
SN_E_x = np.append(SN_E_x, SN_E_x_010, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_015, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_020, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_025, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_030, axis = 0)
#SN_E_x = np.append(SN_E_x, SN_E_x_035, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar = np.append(SN_E_e_000, SN_E_x_bar_005, axis=0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_010, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_015, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_020, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_025, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_030, axis = 0)
#SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_035, axis = 0)



fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize = (10, 7), layout = "constrained", sharey = True, sharex = True)
fig.supxlabel(r"$\mathrm{Energy \ MeV}$")
fig.supylabel(r"$\mathrm{Number \ Luminosity \ Spectrum \ \frac{d^2L_n}{dEd\omega} (s^{-1}MeV^{-1}str^{-1}})$", fontsize = 14)


#usingfuncanimate
def func(frames):
    axs[0, 0].clear()
    axs[0, 1].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()
    axs[0, 0].set_title(r"$\mathrm{\nu_e}$")
    axs[0, 1].set_title(r"$\mathrm{\bar{\nu}_e}$")
    axs[1, 0].set_title(r"$\mathrm{\nu_{\mu + \tau}}$")
    axs[1, 1].set_title(r"$\mathrm{\bar{\nu}}_{\mu + \tau}$")
    axs[0, 0].set_ylim(top = 2.5e56, auto = False)
    axs[0, 1].set_ylim(top = 2.5e56, auto = False)
    axs[1, 0].set_ylim(top = 2.5e56, auto = False)
    axs[1, 1].set_ylim(top = 2.5e56, auto = False)
    axs[0, 0].semilogx(energy_bins, SN_E_e[frames, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar[frames, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x[frames, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar[frames, 0, 90], color = "Black", animated = True)
    axs[1, 1].set_xlabel(f"Time = {round(time[frames], 3)*1000}ms", loc = "right")
    
movie = animation.FuncAnimation(fig, func, interval = 50, blit = False, frames = len(time))
movie.save("movietest_030.gif")
plt.show()
#020: 1070 seconds
#020 w energy bin x axis: 898 seconds
#020 w log x axis: 1828 seconds, 2060 seconds 6/5
#up to 030: kernel died after 2667 seconds >:(
#up to 025: 2514 secondsimport h5py
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

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


data_000 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_000-500km.h5", "r")
data_005 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_005-500km.h5", "r")
data_010 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_010-500km.h5", "r")
data_015 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_015-500km.h5", "r")
data_020 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_020-500km.h5", "r")
data_025 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_025-500km.h5", "r")
data_030 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_030-500km.h5", "r")
data_035 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/D9.6-2D/D9.6-2D-500km-Public/Ray-By-Ray/D9.6-2D_Ray-By-Ray-Neutrino_035-500km.h5", "r")

SN_E_e = []
SN_E_e_bar = []
SN_E_x = []
SN_E_x_bar = []
time = []
energy_bins = []

#time
time_000 = data_000["Time"]["Post Bounce Time"][:]
time_005 = data_005["Time"]["Post Bounce Time"][:] 
time_010 = data_010["Time"]["Post Bounce Time"][:]
time_015 = data_015["Time"]["Post Bounce Time"][:] 
time_020 = data_020["Time"]["Post Bounce Time"][:]
time_025 = data_025["Time"]["Post Bounce Time"][:]
time_030 = data_030["Time"]["Post Bounce Time"][:]
time_035 = data_035["Time"]["Post Bounce Time"][:]
time = np.append(time_000, time_005, axis = 0)
time = np.append(time, time_010, axis = 0)
time = np.append(time, time_015, axis = 0)
time = np.append(time, time_020, axis = 0)
time = np.append(time, time_025, axis = 0)
time = np.append(time, time_030, axis = 0)
#time = np.append(time, time_035, axis = 0)

#energy bins
energy_bins = data_000["Energy Bins"]["Center"][:]

#eulerian nu e
SN_E_e_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e = np.append(SN_E_e_000, SN_E_e_005, axis=0)
SN_E_e = np.append(SN_E_e, SN_E_e_010, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_015, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_020, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_025, axis = 0)
SN_E_e = np.append(SN_E_e, SN_E_e_030, axis = 0)
#SN_E_e = np.append(SN_E_e, SN_E_e_035, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar = np.append(SN_E_e_000, SN_E_e_bar_005, axis=0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_010, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_015, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_020, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_025, axis = 0)
SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_030, axis = 0)
#SN_E_e_bar = np.append(SN_E_e_bar, SN_E_e_bar_035, axis = 0)

#eulerian nu x
SN_E_x_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x = np.append(SN_E_x_000, SN_E_x_005, axis=0)
SN_E_x = np.append(SN_E_x, SN_E_x_010, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_015, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_020, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_025, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_030, axis = 0)
#SN_E_x = np.append(SN_E_x, SN_E_x_035, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar = np.append(SN_E_e_000, SN_E_x_bar_005, axis=0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_010, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_015, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_020, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_025, axis = 0)
SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_030, axis = 0)
#SN_E_x_bar = np.append(SN_E_e_bar, SN_E_x_bar_035, axis = 0)



fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize = (10, 7), layout = "constrained", sharey = True, sharex = True)
fig.supxlabel(r"$\mathrm{Energy \ MeV}$")
fig.supylabel(r"$\mathrm{Number \ Luminosity \ Spectrum \ \frac{d^2L_n}{dEd\omega} (s^{-1}MeV^{-1}str^{-1}})$", fontsize = 14)


#usingfuncanimate
def func(frames):
    axs[0, 0].clear()
    axs[0, 1].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()
    axs[0, 0].set_title(r"$\mathrm{\nu_e}$")
    axs[0, 1].set_title(r"$\mathrm{\bar{\nu}_e}$")
    axs[1, 0].set_title(r"$\mathrm{\nu_{\mu + \tau}}$")
    axs[1, 1].set_title(r"$\mathrm{\bar{\nu}}_{\mu + \tau}$")
    axs[0, 0].set_ylim(top = 2.5e56, auto = False)
    axs[0, 1].set_ylim(top = 2.5e56, auto = False)
    axs[1, 0].set_ylim(top = 2.5e56, auto = False)
    axs[1, 1].set_ylim(top = 2.5e56, auto = False)
    axs[0, 0].semilogx(energy_bins, SN_E_e[frames, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar[frames, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x[frames, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar[frames, 0, 90], color = "Black", animated = True)
    axs[1, 1].set_xlabel(f"Time = {round(time[frames], 3)*1000}ms", loc = "right")
    
movie = animation.FuncAnimation(fig, func, interval = 50, blit = False, frames = len(time))
movie.save("movietest_030.gif")
plt.show()
#020: 1070 seconds
#020 w energy bin x axis: 898 seconds
#020 w log x axis: 1828 seconds, 2060 seconds 6/5
#up to 030: kernel died after 2667 seconds 
#up to 025: 2514 seconds
#testinggittestinggittestinggit
#comment
