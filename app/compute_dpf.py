import os
import argparse
from functions import rw 
from functions import texture as stex
from functions import dpf
import config as cfg  # Import du chemin depuis config.py

def save_dpf(dpf, name_subject):
    # Création du dossier wd/named_subject
    save_folder = os.path.join(cfg.WD_FOLDER, name_subject)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Sauvegarde dans le dossier avec le nom dpfstar.gii 
    rw.write_texture(stex.TextureND(darray=dpf), os.path.join(save_folder, cfg.DPF))


def call_compute_curvature(mesh_path):
    os.system(f"python .\compute_curvature.py {mesh_path}")

def call_visuallizer(mesh_path, texture_path):
    os.system(f"python -m app.visualizer {mesh_path} --texture {texture_path}")


def main(mesh_path, curvature=None, display=False):
    # Lecture du maillage
    mesh = rw.load_mesh(mesh_path)

    # Extraction du nom du fichier sans l'extension .gii
    name_subject = os.path.basename(mesh_path).replace('.gii', '')

    # Vérifier si le chemin de courbure est fourni
    if curvature is None:
        try:
            # Chargement de la courbure s'il est présent dans le dossier
            Kmean = rw.read_gii_file(os.path.join(cfg.WD_FOLDER, name_subject, cfg.KMEAN))
        except FileNotFoundError:
            print("Calcul de la courbure car aucune courbure fournie.")
            call_compute_curvature(mesh_path)  # Fonction qui doit exister
            Kmean = rw.read_gii_file(os.path.join(cfg.WD_FOLDER, name_subject, cfg.KMEAN))
    else:
        # Charger la courbure à partir du chemin spécifié
        Kmean = rw.read_gii_file(curvature)

    # Calcul de la DPF-star
    dp = dpf.depth_potential_function(mesh, Kmean)

    # Sauvegarde de la DPF-star
    save_dpf(dp, name_subject)  # Fonction qui doit exister pour la sauvegarde

    # Affichage si l'argument --display est spécifié
    if display:
        try:
            call_visuallizer(mesh_path, os.path.join(cfg.WD_FOLDER, name_subject, cfg.DPF))  # Fonction qui doit exister pour la visualisation
        except Exception as e:
            print("Erreur lors de la visualisation :", e)

if __name__ == "__main__":
    # Parse des arguments de la ligne de commande
    parser = argparse.ArgumentParser(description="Calculer et sauvegarder la dpf d'un maillage.")
    parser.add_argument("mesh_path", type=str, help="Chemin vers le fichier maillage .gii")
    parser.add_argument("--curvature", type=str, help="Chemin vers la courbure du maillage", default=None)
    parser.add_argument("--display", action="store_true", help="Utiliser --display pour afficher le résultat")
    args = parser.parse_args()

    # Appel de la fonction principale avec les arguments
    main(args.mesh_path, curvature=args.curvature, display=args.display)