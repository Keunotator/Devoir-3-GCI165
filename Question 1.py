#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python pour resoudre le probleme 2 du devoir 1 de GBA400 E2020

On a un billot de bois qui flotte dans l'eau et qui est aussi retenu par une corde
On cherche:
a. Le poids specifique du billot
b. La tension dans la corde
c. L’angle d’inclinaison du billot par rapport à l’horizontale, sachant que
la pression hydrostatique au point A est de 24.5 kPa (jaugee)

M-A Boucher, juin 2020 U. de Sherbrooke
"""
# Importer les modules necessaires
import math


# Definir les variables
L_TOT_BILLOT = 11  #m
L_SUBMERGEE_BILLOT = 8  #m
D_BILLOT= 0.2  #m
RHO_EAU = 998  #kg/m^3
PRESSION = 24500 #Pa



# Calculs

CENTRE_FLOTTAISON = L_SUBMERGEE_BILLOT/2 #m
VOL_SUB = L_SUBMERGEE_BILLOT*(D_BILLOT/2)**2*math.pi
VOL_TOT = L_TOT_BILLOT*(D_BILLOT/2)**2*math.pi
FB = RHO_EAU*9.81*VOL_SUB
RHO_BILLOT = (CENTRE_FLOTTAISON*FB)/((L_TOT_BILLOT/2)*9.81*VOL_TOT)
POIDS_SPEC_BILLOT = RHO_BILLOT*9.81
W = RHO_BILLOT*9.81*VOL_TOT
TENSION_CORDE = FB-W
H = PRESSION/(RHO_EAU*9.81)
angle = (180/math.pi)*math.asin(H/L_SUBMERGEE_BILLOT)
