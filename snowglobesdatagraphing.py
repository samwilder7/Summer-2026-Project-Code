#snowglobes graphing

name_var = "/lustre/orion/ast137/proj-shared/colterrichardson/Neutrinos_Summer_2026/2D/snowglobes_output_test/D9.6-2D_neutrino_number_spectrum_Comoving_S_010kpc_02000_"



#argon 
##smeared & nc
nc_nue_ar40_smeared = np.nan_to_num(np.genfromtxt(name_var+"nc_nue_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2))
nc_nuebar_ar40_smeared = np.genfromtxt(name_var+"nc_nuebar_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)

nc_numu_ar40_smeared = np.genfromtxt(name_var+"nc_numu_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)
nc_numubar_ar40_smeared = np.genfromtxt(name_var+"nc_numubar_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)

nc_nutau_ar40_smeared = np.genfromtxt(name_var+"nc_nutau_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)
nc_nutaubar_ar40_smeared = np.genfromtxt(name_var+"nc_nutaubar_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)

##smeared and cc
nue_ar40_smeared = np.nan_to_num(np.genfromtxt(name_var+"nue_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2))
nuebar_ar40_smeared = np.genfromtxt(name_var+"nuebar_Ar40_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)

##not smeared and nc
nc_nue_ar40 = np.nan_to_num(np.genfromtxt(name_var+"nc_nue_Ar40_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2))
nc_nuebar_ar40 = np.genfromtxt(name_var+"nc_nuebar_Ar40_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)

nc_numu_ar40 = np.genfromtxt(name_var+"nc_numu_Ar40_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)
nc_numubar_ar40 = np.genfromtxt(name_var+"nc_numubar_Ar40_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)

nc_nutau_ar40 = np.genfromtxt(name_var+"nc_nutau_Ar40_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)
nc_nutaubar_ar40 = np.genfromtxt(name_var+"nc_nutaubar_Ar40_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)

##not smeared and cc
nue_ar40 = np.nan_to_num(np.genfromtxt(name_var+"nue_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2))
nuebar_ar40 = np.genfromtxt(name_var+"nuebar_Ar40_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)







#electron (all cc)
##smeared
nue_ar40_smeared_electron = np.nan_to_num(np.genfromtxt(name_var+"nue_e_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2))
nuebar_ar40_smeared_electron = np.genfromtxt(name_var+"nuebar_e_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)

numu_ar40_smeared_electron = np.genfromtxt(name_var+"numu_e_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)
numubar_ar40_smeared_electron = np.genfromtxt(name_var+"numubar_e_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)

nutau_ar40_smeared_electron = np.genfromtxt(name_var+"nutau_e_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)
nutaubar_ar40_smeared_electron = np.genfromtxt(name_var+"nutaubar_e_ar40kt_events_smeared_unweighted.dat", skip_header = 1, skip_footer = 2)

##not smeared
nue_ar40_electron = np.nan_to_num(np.genfromtxt(name_var+"nue_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2))
nuebar_ar40_electron = np.genfromtxt(name_var+"nuebar_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)

numu_ar40_electron = np.genfromtxt(name_var+"numu_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)
numubar_ar40_electron = np.genfromtxt(name_var+"numubar_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)

nutau_ar40_electron = np.genfromtxt(name_var+"nutau_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)
nutaubar_ar40_electron = np.genfromtxt(name_var+"nutaubar_e_ar40kt_events_unweighted.dat", skip_header = 1, skip_footer = 2)





##added together
#smeared
sum_smeared = nue_ar40_smeared_electron + nuebar_ar40_smeared_electron + numu_ar40_smeared_electron + numubar_ar40_smeared_electron + nutau_ar40_smeared_electron + nutaubar_ar40_smeared_electron + nue_ar40_smeared + nuebar_ar40_smeared + nc_nue_ar40_smeared +  nc_nuebar_ar40_smeared + nc_numu_ar40_smeared + nc_numubar_ar40_smeared + nc_nutau_ar40_smeared + nc_nutaubar_ar40_smeared
#unsmeared
sum_unsmeared = nue_ar40_electron + nuebar_ar40_electron + numu_ar40_electron + numubar_ar40_electron + nutau_ar40_electron + nutaubar_ar40_electron + nue_ar40 + nuebar_ar40 + nc_nue_ar40 + nc_nuebar_ar40 + nc_numu_ar40 + nc_numubar_ar40 + nc_nutau_ar40 + nc_nutaubar_ar40



#plotting
fig, axs = plt.subplots(nrows = 3, ncols = 1, figsize = (10, 21))
fig.supxlabel(r"$\mathrm{Energy \ (MeV)}$")
fig.supylabel(r"$\mathrm{Events\ (MeV^{-1})}$")
#############################################################################################################################################
#nc smeared
axs[0].semilogy(1000*nc_nue_ar40_smeared[:,0], nc_nue_ar40_smeared[:,1], label = r"$\mathrm{NC \ \nu_{e} \ {}^{40}Ar}$")
axs[0].semilogy(1000*nc_numu_ar40_smeared[:,0], nc_numu_ar40_smeared[:,1], label = r"$\mathrm{NC \ \nu_{\mu} \ {}^{40}Ar}$")
axs[0].semilogy(1000*nc_nutau_ar40_smeared[:,0], nc_nutau_ar40_smeared[:,1], label = r"$\mathrm{NC \ \nu_{\tau} \ {}^{40}Ar}$")

axs[0].semilogy(1000*nc_nuebar_ar40_smeared[:,0], nc_nuebar_ar40_smeared[:,1], label = r"$\mathrm{NC \ \bar{\nu_{e}} \ {}^{40}Ar}$")
axs[0].semilogy(1000*nc_numubar_ar40_smeared[:,0], nc_numubar_ar40_smeared[:,1], label = r"$\mathrm{NC \ \bar{\nu_{\mu}} \ {}^{40}Ar}$")
axs[0].semilogy(1000*nc_nutaubar_ar40_smeared[:,0], nc_nutaubar_ar40_smeared[:,1], label = r"$\mathrm{NC \ \bar{\nu_{\tau}} \ {}^{40}Ar}$")
#############################################################################################################################################
#cc smeared
axs[0].semilogy(1000*nue_ar40_smeared[:,0], nue_ar40_smeared[:,1], label = r"$\mathrm{CC \ \nu_{e} \ {}^{40}Ar}$")
axs[0].semilogy(1000*nue_ar40_smeared_electron[:,0], nue_ar40_smeared_electron[:,1], label = r"$\mathrm{CC \ \nu_{e} \ e}$")
axs[0].semilogy(1000*numu_ar40_smeared_electron[:,0], numu_ar40_smeared_electron[:,1], label = r"$\mathrm{CC \ \nu_{\mu} \ e}$")
axs[0].semilogy(1000*nutau_ar40_smeared_electron[:,0], nutau_ar40_smeared_electron[:,1], label = r"$\mathrm{CC \ \nu_{\tau} \ e}$")

axs[0].semilogy(1000*nuebar_ar40_smeared[:,0], nuebar_ar40_smeared[:,1], label = r"$\mathrm{CC \ \bar{\nu_{e}} \ {}^{40}Ar}$")
axs[0].semilogy(1000*nuebar_ar40_smeared_electron[:,0], nuebar_ar40_smeared_electron[:,1], label = r"$\mathrm{CC \ \bar{\nu_{e}} \ e}$")
axs[0].semilogy(1000*numubar_ar40_smeared_electron[:,0], numubar_ar40_smeared_electron[:,1], label = r"$\mathrm{CC \ \bar{\nu_{\mu}} \ e}$")
axs[0].semilogy(1000*nutaubar_ar40_smeared_electron[:,0], nutaubar_ar40_smeared_electron[:,1], label = r"$\mathrm{CC \ \bar{\nu_{\tau}} \ e}$")
#############################################################################################################################################
#nc not smeared
axs[1].semilogy(1000*nc_nue_ar40[:,0], nc_nue_ar40[:,1], label = r"$\mathrm{NC \ \nu_{e} \ {}^{40}Ar}$")
axs[1].semilogy(1000*nc_numu_ar40[:,0], nc_numu_ar40[:,1], label = r"$\mathrm{NC \ \nu_{\mu} \ {}^{40}Ar}$")
axs[1].semilogy(1000*nc_nutau_ar40[:,0], nc_nutau_ar40[:,1], label = r"$\mathrm{NC \ \nu_{\tau} \ {}^{40}Ar}$")

axs[1].semilogy(1000*nc_nuebar_ar40[:,0], nc_nuebar_ar40[:,1], label = r"$\mathrm{NC \ \bar{\nu_{e}} \ {}^{40}Ar}$")
axs[1].semilogy(1000*nc_numubar_ar40[:,0], nc_numubar_ar40[:,1], label = r"$\mathrm{NC \ \bar{\nu_{\mu}} \ {}^{40}Ar}$")
axs[1].semilogy(1000*nc_nutaubar_ar40[:,0], nc_nutaubar_ar40[:,1], label = r"$\mathrm{NC \ \bar{\nu_{\tau}} \ {}^{40}Ar}$")
##############################################################################################################################################
#cc not smeared
axs[1].semilogy(1000*nue_ar40[:,0], nue_ar40[:,1], label = r"$\mathrm{CC \ \nu_{e} \ {}^{40}Ar}$")
axs[1].semilogy(1000*nue_ar40_electron[:,0], nue_ar40_electron[:,1], label = r"$\mathrm{CC \ \nu_{e} \ e}$")
axs[1].semilogy(1000*numu_ar40_electron[:,0], numu_ar40_electron[:,1], label = r"$\mathrm{CC \ \nu_{\mu} \ e}$")
axs[1].semilogy(1000*nutau_ar40_electron[:,0], nutau_ar40_electron[:,1], label = r"$\mathrm{CC \ \nu_{\tau} \ e}$")

axs[1].semilogy(1000*nuebar_ar40[:,0], nuebar_ar40[:,1], label = r"$\mathrm{CC \ \bar{\nu_{e}} \ {}^{40}Ar}$")
axs[1].semilogy(1000*nuebar_ar40_electron[:,0], nuebar_ar40_electron[:,1], label = r"$\mathrm{CC \ \bar{\nu_{e}} \ e}$")
axs[1].semilogy(1000*numubar_ar40_electron[:,0], numubar_ar40_electron[:,1], label = r"$\mathrm{CC \ \bar{\nu_{\mu}} \ e}$")
axs[1].semilogy(1000*nutaubar_ar40_electron[:,0], nutaubar_ar40_electron[:,1], label = r"$\mathrm{CC \ \bar{\nu_{\tau}} \ e}$")
#############################################################################################################################################
axs[2].semilogy(1000*nuebar_ar40[:,0], sum_smeared[:,1], label = r"$\mathrm{Smeared}$")
axs[0].semilogy(1000*nuebar_ar40[:,0], sum_smeared[:,1], label = r"$\mathrm{Smeared}$")
axs[2].semilogy(1000*nuebar_ar40[:,0], sum_unsmeared[:,1], label = r"$\mathrm{Unsmeared}$")
axs[1].semilogy(1000*nuebar_ar40[:,0], sum_unsmeared[:,1], label = r"$\mathrm{Unsmeared}$")


axs[0].legend(fontsize = "xx-small", ncol = 2, frameon = False)
axs[1].legend(fontsize = "xx-small", ncol = 2, frameon = False)
axs[2].legend(loc = "lower left")
axs[0].set_title("Smeared")
axs[1].set_title("Not Smeared (Unsmeared?)")
axs[2].set_title("Summed Neutrinos")

plt.show()
