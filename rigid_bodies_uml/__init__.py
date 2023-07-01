#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This modul provides objects to simulate single floating rigid
bodies in 2D according to the dynamics described in:

T. Fossen, Marine Control Systems: Guidance, Navigation
and Control of Ships, Rigs and Underwater Vehicles. Marine
Cybernetics, Trondheim, Norway, 2002.

Submodules:

    constraints - restrict movements of rigid bodies relative to each other
    disturbances - generate external disturbance forces acting rigid bodies
    propulsion - generate propulsion forces if attached to rigid bodies

Classes:

    RigidBody - base class
    FloatingBody - floating rigid body (including general hydrodynamics)
    UnactuatedBody - unactuated floating body with decoupled surge and sway-yaw hydrodynamics
    Ship - ship with decoupled surge and sway-yaw hydrodynamics

"""

__author__ = "Sandeep Pal"

__all__ = ['rigid_body_uml.py', 'generate_puml']
