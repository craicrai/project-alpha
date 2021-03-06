"""
Creates several images that will be used in our final paper

"""
from __future__ import absolute_import, division, print_function
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import os
import sys

bRIGHT= True # if you'd like to brighten up them charts

project_path          = "../../"
path_to_data          = project_path+"data/ds009/"
location_of_images    = project_path+"images/"
location_of_functions = project_path+"code/utils/functions/" 
final_data            = "../data/"
behav_suffix           = "/behav/task001_run001/behavdata.txt"
smooth_data           =  final_data + 'smooth/'
hrf_data              = final_data + 'hrf/'

sys.path.append(location_of_functions)

# list of subjects
sub_list = os.listdir(path_to_data)
sub_list = [i for i in sub_list if 'sub' in i]


from Image_Visualizing import present_3d


#load in results from benjamini hochberg, t, and beta analysis

bh_all   = np.load("../data/bh_t_beta/bh_all.npy")
t_all    = np.load("../data/bh_t_beta/t_all.npy")
beta_all = np.load("../data/bh_t_beta/beta_all.npy")


bh_all[bh_all!=1]=np.nan
t_all[t_all!=1]=np.nan
beta_all[beta_all!=1]=np.nan



# subjects desired 1,3,6,7,11,23
desired_index=[0,2,5,6,9,18]


# Progress bar
toolbar_width=len(desired_index)
sys.stdout.write("Clustering images:  ")
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))


for i in desired_index:
    name=sub_list[i]
    # the mask for each subject
    path_to_data = project_path + "data/ds009/" + name
    brain = nib.load(path_to_data + '/anatomy/inplane001_brain.nii.gz')
    brain=brain.get_data()


    ###########################
    # Benjamini Hochberg Plot #
    ###########################
    
    plt.imshow(present_3d(brain[::2,::2,:]),cmap="gray")

    upper= np.percentile(np.ravel(brain[::2,::2,:]),95)
    plt.colorbar()
    if bRIGHT:
    	plt.clim(0,upper)
    overlap=present_3d(bh_all[...,i])
    overlap[overlap==0]=np.nan
    overlap[-1,-1]=0 # to make the output correct
    plt.imshow(overlap,cmap="bwr",alpha=.7)
    plt.xticks([])
    plt.yticks([])
    plt.title(name+ ", Benjamini Hochberg")
    plt.savefig("../../images/"+name+"_bh_overlay.png")
    plt.close()


    #################
    # T-Value Plot  #
    #################
    plt.imshow(present_3d(brain[::2,::2,:]),cmap="gray")
    plt.colorbar()
    overlap=present_3d(t_all[...,i])
    overlap[overlap==0]=np.nan
    overlap[-1,-1]=0 # to make the output color correct
    if bRIGHT:
    	plt.clim(0,upper)
    plt.xticks([])
    plt.yticks([])
    plt.title(name+ ", t-clustering")
    plt.imshow(overlap,cmap="bwr",alpha=.7)
    plt.savefig("../../images/"+name+"_t_overlay.png")
    plt.close()



    ####################
    # Beta-value Plot  #
    ####################
    
    plt.imshow(present_3d(brain[::2,::2,:]),cmap="gray")
    plt.colorbar()
    overlap=present_3d(beta_all[...,i])
    overlap[overlap==0]=np.nan
    overlap[-1,-1]=0 # to make the output color correct
    if bRIGHT:
    	plt.clim(0,upper)
    plt.xticks([])
    plt.yticks([])
    plt.title(name+ ", Beta-clustering")
    plt.imshow(overlap,cmap="bwr",alpha=.7)
    plt.savefig("../../images/"+name+"_beta_overlay.png")
    plt.close()

    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")


