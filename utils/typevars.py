#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definitions of type variables for global usage throughout the package.
"""

__author__ = "Marius Seidl"


from typing import TypeVar, Type
import numpy as np

from rigid_bodies.rigid_body import RigidBody

# composed data types
TNum = TypeVar('TNum', int, float, np.float64)
TPoint = tuple[TNum, TNum]
T2Vector = tuple[TNum, TNum]
TState = tuple[TNum, TNum, TNum, TNum, TNum, TNum]

# types of class instances
TRigidBody = Type[RigidBody]
