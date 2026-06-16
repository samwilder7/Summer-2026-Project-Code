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


#with equations of state
#using pictures 
data_000_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")
data_005_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")
data_010_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")
data_015_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")
data_020_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")
data_025_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")
data_030_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")
data_035_DD2 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-DD2", "r")

data_000_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")
data_005_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")
data_010_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")
data_015_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")
data_020_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")
data_025_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")
data_030_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")
data_035_FSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-FSUGold", "r")

data_000_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")
data_005_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")
data_010_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")
data_015_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")
data_020_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")
data_025_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")
data_030_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")
data_035_IUFSU = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-IUFSU", "r")

data_000_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")
data_005_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")
data_010_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")
data_015_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")
data_020_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")
data_025_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")
data_030_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")
data_035_LSBCK = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-LSBCK", "r")

data_000_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")
data_005_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")
data_010_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")
data_015_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")
data_020_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")
data_025_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")
data_030_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")
data_035_NL3 = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-NL3", "r")

data_000_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")
data_005_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")
data_010_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")
data_015_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")
data_020_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")
data_025_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")
data_030_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")
data_035_SFHo = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHo", "r")

data_000_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")
data_005_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")
data_010_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")
data_015_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")
data_020_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")
data_025_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")
data_030_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")
data_035_SFHx = h5py.File("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/E15-SFHx", "r")

SN_E_e_DD2 = []
SN_E_e_bar_DD2 = []
SN_E_x_DD2 = []
SN_E_x_bar_DD2 = []

SN_E_e_FSU = []
SN_E_e_bar_FSU = []
SN_E_x_FSU = []
SN_E_x_bar_FSU = []

SN_E_e_IUFSU = []
SN_E_e_bar_IUFSU = []
SN_E_x_IUFSU = []
SN_E_x_bar_IUFSU = []

SN_E_e_LSBCK = []
SN_E_e_bar_LSBCK = []
SN_E_x_LSBCK = []
SN_E_x_bar_LSBCK = []

SN_E_e_NL3 = []
SN_E_e_bar_NL3 = []
SN_E_x_NL3 = []
SN_E_x_bar_NL3 = []

SN_E_e_SFHo = []
SN_E_e_bar_SFHo = []
SN_E_x_SFHo = []
SN_E_x_bar_SFHo = []

SN_E_e_SFHx = []
SN_E_e_bar_SFHx = []
SN_E_x_SFHx = []
SN_E_x_bar_SFHx = []

time = []
energy_bins = []

#time
time_000 = data_000_DD2["Time"]["Post Bounce Time"][:]
time_005 = data_005_DD2["Time"]["Post Bounce Time"][:] 
time_010 = data_010_DD2["Time"]["Post Bounce Time"][:]
time_015 = data_015_DD2["Time"]["Post Bounce Time"][:] 
#time_020 = data_020_DD2["Time"]["Post Bounce Time"][:]
#time_025 = data_025_DD2["Time"]["Post Bounce Time"][:]
#time_030 = data_030_DD2["Time"]["Post Bounce Time"][:]
#time_035 = data_035_DD2["Time"]["Post Bounce Time"][:]
time = np.append(time_000, time_005, axis = 0)
time = np.append(time, time_010, axis = 0)
time = np.append(time, time_015, axis = 0)
#time = np.append(time, time_020, axis = 0)
#time = np.append(time, time_025, axis = 0)
#time = np.append(time, time_030, axis = 0)
#time = np.append(time, time_035, axis = 0)

#energy bins
energy_bins = data_000_DD2["Energy Bins"]["Center"][:]

#DD2
#eulerian nu e
SN_E_e_000_DD2 = data_000_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005_DD2 = data_005_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010_DD2 = data_010_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015_DD2 = data_015_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_020_DD2 = data_020_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_025_DD2 = data_025_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_030_DD2 = data_030_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_035_DD2 = data_035_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_DD2 = np.append(SN_E_e_000_DD2, SN_E_e_005_DD2, axis=0)
SN_E_e_DD2 = np.append(SN_E_e_DD2, SN_E_e_010_DD2, axis = 0)
SN_E_e_DD2 = np.append(SN_E_e_DD2, SN_E_e_015_DD2, axis = 0)
#SN_E_e_DD2 = np.append(SN_E_e_DD2, SN_E_e_020_DD2, axis = 0)
#SN_E_e_DD2 = np.append(SN_E_e_DD2, SN_E_e_025_DD2, axis = 0)
#SN_E_e_DD2 = np.append(SN_E_e_DD2, SN_E_e_030_DD2, axis = 0)
#SN_E_e_DD2 = np.append(SN_E_e_DD2, SN_E_e_035_DD2, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000_DD2 = data_000_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005_DD2 = data_005_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010_DD2 = data_010_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015_DD2 = data_015_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_020_DD2 = data_020_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_025_DD2 = data_025_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_030_DD2 = data_030_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_035_DD2 = data_035_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_DD2 = np.append(SN_E_e_000_DD2, SN_E_e_bar_005_DD2, axis=0)
SN_E_e_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_e_bar_010_DD2, axis = 0)
SN_E_e_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_e_bar_015_DD2, axis = 0)
#SN_E_e_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_e_bar_020_DD2, axis = 0)
#SN_E_e_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_e_bar_025_DD2, axis = 0)
#SN_E_e_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_e_bar_030_DD2, axis = 0)
#SN_E_e_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_e_bar_035_DD2, axis = 0)

#eulerian nu x
SN_E_x_000_DD2 = data_000_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005_DD2 = data_005_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010_DD2 = data_010_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015_DD2 = data_015_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_020_DD2 = data_020_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_025_DD2 = data_025_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_030_DD2 = data_030_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_035_DD2 = data_035_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_DD2 = np.append(SN_E_x_000_DD2, SN_E_x_005_DD2, axis=0)
SN_E_x_DD2 = np.append(SN_E_x_DD2, SN_E_x_010_DD2, axis = 0)
SN_E_x_DD2 = np.append(SN_E_x_DD2, SN_E_x_015_DD2, axis = 0)
#SN_E_x_DD2 = np.append(SN_E_x_DD2, SN_E_x_020_DD2, axis = 0)
#SN_E_x_DD2 = np.append(SN_E_x_DD2, SN_E_x_025_DD2, axis = 0)
#SN_E_x_DD2 = np.append(SN_E_x_DD2, SN_E_x_030_DD2, axis = 0)
#SN_E_x_DD2 = np.append(SN_E_x_DD2, SN_E_x_035_DD2, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000_DD2 = data_000_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005_DD2 = data_005_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010_DD2 = data_010_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015_DD2 = data_015_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_020_DD2 = data_020_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_025_DD2 = data_025_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_030_DD2 = data_030_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_035_DD2 = data_035_DD2["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_DD2 = np.append(SN_E_e_000_DD2, SN_E_x_bar_005_DD2, axis=0)
SN_E_x_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_x_bar_010_DD2, axis = 0)
SN_E_x_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_x_bar_015_DD2, axis = 0)
#SN_E_x_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_x_bar_020_DD2, axis = 0)
#SN_E_x_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_x_bar_025_DD2, axis = 0)
#SN_E_x_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_x_bar_030_DD2, axis = 0)
#SN_E_x_bar_DD2 = np.append(SN_E_e_bar_DD2, SN_E_x_bar_035_DD2, axis = 0)



###################################################################################################################################

#FSUGold
#eulerian nu e
SN_E_e_000_FSU = data_000_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005_FSU = data_005_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010_FSU = data_010_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015_FSU = data_015_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_020_FSU = data_020_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_025_FSU = data_025_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_030_FSU = data_030_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_035_FSU = data_035_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_FSU = np.append(SN_E_e_000_FSU, SN_E_e_005_FSU, axis=0)
SN_E_e_FSU = np.append(SN_E_e_FSU, SN_E_e_010_FSU, axis = 0)
SN_E_e_FSU = np.append(SN_E_e_FSU, SN_E_e_015_FSU, axis = 0)
#SN_E_e_FSU = np.append(SN_E_e_FSU, SN_E_e_020_FSU, axis = 0)
#SN_E_e_FSU = np.append(SN_E_e_FSU, SN_E_e_025_FSU, axis = 0)
#SN_E_e_FSU = np.append(SN_E_e_FSU, SN_E_e_030_FSU, axis = 0)
#SN_E_e_FSU = np.append(SN_E_e_FSU, SN_E_e_035_FSU, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000_FSU = data_000-FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005_FSU = data_005_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010_FSU = data_010_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015_FSU = data_015_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_020_FSU = data_020_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_025_FSU = data_025_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_030_FSU = data_030_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_035_FSU = data_035_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_FSU = np.append(SN_E_e_000_FSU, SN_E_e_bar_005_FSU, axis=0)
SN_E_e_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_e_bar_010_FSU, axis = 0)
SN_E_e_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_e_bar_015_FSU, axis = 0)
#SN_E_e_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_e_bar_020_FSU, axis = 0)
#SN_E_e_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_e_bar_025_FSU, axis = 0)
#SN_E_e_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_e_bar_030_FSU, axis = 0)
#SN_E_e_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_e_bar_035_FSU, axis = 0)

#eulerian nu x
SN_E_x_000_FSU = data_000_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005_FSU = data_005_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010_FSU = data_010_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015_FSU = data_015_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_020_FSU = data_020_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_025_FSU = data_025_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_030_FSU = data_030_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_035_FSU = data_035_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_FSU = np.append(SN_E_x_000_FSU, SN_E_x_005_FSU, axis=0)
SN_E_x_FSU = np.append(SN_E_x_FSU, SN_E_x_010_FSU, axis = 0)
SN_E_x_FSU = np.append(SN_E_x_FSU, SN_E_x_015_FSU, axis = 0)
#SN_E_x_FSU = np.append(SN_E_x_FSU, SN_E_x_020_FSU, axis = 0)
#SN_E_x_FSU = np.append(SN_E_x_FSU, SN_E_x_025_FSU, axis = 0)
#SN_E_x_FSU = np.append(SN_E_x_FSU, SN_E_x_030_FSU, axis = 0)
#SN_E_x_FSU = np.append(SN_E_x_FSU, SN_E_x_035_FSU, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000_FSU = data_000_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005_FSU = data_005_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010_FSU = data_010_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015_FSU = data_015_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_020_FSU = data_020_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_025_FSU = data_025_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_030_FSU = data_030_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_035_FSU = data_035_FSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_FSU = np.append(SN_E_e_000_FSU, SN_E_x_bar_005_FSU, axis=0)
SN_E_x_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_x_bar_010_FSU, axis = 0)
SN_E_x_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_x_bar_015_FSU, axis = 0)
#SN_E_x_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_x_bar_020_FSU, axis = 0)
#SN_E_x_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_x_bar_025_FSU, axis = 0)
#SN_E_x_bar _FSU= np.append(SN_E_e_bar_FSU, SN_E_x_bar_030_FSU, axis = 0)
#SN_E_x_bar_FSU = np.append(SN_E_e_bar_FSU, SN_E_x_bar_035_FSU, axis = 0)


###############################################################################################################################
#IUFSU
#eulerian nu e
SN_E_e_000_IUFSU = data_000_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005_IUFSU = data_005_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010_IUFSU = data_010_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015_IUFSU = data_015_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_020_IUFSU = data_020_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_025_IUFSU = data_025_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_030_IUFSU = data_030_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_035_IUFSU = data_035_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_IUFSU = np.append(SN_E_e_000_IUFSU, SN_E_e_005_IUFSU, axis=0)
SN_E_e_IUFSU = np.append(SN_E_e_IUFSU, SN_E_e_010_IUFSU, axis = 0)
SN_E_e_IUFSU = np.append(SN_E_e_IUFSU, SN_E_e_015_IUFSU, axis = 0)
#SN_E_e_IUFSU = np.append(SN_E_e_IUFSU, SN_E_e_020_IUFSU, axis = 0)
#SN_E_e_IUFSU = np.append(SN_E_e_IUFSU, SN_E_e_025_IUFSU, axi_IUFSUs = 0)
#SN_E_e_IUFSU = np.append(SN_E_e_IUFSU, SN_E_e_030_IUFSU, axis = 0)
#SN_E_e_IUFSU = np.append(SN_E_e_IUFSU, SN_E_e_035_IUFSU, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000_IUFSU = data_000_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005_IUFSU = data_005_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010_IUFSU = data_010_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015_IUFSU = data_015_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_020_IUFSU = data_020_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_025_IUFSU = data_025_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_030_IUFSU = data_030_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_035_IUFSU = data_035_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_IUFSU = np.append(SN_E_e_000_IUFSU, SN_E_e_bar_005_IUFSU, axis=0)
SN_E_e_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_e_bar_010_IUFSU, axis = 0)
SN_E_e_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_e_bar_015_IUFSU, axis = 0)
#SN_E_e_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_e_bar_020_IUFSU, axis = 0)
#SN_E_e_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_e_bar_025_IUFSU, axis = 0)
#SN_E_e_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_e_bar_030_IUFSU, axis = 0)
#SN_E_e_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_e_bar_035_IUFSU, axis = 0)

#eulerian nu x
SN_E_x_000_IUFSU = data_000_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005_IUFSU = data_005_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010_IUFSU = data_010_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015_IUFSU = data_015_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_020_IUFSU = data_020_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_025_IUFSU = data_025_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_030_IUFSU = data_030_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_035_IUFSU = data_035_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_IUFSU = np.append(SN_E_x_000_IUFSU, SN_E_x_005_IUFSU, axis=0)
SN_E_x_IUFSU = np.append(SN_E_x_IUFSU, SN_E_x_010_IUFSU, axis = 0)
SN_E_x_IUFSU = np.append(SN_E_x,_IUFSU SN_E_x_015_IUFSU, axis = 0)
#SN_E_x_IUFSU = np.append(SN_E_x_IUFSU, SN_E_x_020_IUFSU axis = 0)
#SN_E_x_IUFSU = np.append(SN_E_x_IUFSU, SN_E_x_025_IUFSU, axis = 0)
#SN_E_x_IUFSU = np.append(SN_E_x_IUFSU, SN_E_x_030_IUFSU, axis = 0)
#SN_E_x_IUFSU = np.append(SN_E_x_IUFSU, SN_E_x_035_IUFSU, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000_IUFSU = data_000_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005_IUFSU = data_005_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010_IUFSU = data_010_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015_IUFSU = data_015_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_020_IUFSU = data_020_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_025_IUFSU = data_025_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_030_IUFSU = data_030_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_035_IUFSU = data_035_IUFSU["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_IUFSU = np.append(SN_E_e_000_IUFSU, SN_E_x_bar_005_IUFSU, axis=0)
SN_E_x_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_x_bar_010_IUFSU, axis = 0)
SN_E_x_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_x_bar_015_IUFSU, axis = 0)
#SN_E_x_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_x_bar_020_IUFSU, axis = 0)
#SN_E_x_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_x_bar_025_IUFSU, axis = 0)
#SN_E_x_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_x_bar_030_IUFSU, axis = 0)
#SN_E_x_bar_IUFSU = np.append(SN_E_e_bar_IUFSU, SN_E_x_bar_035_IUFSU, axis = 0)



###############################################################################################################################################


#LSBCK
#eulerian nu e
SN_E_e_000_LSBCK = data_000_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005_LSBCK = data_005_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010_LSBCK = data_010_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015_LSBCK = data_015_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_020_LSBCK = data_020_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_025_LSBCK = data_025_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_030_LSBCK = data_030_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_035_LSBCK = data_035_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_LSBCK = np.append(SN_E_e_000_LSBCK, SN_E_e_005_LSBCK, axis=0)
SN_E_e_LSBCK = np.append(SN_E_e_LSBCK, SN_E_e_010_LSBCK, axis = 0)
SN_E_e_LSBCK = np.append(SN_E_e_LSBCK, SN_E_e_015_LSBCK, axis = 0)
#SN_E_e_LSBCK = np.append(SN_E_e_LSBCK, SN_E_e_020_LSBCK, axis = 0)
#SN_E_e_LSBCK = np.append(SN_E_e_LSBCK, SN_E_e_025_LSBCK, axis = 0)
#SN_E_e_LSBCK = np.append(SN_E_e_LSBCK, SN_E_e_030_LSBCK, axis = 0)
#SN_E_e_LSBCK = np.append(SN_E_e_LSBCK, SN_E_e_03_LSBCK, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000_LSBCK = data_000_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005_LSBCK = data_005_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010_LSBCK = data_010_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015_LSBCK = data_015_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_020_LSBCK = data_020_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_025_LSBCK = data_025_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_030_LSBCK = data_030_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_035_LSBCK = data_035_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_LSBCK = np.append(SN_E_e_000_LSBCK, SN_E_e_bar_005_LSBCK, axis=0)
SN_E_e_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_e_bar_010_LSBCK, axis = 0)
SN_E_e_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_e_bar_015_LSBCK, axis = 0)
#SN_E_e_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_e_bar_020_LSBCK, axis = 0)
#SN_E_e_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_e_bar_025_LSBCK, axis = 0)
#SN_E_e_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_e_bar_030_LSBCK, axis = 0)
#SN_E_e_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_e_bar_035_LSBCK, axis = 0)

#eulerian nu x
SN_E_x_000_LSBCK = data_000_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005_LSBCK = data_005_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010_LSBCK = data_010_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015_LSBCK = data_015_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_020_LSBCK = data_020_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_025_LSBCK = data_025_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_030_LSBCK = data_030_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_035_LSBCK = data_035_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_LSBCK = np.append(SN_E_x_000_LSBCK, SN_E_x_005_LSBCK, axis=0)
SN_E_x_LSBCK = np.append(SN_E_x_LSBCK, SN_E_x_010_LSBCK, axis = 0)
SN_E_x_LSBCK = np.append(SN_E_x_LSBCK, SN_E_x_015_LSBCK, axis = 0)
#SN_E_x_LSBCK = np.append(SN_E_x_LSBCK, SN_E_x_020_LSBCK, axis = 0)
#SN_E_x_LSBCK = np.append(SN_E_x_LSBCK, SN_E_x_025_LSBCK, axis = 0)
#SN_E_x_LSBCK = np.append(SN_E_x_LSBCK, SN_E_x_030_LSBCK, axis = 0)
#SN_E_x_LSBCK = np.append(SN_E_x_LSBCK, SN_E_x_035_LSBCK, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000_LSBCK = data_000_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005_LSBCK = data_005_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010_LSBCK = data_010_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015_LSBCK = data_015_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_020_LSBCK = data_020_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_025_LSBCK = data_025_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_030_LSBCK = data_030_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_035_LSBCK = data_035_LSBCK["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_LSBCK = np.append(SN_E_e_000_LSBCK, SN_E_x_bar_005_LSBCK, axis=0)
SN_E_x_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_x_bar_010_LSBCK, axis = 0)
SN_E_x_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_x_bar_015_LSBCK, axis = 0)
#SN_E_x_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_x_bar_020_LSBCK, axis = 0)
#SN_E_x_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_x_bar_025_LSBCK, axis = 0)
#SN_E_x_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_x_bar_030_LSBCK, axis = 0)
#SN_E_x_bar_LSBCK = np.append(SN_E_e_bar_LSBCK, SN_E_x_bar_035_LSBCK, axis = 0)



################################################################################################################################



#NL3
#eulerian nu e
SN_E_e_000_NL3 = data_000_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005_NL3 = data_005_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010_NL3 = data_010_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015_NL3 = data_015_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_020_NL3 = data_020_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_025_NL3 = data_025_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_030_NL3 = data_030_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_035_NL3 = data_035_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_NL3 = np.append(SN_E_e_000_NL3, SN_E_e_005_NL3, axis=0)
SN_E_e_NL3 = np.append(SN_E_e_NL3, SN_E_e_010_NL3, axis = 0)
SN_E_e_NL3 = np.append(SN_E_e_NL3, SN_E_e_015_NL3, axis = 0)
#SN_E_e_NL3 = np.append(SN_E_e_NL3, SN_E_e_020_NL3, axis = 0)
#SN_E_e_NL3 = np.append(SN_E_e_NL3, SN_E_e_025_NL3, axis = 0)
#SN_E_e_NL3 = np.append(SN_E_e_NL3, SN_E_e_030_NL3, axis = 0)
#SN_E_e_NL3 = np.append(SN_E_e_NL3, SN_E_e_035_NL3, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000_NL3 = data_000_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005_NL3 = data_005_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010_NL3 = data_010_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015_NL3 = data_015_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_020_NL3 = data_020_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_025_NL3 = data_025_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_030_NL3 = data_030_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_035_NL3 = data_035_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_NL3 = np.append(SN_E_e_000_NL3, SN_E_e_bar_005_NL3, axis=0)
SN_E_e_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_e_bar_010_NL3, axis = 0)
SN_E_e_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_e_bar_015_NL3, axis = 0)
#SN_E_e_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_e_bar_020_NL3, axis = 0)
#SN_E_e_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_e_bar_025_NL3, axis = 0)
#SN_E_e_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_e_bar_030_NL3, axis = 0)
#SN_E_e_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_e_bar_035_NL3, axis = 0)

#eulerian nu x
SN_E_x_000 = data_000["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005 = data_005["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010 = data_010["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015 = data_015["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_020 = data_020["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_025 = data_025["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_030 = data_030["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_035 = data_035["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x = np.append(SN_E_x_000, SN_E_x_005, axis=0)
SN_E_x = np.append(SN_E_x, SN_E_x_010, axis = 0)
SN_E_x = np.append(SN_E_x, SN_E_x_015, axis = 0)
#SN_E_x = np.append(SN_E_x, SN_E_x_020, axis = 0)
#SN_E_x = np.append(SN_E_x, SN_E_x_025, axis = 0)
#SN_E_x = np.append(SN_E_x, SN_E_x_030, axis = 0)
#SN_E_x = np.append(SN_E_x, SN_E_x_035, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000_NL3 = data_000_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005_NL3 = data_005_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010_NL3 = data_010_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015_NL3 = data_015_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_020_NL3 = data_020_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_025_NL3 = data_025_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_030_NL3 = data_030_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_035_NL3 = data_035_NL3["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_NL3 = np.append(SN_E_e_000_NL3, SN_E_x_bar_005_NL3, axis=0)
SN_E_x_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_x_bar_010_NL3, axis = 0)
SN_E_x_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_x_bar_015_NL3, axis = 0)
#SN_E_x_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_x_bar_020_NL3, axis = 0)
#SN_E_x_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_x_bar_025_NL3, axis = 0)
#SN_E_x_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_x_bar_030_NL3, axis = 0)
#SN_E_x_bar_NL3 = np.append(SN_E_e_bar_NL3, SN_E_x_bar_035_NL3, axis = 0)



###############################################################################################################################



#SFHo
#eulerian nu e
SN_E_e_000_SFHo = data_000_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005_SFHo = data_005_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010_SFHo = data_010_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015_SFHo = data_015_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_020_SFHo = data_020_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_025_SFHo = data_025_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_030_SFHo = data_030_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_035_SFHo = data_035_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_SFHo = np.append(SN_E_e_000_SFHo, SN_E_e_005_SFHo, axis=0)
SN_E_e_SFHo = np.append(SN_E_e,_SFHo SN_E_e_010_SFHo, axis = 0)
SN_E_e_SFHo = np.append(SN_E_e_SFHo, SN_E_e_015_SFHo, axis = 0)
#SN_E_e_SFHo = np.append(SN_E_e_SFHo, SN_E_e_020_SFHo, axis = 0)
#SN_E_e_SFHo = np.append(SN_E_e_SFHo, SN_E_e_025_SFHo, axis = 0)
#SN_E_e_SFHo = np.append(SN_E_e_SFHo, SN_E_e_030_SFHo, axis = 0)
#SN_E_e_SFHo = np.append(SN_E_e_SFHo, SN_E_e_035_SFHo, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000_SFHo = data_000_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005_SFHo = data_005_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010_SFHo = data_010_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015_SFHo = data_015_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_020_SFHo = data_020_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_025_SFHo = data_025_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_030_SFHo = data_030_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_035_SFHo = data_035_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_SFHo = np.append(SN_E_e_000_SFHo, SN_E_e_bar_005_SFHo, axis=0)
SN_E_e_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_e_bar_010_SFHo, axis = 0)
SN_E_e_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_e_bar_015_SFHo, axis = 0)
#SN_E_e_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_e_bar_020_SFHo, axis = 0)
#SN_E_e_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_e_bar_025_SFHo, axis = 0)
#SN_E_e_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_e_bar_030_SFHo, axis = 0)
#SN_E_e_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_e_bar_035_SFHo, axis = 0)

#eulerian nu x
SN_E_x_000_SFHo = data_000_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005_SFHo = data_005_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010_SFHo = data_010_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015_SFHo = data_015_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_020_SFHo = data_020_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_025_SFHo = data_025_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_030_SFHo = data_030_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_035_SFHo = data_035_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_SFHo = np.append(SN_E_x_000_SFHo, SN_E_x_005_SFHo, axis=0)
SN_E_x_SFHo = np.append(SN_E_x_SFHo, SN_E_x_010_SFHo, axis = 0)
SN_E_x_SFHo = np.append(SN_E_x_SFHo, SN_E_x_015_SFHo, axis = 0)
#SN_E_x_SFHo = np.append(SN_E_x_SFHo, SN_E_x_020_SFHo, axis = 0)
#SN_E_x_SFHo = np.append(SN_E_x_SFHo, SN_E_x_025_SFHo, axis = 0)
#SN_E_x_SFHo = np.append(SN_E_x_SFHo, SN_E_x_030_SFHo, axis = 0)
#SN_E_x_SFHo = np.append(SN_E_x_SFHo, SN_E_x_035_SFHo, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000_SFHo = data_000_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005_SFHo = data_005_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010_SFHo = data_010_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015_SFHo = data_015_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_020_SFHo = data_020_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_025_SFHo = data_025_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_030_SFHo = data_030_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_035_SFHo = data_035_SFHo["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_SFHo = np.append(SN_E_e_000_SFHo, SN_E_x_bar_005_SFHo, axis=0)
SN_E_x_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_x_bar_010_SFHo, axis = 0)
SN_E_x_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_x_bar_015_SFHo, axis = 0)
#SN_E_x_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_x_bar_020_SFHo, axis = 0)
#SN_E_x_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_x_bar_025_SFHo, axis = 0)
#SN_E_x_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_x_bar_030_SFHo, axis = 0)
#SN_E_x_bar_SFHo = np.append(SN_E_e_bar_SFHo, SN_E_x_bar_035_SFHo, axis = 0)





#SFHx
#eulerian nu e
SN_E_e_000_SFHx = data_000_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_005_SFHx = data_005_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_010_SFHx = data_010_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_015_SFHx = data_015_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_020_SFHx = data_020_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_025_SFHx = data_025_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_030_SFHx = data_030_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
#SN_E_e_035_SFHx = data_035_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e"][:]
SN_E_e_SFHx = np.append(SN_E_e_000_SFHx, SN_E_e_005_SFHx, axis=0)
SN_E_e_SFHx = np.append(SN_E_e_SFHx, SN_E_e_010_SFHx, axis = 0)
SN_E_e_SFHx = np.append(SN_E_e_SFHx, SN_E_e_015_SFHx, axis = 0)
#SN_E_e_SFHx = np.append(SN_E_e_SFHx, SN_E_e_020_SFHx, axis = 0)
#SN_E_e_SFHx = np.append(SN_E_e_SFHx, SN_E_e_025_SFHx, axis = 0)
#SN_E_e_SFHx = np.append(SN_E_e_SFHx, SN_E_e_030_SFHx, axis = 0)
#SN_E_e_SFHx = np.append(SN_E_e_SFHx, SN_E_e_035_SFHx, axis = 0)

#eulerian nu e bar
SN_E_e_bar_000_SFHx = data_000_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_005_SFHx = data_005_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_010_SFHx = data_010_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_015_SFHx = data_015_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_020_SFHx = data_020_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_025_SFHx = data_025_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_030_SFHx = data_030_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
#SN_E_e_bar_035_SFHx = data_035_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_e_b"][:]
SN_E_e_bar_SFHx = np.append(SN_E_e_000_SFHx, SN_E_e_bar_005_SFHx, axis=0)
SN_E_e_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_e_bar_010_SFHx, axis = 0)
SN_E_e_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_e_bar_015_SFHx, axis = 0)
#SN_E_e_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_e_bar_020_SFHx, axis = 0)
#SN_E_e_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_e_bar_025_SFHx, axis = 0)
#SN_E_e_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_e_bar_030_SFHx, axis = 0)
#SN_E_e_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_e_bar_035_SFHx, axis = 0)

#eulerian nu x
SN_E_x_000_SFHx = data_000_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_005_SFHx = data_005_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_010_SFHx = data_010_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_015_SFHx = data_015_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_020_SFHx = data_020_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_025_SFHx = data_025_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_030_SFHx = data_030_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
#SN_E_x_035_SFHx = data_035_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x"][:]
SN_E_x_SFHx = np.append(SN_E_x_000_SFHx, SN_E_x_005_SFHx, axis=0)
SN_E_x_SFHx = np.append(SN_E_x_SFHx, SN_E_x_010_SFHx, axis = 0)
SN_E_x_SFHx = np.append(SN_E_x_SFHx, SN_E_x_015_SFHx, axis = 0)
#SN_E_x_SFHx = np.append(SN_E_x_SFHx, SN_E_x_020_SFHx, axis = 0)
#SN_E_x_SFHx = np.append(SN_E_x_SFHx, SN_E_x_025_SFHx, axis = 0)
#SN_E_x_SFHx = np.append(SN_E_x_SFHx, SN_E_x_030_SFHx, axis = 0)
#SN_E_x_SFHx = np.append(SN_E_x_SFHx, SN_E_x_035_SFHx, axis = 0)

#eulerian nu x bar
SN_E_x_bar_000_SFHx = data_000_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_005_SFHx = data_005_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_010_SFHx = data_010_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_015_SFHx = data_015_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_020_SFHx = data_020_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_025_SFHx = data_025_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_030_SFHx = data_030_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
#SN_E_x_bar_035_SFHx = data_035_SFHx["Number Spectrum"]["Eulerian-Lab Frame"]["nu_x_b"][:]
SN_E_x_bar_SFHx = np.append(SN_E_e_000_SFHx, SN_E_x_bar_005_SFHx, axis=0)
SN_E_x_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_x_bar_010_SFHx, axis = 0)
SN_E_x_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_x_bar_015_SFHx, axis = 0)
#SN_E_x_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_x_bar_020_SFHx, axis = 0)
#SN_E_x_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_x_bar_025_SFHx, axis = 0)
#SN_E_x_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_x_bar_030_SFHx, axis = 0)
#SN_E_x_bar_SFHx = np.append(SN_E_e_bar_SFHx, SN_E_x_bar_035_SFHx, axis = 0)





fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize = (10, 7), layout = "constrained", sharey = True, sharex = True)
fig.supxlabel(r"$\mathrm{Energy \ MeV}$")
fig.supylabel(r"$\mathrm{Number \ Luminosity \ Spectrum \ \frac{d^2L_n}{dEd\omega} (s^{-1}MeV^{-1}str^{-1}})$", fontsize = 14)


#usingpictures
for i in range(len(time)):
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
    
    axs[0, 0].semilogx(energy_bins, SN_E_e_DD2[i, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar_DD2[i, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x_DD2[i, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar_DD2[i, 0, 90], color = "Black", animated = True)

    axs[0, 0].semilogx(energy_bins, SN_E_e_FSU[i, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar_FSU[i, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x_FSU[i, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar_FSU[i, 0, 90], color = "Black", animated = True)

    axs[0, 0].semilogx(energy_bins, SN_E_e_IUFSU[i, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar_IUFSU[i, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x_IUFSU[i, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar_IUFSU[i, 0, 90], color = "Black", animated = True)

    axs[0, 0].semilogx(energy_bins, SN_E_e_LSBCK[i, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar_LSBCK[i, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x_LSBCK[i, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar_LSBCK[i, 0, 90], color = "Black", animated = True)

    axs[0, 0].semilogx(energy_bins, SN_E_e_NL3[i, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar_NL3[i, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x_NL3[i, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar_NL3[i, 0, 90], color = "Black", animated = True)

    axs[0, 0].semilogx(energy_bins, SN_E_e_SFHo[i, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar_SFHo[i, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x_SFHo[i, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar_SFHo[i, 0, 90], color = "Black", animated = True)

    axs[0, 0].semilogx(energy_bins, SN_E_e_SFHx[i, 0, 90], color = "Black", animated=True)
    axs[0, 1].semilogx(energy_bins, SN_E_e_bar_SFHx[i, 0, 90], color = "Black", animated = True)
    axs[1, 0].semilogx(energy_bins, 2.0 * SN_E_x_SFHx[i, 0, 90], color = "Black", animated = True)
    axs[1, 1].semilogx(energy_bins, 2.0 * SN_E_x_bar_SFHx[i, 0, 90], color = "Black", animated = True)

    axs[1, 1].set_xlabel(f"Time = {round(time[i], 3)*1000}ms", loc = "right")
    plt.savefig(f"Graphs/sn_graph{i}.png")
    
