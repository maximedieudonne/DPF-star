# DPF-STAR Repository

[![DOI](https://zenodo.org/badge/887228134.svg)](https://doi.org/10.5281/zenodo.14163623)


## Introduction
This repository contains the code associated with the paper: **"New Scale-Invariant Sulcal Depth Measure: A Response to the Conceptual and Methodological Problems of Sulcal Depth Estimation."** 

The code here provides tools to compute curvature and a novel DPF-STAR depth measure for brain surface meshes, addressing limitations in traditional sulcal depth estimation methods.

## Table of Contents  
1. [Installation](#installation) 
2. [Repository Organization](#organization) 
3. [Worspace Configuration](#configuration)
4. [How to use the App](#app)  
5. [Data and Scripts](#scripts)


<a name="installation"/>

## Installation
First, fork and Clone this repository:
```bash
git clone https://github.com/your-username/DPF-star
cd DPF-star
```
Then, follow the installation steps to set up and run this project on your machine.

### Installation Steps

#### Option 1 : automatic installation of the conda env (recommended)

1. Make sure **Conda** is installed on your machine. You can download Miniconda or Anaconda here: [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)  

```
2. Run the installation script:
```bash
./install.sh
```
This script will:
* Create a Conda environment using the environment.yml file.
* Activate the newly created environment.

If the script does not execute, make sure it is executable:
 ```bash
chmod +x install.sh
```
#### Option 2 : manual installation of the conda env
If you prefer not to use the script, here are the manual steps:
1. Create the Conda environment from the environment.yml file:
```bash
conda env create -f environment.yml
```
2. Activate the Conda environment:
```bash
conda activate your_project_name
```

### Option 3 : editable mode.

If you want to contribute to this repository, you can install all the dependencies and the application in editable mode using 'pip install -e .'. This command installs the package as a symbolic link, allowing you to test changes locally as you develop without needing to reinstall the package. For more details about editable installations, see [the pip documentation on editable installs](https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs).

1. Navigate to the project root directory:
```bash
cd path/to/DPF-STAR
```
2. Upgrade pip and setuptools:
```bash
pip install --upgrade setuptools pip
```
3. Install the package in development mode:
```bash
pip install -e .
```
You can run pip install -e . after creating either a Python virtual environment or a Conda environment. While Conda environments are larger in size, they offer more robust dependency management and support for non-Python packages. For maximum flexibility, it is recommended to create and activate a Conda environment first, then use pip install -e . to install the application in editable mode, allowing you to develop and test changes while benefiting from Conda's comprehensive package management.

<a name="organization"/>

## Repository Organization
There are 2 main files in this repo : 
(1) app : functions you can run on command line and allow you to use the dpf-star method for your own studies.
(2) research : the scripts used for the different experience introduced in the article.
The repository is organized as follows:

```plaintext
DPF-STAR/
│ 
├── app/                       # Application for using the DPF-STAR method on custom data
│   ├── fonctions/             # fonctions used by the app commands
│   ├── compute_curvature.py   # command for computing mesh curvature
│   ├── compute_dpfstar.py     # command for computing the DPF-STAR depth
│   └── visualiser.py          # command for visualizing textures on meshes
│ 
├── research/                  # Scripts and used in experiments for the paper
│   ├── scripts/
│   │    ├── scripts_EXP1.py
│   │    ├── scripts_EXP2.py
│   │    ├── scripts_EXP3.py
│   │    └── scripts_EXP4.py
│   ├── data/
│   └── toolrs/
│ 
└── config.py                   # file for config local path
```

<a name="configuration"/>

## Workspace Configuration
Before running the app, adjust the workspace configuration to ensure smooth operation:

1. Update `.vscode/settings.json` with the correct project root directory path.
2. Update `.vscode/launch.json` with the correct project root directory path.
3. Adjust the `config.py` file to point to the correct project root directory.

<a name="app"/>

## How to Use the App

### Usage Overview
The app allows you to:
- Compute the **curvature** of a mesh.
- Calculate the **DPF depth** of a mesh.
- Calculate the **DPF-STAR depth** of a mesh.
- Quickly visualize the **texture** applied on the mesh.

### Commands

#### 1. Compute Curvature
To compute the curvature of a mesh, run:
```bash
python -m app.compute_curvature {path/to/your/mesh} --display
```
Replace `{path/to/your/mesh}` with the actual path to your mesh file.
- If the `--display` argument is added, the script will automatically run the dash code for visualising the mesh with the curvature texture.

Here a screenshot of what you get with the example mesh : 
<img src="./images/display_curvature.png" alt="curvature display" width="500"/>

#### 2. Compute DPF Depth
To calculate the DPF depth of a mesh, use:
```bash
python -m app.compute_dpf {path/to/your/mesh} --curvature {curvature/path} --display
```
- If the `--curvature` argument is not specified, the script will look for a curvature file in the corresponding folder or compute it if necessary.
- If the `--display` argument is added, the script will automatically run the dash code for visualising the mesh with the dpf texture.

Here a screenshot of what you get with the example mesh : 
<img src="./images/display_dpf.png" alt="dpf display" width="500"/>

#### 3. Compute DPF-STAR Depth
To calculate the DPF-STAR depth of a mesh, use:
```bash
python -m app.compute_dpfstar {path/to/your/mesh} --curvature {curvature/path} --display
```
- If the `--curvature` argument is not specified, the script will look for a curvature file in the corresponding folder or compute it if necessary.
- If the `--display` argument is added, the script will automatically run the dash code for visualising the mesh with the dpf-star texture.

Here a screenshot of what you get with the example mesh : 
<img src="./images/display_dpfstar.png" alt="dpfstar display" width="500"/>

#### 4. Visualize Textures
To visualize textures on a mesh, use the following command:
```bash
python -m app.visualiser {path/to/your/mesh} --texture {texture/path} 
```
Replace `{path/to/your/mesh}` and `{texture/path}` with the paths to your mesh and texture files, respectively.

you will get :
```bash
Dash is running on http://XXX.X.X.X:XXXX/

 * Serving Flask app 'visualizer'
 * Debug mode: on
```
simply copy paste the url http://XXX.X.X.X:XXXX/ is your internet browser

<a name="scripts"/>

# Data and scripts of the paper

## 1. Scripts Experience 1.
1. [Dataset](#dataset1)
2. [Computation of different sulcal depth](#depth)
   1. [SULC Computation for Dataset EXP1](#sulc)
   2. [DPF 0.03 and DPF* Computation for Dataset EXP1](#dpf)
3. [Manual labelisation of the cortical structures](#manuallabel)
   1. [Crest lines](#crest)
   2. [fundi lines](#fundi)
   3. [direction lines](#wall)
5. [Computation of quantitaiv metric for sulcal depth](#metrics)
   1. [Computation of diff between fundi and crest](#difffundicrest)
   2. [Computation of std crest](#stdcrest)
   3. [Computation of angular deviation](#angular)
       1. [computation of depth gradient](#depthgradient)
       2. [compuation of diffusion map](#diffusion)
       3. [computation of gradient diffusion map](#gradientdiffusion)


<a name="dataset1"/>

### Dataset 1

The informations relative to the datasets are stored in the folder ./data/dataset_EXP1.csv
<img src="./images/screen_dataset_EXP1.png" alt="data EXP1" width="500"/>

<a name="depth"/>

### Computation of different sulcal depth for each subject of the dataset 1

<a name="sulc"/>

#### Computation of SULC

It provides a pipeline for processing and analyzing brain surface meshes and computing sulcal depth. The workflow consists of three main steps: mesh conversion, sulcal depth computation, and data post-processing.
Requirement : 
- **FreeSurfer**: For mesh conversion.
- **MIRTK**: For sulcal depth computation on scaled meshes.

1. **Mesh Conversion**
Purpose: Convert white matter surface meshes into a format compatible with FreeSurfer tools.
- Input files: `.surf.gii` meshes located in the `meshes/` directory.
- Tool used: `mris_convert` from FreeSurfer.
- Output files: Converted meshes saved in the `mris_meshes/` directory.
- Batch processing is supported for multiple subjects.

2. **Sulcal Depth Computation**
Purpose: Compute sulcal depth across multiple scales using `mirtk` deformation tools.
- Input files: Preprocessed scaled meshes for each subject.
- Tool used: `mirtk deform-mesh` with the `-track SulcalDepth` option.
- Output files: Sulcal depth `.gii` files saved in scale-specific subdirectories.
- Scales include predefined resolutions, enabling multi-scale analysis.

3. **Sulcal Depth Extraction**
Purpose : Prepare sulcal depth data for analysis by normalizing and saving processed values.
- Input files: Sulcal depth `.gii` files generated in the previous step.
- Operations performed:
  - Extract sulcal depth values from the data.
  - Inverse the sign of the values to ensure positivity.
- Output files: Processed `.gii` files saved in the `sulc/` subdirectory for each subject.


<a name="dpf"/>

#### DPF 0.03 and DPF* Computation for Dataset EXP1

The `dpf*` (Depth Potential Function) was computed for the dataset **EXP1** using a Python script that leverages the `slam` package. This process calculates the depth potential function values across a range of alpha values, including the primary setting of `alpha = 0.03`. Below is a summary of the methodology:

1. **Dataset and Input Data**:
   - The dataset information was loaded from a CSV file (`dataset_EXP1.csv`) containing:
     - `participant_id` (subject ID),
     - `session_id` (session ID),
     - `dataset` (dataset identifier).
   - For each subject and session, the following input files were used:
     - Surface mesh: `sub-<participant_id>_ses-<session_id>_hemi-L_space-T2w_wm.surf.gii`
     - Curvature files: `K1.gii` and `K2.gii`
   - All input files are stored in the `data_EXP1` directory.

2. **Curvature Processing**:
   - The principal curvatures \( K1 \) and \( K2 \) were averaged to compute the mean curvature:
     ```python
     curv = 0.5 * (K1 + K2)
     ```

3. **DPF and DPFstar Computation**:
   - The `depth.depth_potential_function` function from the `slam` package is used to compute the depth potential function (DPF) for the surface mesh:
   - \( \text{Alpha: } 0.03 \)
   - The computed DPF values are negated to produce the `dpf*`:
     ```python
     dpf = depth.depth_potential_function(mesh, curv, [0.03])
     dpf_star = -dpf[0]
     ```
   - The `depth.depth_potential_function` function from the `slam` package was used to compute the depth potential function (DPF) for each mesh. This function takes into account:
     - The curvature,
     - A predefined set of alpha values:
       ```python
       alphas = [0, 0.0001, 0.0005, 0.001, 0.003, 0.005, 0.01, 0.03, 0.05, 0.5]
       ```
   - For consistency, the values were negated to obtain the `dpf*`:
     ```python
     dpf = [-dp for dp in dpf_temp]
     ```


5. **Output**:
   - The computed DPF* values were saved as `.gii` files for each subject and session in the directory:
     ```
     data_EXP1/result_EXP1/depth/<subject_session>/dpf/
     ```
   - The alpha values used for computation were saved as a CSV file (`alpha.csv`) in the same directory.





