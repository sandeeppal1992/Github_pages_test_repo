#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
#from ..utils.typevars import TNum, TPoint, TState

from Github_pages_test_repo.utils.typevars import TNum, TPoint, TState#, TRigidBody
from Github_pages_test_repo.utils import utils
#from Github_pages_test_repo.utils.errors import SimulationError
from Github_pages_test_repo.utils import errors



class RigidBody:
    """
    Base class for the rigid body simulation.

    Methods
    -------
    get_rotation_matrix()
    get_mass()
    get_moment()
    get_current_shape()
    get_shape()
    get_bounding_box()
    get_bounding_circle()
    get_position()
    get_heading()
    get_velocities()
    get_current_state()
    set_current_state()
    step_state()
    reset_state()
    get_previous_state()
    contains_point()
    intersects()
    point_on_boundary()
    in_contact()
    get_contact_point()
    get_results()
    plot_results()

    """

    def __init__(self,
                 mass: TNum,
                 moment: TNum,
                 shape: list[TPoint,],# ...],
                 initial_state: TState = (0., 0., 0., 0., 0., 0.,),
                 ) -> None:
        self.mass = mass
        self.moment = moment
        self.shape = shape
        self.initial_state = initial_state
    # def __init__(self,
    #              ) -> None:
        """
        Parameters
        ----------
        mass : TNum
            mass of the rigid body in kg
        moment : TNum
            moment of inertia of the rigid body in kg*m^2
        shape: list[TPoint, ...]
            shape of the rigid body, given by points (in meter) defining vertices of a convex polygone
            in clockwise order.
        initial_state: TState
            bodies initial state in bodies frame of reference as (x, y, psi, u, v, r) being
            (x-position / m, y-position / m, heading / rad, x-velocity / m/s, y-velocity / m/s, rotation rate / rad/s),
            heading being in [-pi,pi] with 0 being true North (optional, default is all 0)
        """
        pass
    
    def get_rotation_matrix(self,
                             ) -> np.ndarray:
        """
        Get the rotation matrix between the inertial frame of reference
        and the local frame of the current state.

        Returns
        -------
        np.ndarray
             3x3 numpy array representation of the rotation matrix
        """
        pass
    
    def get_mass(self,
                 ) -> TNum:
        """
        Get the body's mass.

        Returns
        -------
        TNum
             Body's mass in kg
        """
        pass
    
    def get_moment(self,
                   ) -> TNum:
        """
        Get the body's moment of inertia (along yaw/z-axis).

        Returns
        -------
        TNum
             body's moment in kg*m^2
        """
        pass
    
    def get_current_shape(self,
                          ) -> list[TPoint,]: #...]:
        """
        Get the body's shape at its current pose.

        Returns
        -------
        list[TPoint, ...]
             list of points (in meter) making up body's shape in current pose, in clockwise order
        """
        pass
    
    def get_shape(self,
                  ) -> list[TPoint, ]:#...]:
        """
        Get the body's shape at relative to it's center of gravity.

        Returns
        -------
        list[TPoint, ...]
             list of points (in meter) making up body's shape relative to it's center of gravity, in clockwise order
        """
        pass
    
    def get_bounding_box(self,
                         ) -> list[TPoint, TPoint, TPoint, TPoint]:
        """
        Get the bounding box of the body's shape in current pose.

        Returns
        -------
        list[TPoint, TPoint, TPoint, TPoint]
             list of points making up bounding box as [upper left, upper right, lower right, lower left] in meter
        """
        pass

    def get_bounding_circle(self,
                            ) -> list[TPoint, TNum]:
        """
        Get the bounding circle of the body's shape in current pose.

        Returns
        -------
        list[TPoint, TNum]
             list containing the centre's coordinates and the radius in meter
        """
        pass
    
    def get_position(self,
                     ) -> TPoint:
        """
        Get the body's current position.

        Returns
        -------
        TPoint
             body's current position in meter
        """
        pass
    
    def get_heading(self,
                    ) -> TNum:
        """
        Get the body's current heading in rad.

        Returns
        -------
        TNum
             body's current heading in radians
        """
        pass
    
    def get_velocities(self,
                       ) -> tuple[TNum, TNum, TNum]:
        """
        Get the body's current linear and angular velocities in local frame of reference.

        Returns
        -------
        tuple[TNum, TNum, TNum]
             Body's current velocities as (u, v, r) in (m/s, m/s, rad/s)
        """
        pass
    
    def get_current_state(self,
                          ) -> TState:
        """
        Get the body's current state in local frame of reference.


        Returns
        -------
        TState
             Body's current state as (x, y, psi, u, v, r) in (m, m, rad, m/s, m/s, rad/s)
             heading being in [-pi,pi] with 0 being true North

        """
        pass
        
    def set_current_state(self,
                          state: TState,
                          ) -> None:
        """
        Set the body's current state in local frame of reference.

        Parameters
        ----------
        state : TState
            state to set current state to as (x, y, psi, u, v, r) in (m, m, rad, m/s, m/s, rad/s)
            heading being in [-pi,pi] with 0 being true North

        """
        pass

    def step_state(self, 
                   delta_time: TNum,
                   force_input: np.ndarray,
                   ) -> None:
        """
        Advance the simulation for one timestep.

        Parameters
        ----------
        delta_time : TNum
            size of the timestep in seconds
        force_input : np.ndarray
            3x1 numpy array of forces acting on body over timestep in Newton

        """
        pass
    
    def reset_state(self,
                    new_initial_state: TState | None = None,
                    ) -> None:
        """
        Reset all previous simulation steps.

        Parameters
        ----------
        new_initial_state : TState | None
            new initial state after reset (optional, default = None -> use previous)
            as (x, y, psi, u, v, r) in (m, m, rad, m/s, m/s, rad/s)
            heading being in [-pi,pi] with 0 being true North

        """
        pass

    def get_previous_state(self,
                           ) -> TState:
        """
        Get the body's state in local frame of reference at previous timestep.

        Returns
        -------
        TState
            body's previous state as (x, y, psi, u, v, r) in (m, m, rad, m/s, m/s, rad/s)
            heading being in [-pi,pi] with 0 being true North

        Raises
        ------
        SimulationError
            if there is no previous state available

        """
        pass

    def contains_point(self, 
                       point: TPoint,
                       ) -> bool:
        """
        Determines if current shape contains a given point.

        Parameters
        ----------
        point : TPoint
            point in meters to check the shape against


        Returns
        -------
        bool
             indicating if the point in inside current shape

        """
        pass
    
    # def intersects(self,
    #                body: TRigidBody,
    #                ) -> bool:
        """
        Determines if the current shapes of this and another rigid body intersect.

        Parameters
        ----------
        body : TRigidBody
            body to check the shape against

        Returns
        -------
        bool
             indicating if the two shapes intersect
        """
        pass
        
    def point_on_boundary(self,
                          point: TPoint,
                          ) -> bool:
        """
        Determines if a point is on the boundary of the body's current shape.
        (technically if distance is float-close to 0)

        Parameters
        ----------
        point : TPoint
            point in meters to check shape against

        Returns
        -------
        bool
             indicating if the point is on the shapes boundary
        """
        pass
    
    # def in_contact(self,
    #                body: TRigidBody,
    #                ) -> bool:
        """
        Determines if this body's shape is in contact with another bodies shape.
        (technically if distance is float-close to 0)

        Parameters
        ----------
        body : TRigidBody
            body to check the shape against

        Returns
        -------
        bool
             indicating if the two shapes/bodies are in contact
        """
        pass
    
    # def get_contact_point(self,
    #                       body: TRigidBody,
    #                       ) -> TPoint | None:
        """
        Determines the contact point between this body's shape and another bodies shape, if there is any.
        (technically: the point of smallest distance, where the distance is float-close to 0)

        Parameters
        ----------
        body : TRigidBody
            body to check the shape against

        Returns
        -------
        TPoint | None:
            contact point in meter if there is one or None otherwise
        """
        pass
    
    def get_results(self,
                    ) -> dict[str, np.ndarray]:
        """
        Get a dictionary of timestamps and state variables of all simulation steps so far.

        Returns
        -------
        dict[str, np.ndarray]:
            dictionary with state variable names (x, y, psi, u, v, r) being
            (x-position / m, y-position / m, heading / rad being in [-pi,pi] with 0 being true North,
            x-velocity / m/s, y-velocity / m/s, rotation rate / rad/s), as keys and
            their values over time in a numpy array

        """
        pass

    def plot_results(self,
                     ) -> None:
        """
        Create a single matplotlib plot with subplot of all state variables over time.
        """
        pass
