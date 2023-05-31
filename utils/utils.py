#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper functions to use for convenience.
"""

__author__ = "Marius Seidl"

import math

from . import constants as const


def is_close(x: float,
             y: float,
             ) -> bool:
    """
    Determines if two floats are close based on tolerances.
    Use for robust float equality comparison.

    Parameters
    ----------
    x : float
        First float to compare
    y : float
        Second float to compare

    Returns
    -------
    bool
         A boolean indicating if x and y are close
    """

    return math.isclose(x, y, rel_tol=const.FLOAT_EQ_REL_TOL, abs_tol=const.FLOAT_EQ_ABS_TOL)
