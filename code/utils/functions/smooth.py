from __future__ import absolute_import, division, print_function
import numpy as np
import scipy.ndimage
from scipy.ndimage.filters import gaussian_filter

def smoothvoxels(data_4d, fwhm, time):

    """
    Return a 'smoothed' version of data_4d.

    Parameters
    ----------
    data_4d : numpy array of 4 dimensions 
    The image data of one subject


    fwhm : width of normal gaussian curve

    time : time slice (4th dimension)

    Returns
    -------
    smooth_results : array of the smoothed data from data_4d (same dimensions
        but super-voxels will be indicated by the same number) in time slice 
        indicated.

    Note: Edges are affected by random noise and non-voxel data, but to a 
        lesser extent than a filter as aggressive as a mean-filter. However,
        this type of smoothing was important to the process because a Gaussian
        is less affected by the spikes in data.
    """
    
    time_slice = data_4d[..., time]
    smooth_results = scipy.ndimage.filters.gaussian_filter(time_slice, fwhm)
    return smooth_results

