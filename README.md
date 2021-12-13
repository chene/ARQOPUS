# Assessing Registration Quality for Orthogonal Procrustean Ultrasound Probe Calibration (ARQOPUS)

pronounced as \ˈär-kə-pəs

## Updated on December 13, 2021
## This is a work-in-progress. It is far from complete. Any suggestion is very much appreciated.

This GitHub repository contains Jupyter Notebook/Python codes for our MICCAI 2021 paper, which formulates a framework to assess the fitness of calibration for an instance of ultrasound probe calibration. If you find our MICCAI paper and codes below useful, please consider citing it using the following bibtex:
```
@InProceedings{CMP2021,
author        = "Chen, Elvis C. S. and Ma, Burton and Peters, Terry M.",
title         = "Quantitative Assessments for Ultrasound Probe Calibration",
booktitle     = "Medical Image Computing and Computer-Assisted Intervention -- MICCAI 2021",
editor        = "de Bruijne, Marleen and Cattin, Philippe C. and Cotin, St{\'e}phane and Padoy, Nicolas and Speidel, Stefanie and Zheng, Yefeng and Essert, Caroline",
year          = "2021",
publisher     = "Springer International Publishing",
address       = "Cham",
pages         = "363--372",
doi           = "10.1007/978-3-030-87202-1_35", }
```
You can download a copy of our MICCAI 2021 paper [here](https://doi.org/10.1007/978-3-030-87202-1_35).


#### This repository is structured as a set of Jupyter Notebook tutorial with Python codes.

Our MICCAI 2021 paper is quite dense due to MICCAI page limit. Many details are discussed in our prior work including:

**Solution to Procrustean point-fiducial registration with anisotropic scaling**:
```
@inproceedings{CMJ+2014,
author        = {Chen, Elvis C. S. and McLeod, A. Jonathan and Jayarathne, Uditha L. and Peters, Terry M.},
title         = {Solving for free-hand and real-time 3{D} ultrasound calibration with anisotropic orthogonal {P}rocrustes analysis},
volume        = {9036},
booktitle     = {Medical Imaging 2014: Image-Guided Procedures, Robotic Interventions, and Modeling},
editor        = {Yaniv, Ziv R. and Holmes, David R., III},
organization  = {International Society for Optics and Photonics},
publisher     = {SPIE},
pages         = {524--530},
year          = {2014},
doi           = {10.1117/12.2043080}, }
```

and **a line-based Target Registration Error estimation model accounting for heteroscedastic fiducial localization error**:
```
@ARTICLE{CPM2016,
author        = {Chen, Elvis C. S. and Peters, Terry M. and Ma, Burton},
journal       = {International Journal of Computer Assisted Radiology and Surgery}, 
title         = {Guided ultrasound calibration: where, how, and how many calibration fiducials}, 
year          = {2016},
volume        = {11},
number        = {6},
pages         = {889--898},
doi           = {10.1007/s11548-016-1390-7},
pmid          = {27038966}, }
```

This repository is organized as a set of Jupyter Notebook tutorials:
- [Basic Linear Algebra](https://github.com/chene/ARQOPUS/blob/main/BasicLinearAlgebra.ipynb)
- [Point Fiducial Registration, aka. Orthogonal Procrustes Analysis](https://github.com/chene/ARQOPUS/blob/main/point_Procrustes.ipynb)
- [Line Fiducial Registration](https://github.com/chene/ARQOPUS/blob/main/line_Procrustes.ipynb)
