#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transformation du script en fonction
Jacob C. 2026-03-01
"""
# Importer les modules necessaires
import math


def billot(l_totale, l_sub, d_billot, rho_eau, pression):
    """
    Obsolète puisque on inscrit manuellement les valeurs
    # Definir les variables
    L_TOT_BILLOT = 11  #m
    L_SUBMERGEE_BILLOT = 8  #m
    D_BILLOT= 0.2  #m
    RHO_EAU = 998  #kg/m^3
    PRESSION = 24500 #Pa
    """

    # Calculs

    centre_flottaison= l_sub/2  # m
    vol_sub = l_sub*(d_billot/2)**2*math.pi
    vol_tot = l_totale*(d_billot/2)**2*math.pi
    fb = rho_eau*9.81*vol_sub
    rho_billot = (centre_flottaison*fb)/((l_totale/2)*9.81*vol_tot)
    poids_spec_billot = rho_billot*9.81
    w = rho_billot*9.81*vol_tot
    tension_corde= fb-w
    h = pression/(rho_eau*9.81)
    angle = (180/math.pi)*math.asin(h/l_sub)

    return poids_spec_billot, tension_corde, angle
