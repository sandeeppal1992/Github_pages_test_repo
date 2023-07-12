import numpy as np
import pytest
from Github_pages_test_repo.rigid_bodies.rigid_body import RigidBody
#import rigid_body


# from ..utils.typevars import TNum, TPoint, TState, TRigidBody
# from ..utils import utils
# from ..utils.errors import SimulationError


# rigid = rigid_body(3,
#                  3,
#                  [2,3,4],# ...],
#                  (0., 0., 0., 0., 0., 0.,),)

#rigid = RigidBody(2.0,3.0,[2.0,3.0],[0., 0., 0., 0., 0., 0.])
rigid = RigidBody(2.0,3.0,[2.0,3.0],[0., 0., 0., 0., 0., 0.])

def test_get_rotation_matrix():
    assert rigid.get_rotation_matrix(3) == 0
    #pass

def test_get_mass():
    #assert RigidBody.RigidBody.get_mass() == TNum
    pass

def test_get_moment():
    #assert rigid_body.RigidBody.get_moment(self=rigid_body,) == TNum
    assert rigid.get_moment() == None
    #pass

def test_get_current_shape():
    #assert RigidBody.get_current_shape() == list[TPoint, ]
    pass

def test_get_shape():
    #assert RigidBody.get_shape() == list[TPoint, ]
    pass

def test_get_bounding_box():
    #assert RigidBody.get_bounding_box() == list[TPoint, TPoint, TPoint, TPoint]
    pass

def test_get_bounding_circle():
    #assert RigidBody.get_bounding_circle() == list[TPoint, TNum]
    pass

def test_get_position():
    #assert RigidBody.get_position() == TPoint
    pass

def test_get_heading():
    #assert RigidBody.get_heading() == TNum
    pass

def test_get_velocities():
    #assert RigidBody.get_velocities() == tuple[TNum, TNum, TNum]
    pass

def test_get_current_state():
    #assert RigidBody.get_current_state() == TState
    pass

def test_set_current_state():
    #assert RigidBody.set_current_state() == None
    pass

def test_step_state():
    #assert RigidBody.step_state() == None
    pass

def test_reset_state():
    #assert RigidBody.reset_state() == None
    pass

def test_get_previous_state():
    #assert RigidBody.get_previous_state() == TState
    pass

def test_contains_point():
    #assert RigidBody.contains_point() == bool
    pass

def test_intersects():
    #assert RigidBody.intersects() == bool
    pass

def test_point_on_boundary():
    #assert RigidBody.point_on_boundary() == bool
    pass

def test_in_contact():
    #assert RigidBody.in_contact() == bool
    pass

def test_get_contact_point():
    #assert RigidBody.get_contact_point() == TPoint | None
    pass

def test_get_results():
    #assert RigidBody.get_results() == dict[str, np.ndarray]
    pass

def test_plot_results():
    #assert RigidBody.plot_results() == None
    pass