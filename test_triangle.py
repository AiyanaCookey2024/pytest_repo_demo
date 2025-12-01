from triangle import area_of_a_triangle
from pytest import approx

def test_float_values_exact():
    assert area_of_a_triangle(2, 3) == 3

def test_float_values_approx():
    assert area_of_a_triangle(3.4556, 8.3567) == approx(14.43, rel=1e-3)