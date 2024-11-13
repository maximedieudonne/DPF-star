import functions.dpf as dpf
import numpy as np
import trimesh
import config as cfg


def dpf_star(mesh, curvature, alpha_ref=500):
    """
    Compute the dpf-star function of a mesh as described in
    M. Dieudonné, J. Lefèvre, G.Auzias (2025)
    New scale-invariant sulcal depth measure
    :param mesh: 3D mesh with N vertices
    :param curvature: array (1,N)
    :alpha: regularisation parameter 
    :return: array dpf star
    """
    scaling = mesh.volume
    alpha = 1/np.power(scaling,2) * alpha_ref 
    # compute dpf
    depth = dpf.depth_potential_function(mesh, curvature=curvature, alpha=alpha)
    # normalisation
    dpf_star = -depth /scaling 
    dpf_star = dpf_star * 1000 #for better unit
    return dpf_star