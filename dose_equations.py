#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:54:18 2022

Equations and dgn values for tkinter

@author: DIDSR
"""

import numpy as np  
import pandas as pd 

import os

# Sarno polyenergetic and monoenergetic tables from published papers  
Sarno_mono_dgn = pd.read_csv(os.path.join(os.getcwd(), 'dose_table', 'Sarno_mono_dgn.txt'), sep = ' ')

Sarno_poly_dgn = pd.read_csv(os.path.join(os.getcwd(), 'dose_table', 'Sarno_poly_dgn.txt'), sep = ' ', index_col = 'HVL')

# monoenergetic dgnct equation 8th degree polynomial fitting 
sarno_dgnct = lambda a,b,c,d,e,f,g,h,E: (a*10**-14)* E**8 + (b*10**-12)*E**7 + (c*10**-10)*E**6 + (d*10**-8)*E**5 + (e*10**-6)*E**4 + \
                                        (f*10**-4)*E**3 + (g*10**-3)*E**2 + (h*10**-2)*E
# define equation for exposure per fluence
aa = -5.023290717769674e-6;
bb = 1.810595449064631e-7;
cc = 0.008838658459816926;
exposure_per_fluence = lambda E: (aa + bb *np.log(E) * np.log(E) + cc / E**2)**(-1) / 1000 * 0.1145

# Hernandez_hetero_dgn table
Hernandez_hetero_mono_dgn = pd.read_csv(os.path.join(os.getcwd(), 'dose_table', 'Hernandez_heterogeneous_dgn.txt'),sep=',',header=0)

# Sechopoulos dgn
Sechopoulos_poly_dgn = pd.read_csv(os.path.join(os.getcwd(), 'dose_table', 'Sechopoulos_dgn.txt'),sep=' ', header=None, index_col = 0) # index is diameter at chest wall (breast diameter)
Sechopoulos_poly_dgn.columns = ['Chest wall-to-nipple distance', '1%', '14.3%', '25%', '50%', '75%', '100%']
