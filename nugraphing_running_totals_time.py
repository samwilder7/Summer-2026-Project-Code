#graphing the running total versus time
total_sums_list = []
times = []
total_sum = 0
sim = "E15-DD2"

for i in np.arange(1, 10694): 
    total_sum_for_timestep = 0
    file_number = str(i).zfill(5)
    name_var = f"/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/{sim}/{sim}-500km-Public/snowglobes/Ray-By-Ray/Eulerian-Lab/snowglobes_output/Source/num_{file_number}/E15-DD2_neutrino_number_spectrum_Lab_S_010kpc_"

    nc_nue_ar40 = np.nan_to_num(np.genfromtxt(name_var + file_number + "_nc_nue_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2))
    if len(nc_nue_ar40) < 1:
        print(f"{i} is empty")
        continue
    times = np.append(times, i)
    nc_nuebar_ar40 = np.genfromtxt(name_var + file_number + "_nc_nuebar_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2)
        
    nc_numu_ar40 = np.genfromtxt(name_var + file_number + "_nc_numu_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2)
    nc_numubar_ar40 = np.genfromtxt(name_var + file_number + "_nc_numubar_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2)
        
    nc_nutau_ar40 = np.genfromtxt(name_var + file_number + "_nc_nutau_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2)
    nc_nutaubar_ar40 = np.genfromtxt(name_var + file_number + "_nc_nutaubar_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2)
    nue_ar40 = np.genfromtxt(name_var + file_number + "_nue_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2)
    nuebar_ar40 = np.genfromtxt(name_var + file_number + "_nuebar_Ar40_ar40kt_events_unweighted.dat", skip_footer = 2)
    nue_ar40_electron = np.nan_to_num(np.genfromtxt(name_var + file_number + "_nue_e_ar40kt_events_unweighted.dat", skip_footer = 2))
    nuebar_ar40_electron = np.genfromtxt(name_var + file_number + "_nuebar_e_ar40kt_events_unweighted.dat", skip_footer = 2)
        
    numu_ar40_electron = np.genfromtxt(name_var + file_number + "_numu_e_ar40kt_events_unweighted.dat", skip_footer = 2)
    numubar_ar40_electron = np.genfromtxt(name_var + file_number + "_numubar_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)
        
    nutau_ar40_electron = np.genfromtxt(name_var + file_number + "_nutau_e_ar40kt_events_unweighted.dat", skip_footer = 2)
    nutaubar_ar40_electron = np.genfromtxt(name_var + file_number + "_nutaubar_e_ar40kt_events_unweighted.dat", skip_footer = 2)
    
    
    # time = nc_nue_ar40[:, 0]
    
    nc_nue_ar40_sum = np.sum(nc_nue_ar40[:, 1])
    
    nc_nuebar_ar40_sum = np.sum(nc_nuebar_ar40[:, 1])
    
    nc_numu_ar40_sum = np.sum(nc_numu_ar40[:, 1])
    
    nc_numubar_ar40_sum = np.sum(nc_numubar_ar40[:, 1])
    
    nc_nutau_ar40_sum = np.sum(nc_nutau_ar40[:, 1])
    
    nc_nutaubar_ar40_sum = np.sum(nc_nutaubar_ar40[:, 1])
    
    nue_ar40_sum = np.sum(nue_ar40[:, 1])
    
    nuebar_ar40_sum = np.sum(nuebar_ar40[:,1])
    
    nue_ar40_electron_sum = np.sum(nue_ar40_electron[:,1])
    
    nuebar_ar40_electron_sum = np.sum(nuebar_ar40_electron[:,1])
    
    numu_ar40_electron_sum = np.sum(numu_ar40_electron[:,1])
    
    numubar_ar40_electron_sum = np.sum(numubar_ar40_electron[:,1])
    
    nutau_ar40_electron_sum = np.sum(nutau_ar40_electron[:,1])
    
    nutaubar_ar40_electron_sum = np.sum(nutaubar_ar40_electron[:,1])
    
    total_sum_for_timestep = nc_nue_ar40_sum + nc_nuebar_ar40_sum + nc_numu_ar40_sum + nc_numubar_ar40_sum + nc_nutau_ar40_sum + nc_nutaubar_ar40_sum + nue_ar40_sum + nuebar_ar40_sum + nue_ar40_electron_sum + nuebar_ar40_electron_sum  + numu_ar40_electron_sum + numubar_ar40_electron_sum + nutau_ar40_electron_sum + nutaubar_ar40_electron_sum
    total_sum = total_sum + total_sum_for_timestep
    total_sums_list = np.append(total_sums_list, total_sum)

fig, axs = plt.subplots(figsize = (20, 7))
axs.loglog(times, (2*(10**(-4)))*total_sums_list)
axs.set_xlabel(r"$\mathrm{Time \ Step}$")
axs.set_ylabel(r"$\mathrm{Total \ Events}$")
axs.set_title(r"$\mathrm{Running \ Sum \ for \ Each \ Time \ Signature}$")
plt.grid(True)
plt.savefig("/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/sam_summer2026/snowglobesrunningsumsplot.png")
plt.show()
#2 times ten to the negative four (multiply y by that number)
