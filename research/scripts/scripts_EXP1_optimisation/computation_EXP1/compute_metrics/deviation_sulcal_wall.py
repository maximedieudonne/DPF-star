import slam.geodesics as sdg
import pickle
import os
import settings.path_manager as pm
import slam.io as sio
import pandas as pd
import os
import tools.io as tio
import networkx as nx
import numpy as np
import pandas as pd
import slam.texture as stex
import slam.geodesics as slg
import pickle
import math
import matplotlib.pyplot as plt

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in degree between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return math.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))


def grad_list(mesh, trace):
    grad_swp = list()
    for i in np.arange(1,len(trace)):
        gsw = [trace[i] , mesh.vertices[trace[i]] - mesh.vertices[trace[i-1]]]
        grad_swp.append(gsw)
    return  grad_swp

# load subject
wd = '/home/maxime/callisto/repo/paper_sulcal_depth/data/diffuse_fundicrest'
folder_info_dataset = pm.folder_info_dataset
folder_meshes = pm.folder_meshes
folder_subject_analysis = pm.folder_subject_analysis
folder_manual_labelisation = pm.folder_manual_labelisation
info_database = pd.read_csv(os.path.join(folder_info_dataset, 'info_database.csv'))
size_ratio = pd.read_csv(os.path.join(folder_info_dataset, 'size_ratio_KKI113.csv'))
list_subs = info_database['participant_id'].values
list_ses = info_database['session_id'].values

nbs = 10
list_subs = list_subs[0:nbs]
#list_subs = [list_subs[0]]

fig, axs = plt.subplots(nbs, sharex=True)
for idx, sub, in enumerate(list_subs):
    print('#################### ', sub)
    ses = list_ses[idx]

    #import mesh
    mesh_name = 'sub-'+ sub +'_ses-' +ses + '_hemi-L_space-T2w_wm.surf.gii'
    mesh_path = os.path.join(folder_meshes, mesh_name)
    mesh = sio.load_mesh(mesh_path)

    # import gradient of the depth

    gradDepth = pd.read_csv(os.path.join(folder_subject_analysis, sub + '_' + ses, 'surface_processing',
                                              'sulc/derivatives/gradient', sub + '_' + ses + '_grad_sulc.csv'))

    #import sulcal wall path
    with open(os.path.join(wd, sub + '_' + ses + '_sulcalwall.pkl'), 'rb') as file:
        # Call load method to deserialize
        sw_trace = pickle.load(file)

    # calcul de l'angle en chaque point


    list_angle_surface =list()

    for sub_fundi in sw_trace:
        list_angles_subfundi = list()
        for trace in sub_fundi:
            grad_trace = grad_list(mesh, trace)
            list_angles_trace = list()
            for grad_vtx in grad_trace:
                vtx = grad_vtx[0]
                gvtx = grad_vtx[1]
                gdepth = gradDepth.iloc[vtx].values
                angle = angle_between(gvtx, gdepth)
                print(angle)
                list_angles_trace.append(angle)
            list_angles_subfundi.append(list_angles_trace)
        list_angle_surface.append(list_angles_subfundi)

    with open(os.path.join(wd, sub + '_' + ses + '_angle_sulc.pkl'), 'wb') as file:
        pickle.dump(list_angle_surface, file)


    aa = [item for sublist in list_angle_surface for item in sublist]
    aaa = [item for  sublist in aa for item in sublist]
    axs[idx].hist(x = aaa, bins=np.arange(0,180,5))


    # make the average

plt.show()
## calculer le gradient de la texture


#### extraire les lignes


# pour une ligne : chemin.

# dire le point connecté a la crete et le point connecté au fundi

# en chaque point en partant du haut
# faire direction naiv avec le voisin d'apres
# calculer la difference angulaire
# ajouter a la liste

# faire la moyenne



