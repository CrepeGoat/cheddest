import pytest
from intervals import core

from itertools import product
import operator
from math import inf


@pytest.mark.parametrize('div', [
    core.NumberLineDivider(1, False),
    core.NumberLineDivider(3.2, True),
])
def test_NumberLineDivider_print(div):
    repr(div)
    str(div)


@pytest.mark.parametrize('value, expt_result', [
    (core.NumberLineDivider(1, False), core.NumberLineDivider(1, False)),
    (core.NumberLineDivider(2, True), core.NumberLineDivider(2, True)),
    (core.NumberLineDivider(3, None), core.NumberLineDivider(3, None)),
    (4, core.NumberLineDivider(4, False)),
])
def test_NumberLineDivider_as_divider(value, expt_result):
    result = core.NumberLineDivider.as_divider(value)
    assert result.value == expt_result.value
    assert result.on_pos_side == expt_result.on_pos_side


@pytest.mark.parametrize('value, expt_result', [
    (core.NumberLineDivider(1, False), 1),
    (core.NumberLineDivider(2, True), 2),
    (core.NumberLineDivider(3, None), 3),
    (4, 4),
])
def test_NumberLineDivider_as_value(value, expt_result):
    assert core.NumberLineDivider.as_value(value) == expt_result


@pytest.mark.parametrize('lhs, rhs, op, expt_result', [
    (core.NumberLineDivider(1, False), 2, operator.lt, True),
    (core.NumberLineDivider(1, False), 2, operator.gt, False),
    (core.NumberLineDivider(1, False), 2, operator.le, True),
    (core.NumberLineDivider(1, False), 2, operator.ge, False),
    (core.NumberLineDivider(1, False), 2, operator.eq, False),

    (core.NumberLineDivider(1, False), 0.1, operator.lt, False),
    (core.NumberLineDivider(1, False), 0.1, operator.gt, True),
    (core.NumberLineDivider(1, False), 0.1, operator.le, False),
    (core.NumberLineDivider(1, False), 0.1, operator.ge, True),
    (core.NumberLineDivider(1, False), 0.1, operator.eq, False),

    (core.NumberLineDivider(1, False), 1, operator.lt, True),
    (core.NumberLineDivider(1, False), 1, operator.gt, False),
    (core.NumberLineDivider(1, False), 1, operator.le, True),
    (core.NumberLineDivider(1, False), 1, operator.ge, False),
    (core.NumberLineDivider(1, False), 1, operator.eq, False),

    (core.NumberLineDivider(1, True), 2, operator.lt, True),
    (core.NumberLineDivider(1, True), 2, operator.gt, False),
    (core.NumberLineDivider(1, True), 2, operator.le, True),
    (core.NumberLineDivider(1, True), 2, operator.ge, False),
    (core.NumberLineDivider(1, True), 2, operator.eq, False),

    (core.NumberLineDivider(1, True), 0.1, operator.lt, False),
    (core.NumberLineDivider(1, True), 0.1, operator.gt, True),
    (core.NumberLineDivider(1, True), 0.1, operator.le, False),
    (core.NumberLineDivider(1, True), 0.1, operator.ge, True),
    (core.NumberLineDivider(1, True), 0.1, operator.eq, False),

    (core.NumberLineDivider(1, True), 1, operator.lt, False),
    (core.NumberLineDivider(1, True), 1, operator.gt, True),
    (core.NumberLineDivider(1, True), 1, operator.le, False),
    (core.NumberLineDivider(1, True), 1, operator.ge, True),
    (core.NumberLineDivider(1, True), 1, operator.eq, False),

    (core.NumberLineDivider(-inf, False), 2, operator.lt, True),
    (core.NumberLineDivider(-inf, False), 2, operator.gt, False),
    (core.NumberLineDivider(-inf, False), 2, operator.le, True),
    (core.NumberLineDivider(-inf, False), 2, operator.ge, False),
    (core.NumberLineDivider(-inf, False), 2, operator.eq, False),

    (core.NumberLineDivider(inf, False), 0.1, operator.lt, False),
    (core.NumberLineDivider(inf, False), 0.1, operator.gt, True),
    (core.NumberLineDivider(inf, False), 0.1, operator.le, False),
    (core.NumberLineDivider(inf, False), 0.1, operator.ge, True),
    (core.NumberLineDivider(inf, False), 0.1, operator.eq, False),

    (core.NumberLineDivider(inf, False), inf, operator.lt, False),
    (core.NumberLineDivider(inf, False), inf, operator.gt, False),
    (core.NumberLineDivider(inf, False), inf, operator.le, True),
    (core.NumberLineDivider(inf, False), inf, operator.ge, True),
    (core.NumberLineDivider(inf, False), inf, operator.eq, True),

    (core.NumberLineDivider(-inf, True), 2, operator.lt, True),
    (core.NumberLineDivider(-inf, True), 2, operator.gt, False),
    (core.NumberLineDivider(-inf, True), 2, operator.le, True),
    (core.NumberLineDivider(-inf, True), 2, operator.ge, False),
    (core.NumberLineDivider(-inf, True), 2, operator.eq, False),

    (core.NumberLineDivider(inf, True), 0.1, operator.lt, False),
    (core.NumberLineDivider(inf, True), 0.1, operator.gt, True),
    (core.NumberLineDivider(inf, True), 0.1, operator.le, False),
    (core.NumberLineDivider(inf, True), 0.1, operator.ge, True),
    (core.NumberLineDivider(inf, True), 0.1, operator.eq, False),

    (core.NumberLineDivider(inf, True), inf, operator.lt, False),
    (core.NumberLineDivider(inf, True), inf, operator.gt, False),
    (core.NumberLineDivider(inf, True), inf, operator.le, True),
    (core.NumberLineDivider(inf, True), inf, operator.ge, True),
    (core.NumberLineDivider(inf, True), inf, operator.eq, True),

    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(-inf, False), operator.lt, False),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(-inf, False), operator.gt, False),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(-inf, False), operator.le, True),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(-inf, False), operator.ge, True),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(-inf, False), operator.eq, True),

    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(inf, True), operator.lt, True),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(inf, True), operator.gt, False),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(inf, True), operator.le, True),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(inf, True), operator.ge, False),
    (core.NumberLineDivider(-inf, True), core.NumberLineDivider(inf, True), operator.eq, False),
])
def test_NumberLineDivider_cmp(lhs, rhs, op, expt_result):
    assert op(lhs, rhs) == expt_result


@pytest.mark.parametrize('lhs, rhs, op, expt_result', [
    (
        core.NumberLineDivider(1, False), 2, operator.add,
        core.NumberLineDivider(3, False)
    ),
    (
        core.NumberLineDivider(1, False), 2, operator.sub,
        core.NumberLineDivider(-1, False)
    ),
    (
        2, core.NumberLineDivider(1, False), operator.add,
        core.NumberLineDivider(3, False)
    ),
    (
        2, core.NumberLineDivider(1, False), operator.sub,
        core.NumberLineDivider(1, True)
    ),
    (
        core.NumberLineDivider(1, True), 2, operator.add,
        core.NumberLineDivider(3, True)
    ),
    (
        core.NumberLineDivider(1, True), 2, operator.sub,
        core.NumberLineDivider(-1, True)
    ),
    (
        2, core.NumberLineDivider(1, True), operator.add,
        core.NumberLineDivider(3, True)
    ),
    (
        2, core.NumberLineDivider(1, True), operator.sub,
        core.NumberLineDivider(1, False)
    ),
    (
        core.NumberLineDivider(1, None), 2, operator.add,
        core.NumberLineDivider(3, None)
    ),
    (
        core.NumberLineDivider(1, None), 2, operator.sub,
        core.NumberLineDivider(-1, None)
    ),
    (
        2, core.NumberLineDivider(1, None), operator.add,
        core.NumberLineDivider(3, None)
    ),
    (
        2, core.NumberLineDivider(1, None), operator.sub,
        core.NumberLineDivider(1, None)
    ),

    (
        core.NumberLineDivider(1, False),
        core.NumberLineDivider(2, False),
        operator.add,
        core.NumberLineDivider(3, False),
    ),
    (
        core.NumberLineDivider(1, False),
        core.NumberLineDivider(2, False),
        operator.sub,
        core.NumberLineDivider(-1, None),
    ),
    (
        core.NumberLineDivider(1, False),
        core.NumberLineDivider(2, True),
        operator.add,
        core.NumberLineDivider(3, None),
    ),
    (
        core.NumberLineDivider(1, False),
        core.NumberLineDivider(2, True),
        operator.sub,
        core.NumberLineDivider(-1, False),
    ),
    (
        core.NumberLineDivider(1, True),
        core.NumberLineDivider(2, False),
        operator.add,
        core.NumberLineDivider(3, None),
    ),
    (
        core.NumberLineDivider(1, True),
        core.NumberLineDivider(2, False),
        operator.sub,
        core.NumberLineDivider(-1, True),
    ),
    (
        core.NumberLineDivider(1, True),
        core.NumberLineDivider(2, True),
        operator.add,
        core.NumberLineDivider(3, True),
    ),
    (
        core.NumberLineDivider(1, True),
        core.NumberLineDivider(2, True),
        operator.sub,
        core.NumberLineDivider(-1, None),
    ),
    (
        core.NumberLineDivider(1, False),
        core.NumberLineDivider(2, None),
        operator.add,
        core.NumberLineDivider(3, None),
    ),
    (
        core.NumberLineDivider(1, True),
        core.NumberLineDivider(2, None),
        operator.sub,
        core.NumberLineDivider(-1, None),
    ),
    (
        core.NumberLineDivider(1, None),
        core.NumberLineDivider(2, False),
        operator.add,
        core.NumberLineDivider(3, None),
    ),
    (
        core.NumberLineDivider(1, None),
        core.NumberLineDivider(2, True),
        operator.sub,
        core.NumberLineDivider(-1, None),
    ),
])
def test_NumberLineDivider_arithmetic(lhs, rhs, op, expt_result):
    result = op(lhs, rhs)
    assert result.value == expt_result.value
    assert result.on_pos_side == expt_result.on_pos_side


def test_NumberLineDivider_eps_literals():
    assert 3 + core.eps == core.NumberLineDivider(3, True)
    assert 1 - core.ε == core.NumberLineDivider(1, False)


#------------------------------------------------------------------------------

def demo_Interval_str():
    for b_lwr, b_upr, incl_lwr, incl_upr in product(
        range(10), range(10), (False, True), (False, True)
    ):
        itvl = core.Interval.from_values(b_lwr, b_upr, incl_lwr, incl_upr)
        #print(itvl._bounds)
        print(b_lwr, b_upr, incl_lwr, incl_upr, "\t->", itvl)

    return


@pytest.mark.parametrize('div', [
    core.Interval.from_values(*args)
    for args in product(range(3), range(3), (False, True), (False, True))
])
def test_NumberLineDivider_print(div):
    repr(div)
    str(div)


@pytest.mark.parametrize('itvl, result', [
    (core.Interval.from_values(1, 3, False, False), 2),
    (core.Interval.from_values(1, 3, True, False), 2),
    (core.Interval.from_values(1, 3, False, True), 2),
    (core.Interval.from_values(1, 3, True, True), 2),

    (core.Interval.from_values(2.0, 5), 3.0),
    (core.Interval.from_values(3, None), inf),
    (core.Interval.from_values(None, 3), inf),
    (core.Interval.from_values(2, 2), 0),
    (core.Interval.from_values(2, 1), 0),
])
def test_Interval_breadth(itvl, result):
    assert itvl.breadth() == result


@pytest.mark.parametrize('itvl, result', [
    (core.Interval.from_values(1, 3, False, False), True),
    (core.Interval.from_values(1, 3, True, False), True),
    (core.Interval.from_values(1, 3, False, True), True),
    (core.Interval.from_values(1, 3, True, True), True),

    (core.Interval.from_values(2.0, 5), True),
    (core.Interval.from_values(3, None), True),
    (core.Interval.from_values(None, 3), True),
    (core.Interval.from_values(2, 1), False),

    (core.Interval.from_values(2, 2, False, False), False),
    (core.Interval.from_values(2, 2, True, False), False),
    (core.Interval.from_values(2, 2, False, True), False),
    (core.Interval.from_values(2, 2, True, True), True),
])
def test_Interval_bool(itvl, result):
    assert bool(itvl) == result


@pytest.mark.parametrize('itvl1, itvl2, result', [
    # Must both be intervals (but does not fail if not so)
    (core.Interval.from_values(1, 2), 3, False),
    # Boundary values must be equal
    (
        core.Interval.from_values(1, 2),
        core.Interval.from_values(0, 4),
        False,
    ),
    (
        core.Interval.from_values(1, 2),
        core.Interval.from_values(3, 4),
        False,
    ),
    # Boundary inclusion must be the same
    (
        core.Interval.from_values(1, 2, False, True),
        core.Interval.from_values(1, 2, True, True),
        False,
    ),
    (
        core.Interval.from_values(1, 2, False, False),
        core.Interval.from_values(1, 2, False, True),
        False,
    ),
    (
        core.Interval.from_values(1, 2, False, False),
        core.Interval.from_values(1, 2, False, False),
        True,
    ),
    # Heterogeneous value types do not invalidate result
    (
        core.Interval.from_values(1, 2, True, True),
        core.Interval.from_values(1., 2., True, True),
        True,
    ),
    # Boundary inclusion is disregarded on unbounded ends
    (
        core.Interval.from_values(1, None, include_upper=False),
        core.Interval.from_values(1, None, include_upper=True),
        True,
    ),
    (
        core.Interval.from_values(None, 1, include_lower=False),
        core.Interval.from_values(None, 1, include_lower=True),
        True,
    ),
])
def test_Interval_eq(itvl1, itvl2, result):
    assert (itvl1 == itvl2) == result


@pytest.mark.parametrize('x, itvl, result', [
    # (Literal) Edge Cases - Left Bound
    (1, core.Interval.from_values(1, 3, False, False), False),
    (1, core.Interval.from_values(1, 3, False, True), False),
    (1, core.Interval.from_values(1, 3, True, False), True),
    (1, core.Interval.from_values(1, 3, True, True), True),
    # (Literal) Edge Cases - Right Bound
    (6.2, core.Interval.from_values(-1/2, 6.2, False, False), False),
    (6.2, core.Interval.from_values(-1/2, 6.2, False, True), True),
    (6.2, core.Interval.from_values(-1/2, 6.2, True, False), False),
    (6.2, core.Interval.from_values(-1/2, 6.2, True, True), True),
    # Zero-width cases
    (7, core.Interval.from_values(7, 7), False),
    (0, core.Interval.from_values(0, 0, True, True), True),
    (0, core.Interval.from_values(0, 0, False, True), False),
    (0, core.Interval.from_values(0, 0, True, False), False),
    (0, core.Interval.from_values(0, 0, False, False), False),
    # Misordered-bound cases
    (1, core.Interval.from_values(10, 0, True, True), False),
    (1, core.Interval.from_values(10, 0, False, True), False),
    (1, core.Interval.from_values(10, 0, True, False), False),
    (1, core.Interval.from_values(10, 0, False, False), False),
    (0, core.Interval.from_values(10, 0, True, True), False),
    (5, core.Interval.from_values(10, 0, True, True), False),
    (13, core.Interval.from_values(10, 0, True, True), False),
    (-4, core.Interval.from_values(10, 0, True, True), False),
    # Whatever cases
    (2, core.Interval.from_values(1, 10), True),
    (5, core.Interval.from_values(1, 10), True),
    (10, core.Interval.from_values(1, 10), False),
    (2, core.Interval.from_values(-4, 1), False),
])
def test_Interval_in(x, itvl, result):
    assert (x in itvl) == result


@pytest.mark.parametrize('itvl1, itvl2, result', [
    # Infinite-bound cases
    (core.Interval.from_values(3.4, 4.0), core.Interval.from_values(1, None), True),
    (core.Interval.from_values(-3.8, 7.5), core.Interval.from_values(None, 4), False),
    # Heterogeneous Type Cases
    (core.Interval.from_values(2.0, 5.3), core.Interval.from_values(1, 8), True),
    (core.Interval.from_values(-2.7, 5), core.Interval.from_values(1, 8.2), False),
    # Whatever cases
    (core.Interval.from_values(2, 5), core.Interval.from_values(1, 8), True),
    (core.Interval.from_values(1, 8), core.Interval.from_values(2, 5), False),
])
def test_Interval_subeqset(itvl1, itvl2, result):
    assert (itvl1 in itvl2) == result


@pytest.mark.parametrize('itvl1, itvl2, result', [
    # Infinite-bound cases
    (
        core.Interval.from_values(3.4, 4.0),
        core.Interval.from_values(1., None),
        core.Interval.from_values(3.4, 4.0),
    ),
    (
        core.Interval.from_values(-3.8, 7.5),
        core.Interval.from_values(None, 4.),
        core.Interval.from_values(-3.8, 4.),
    ),
    # Heterogeneous Type Cases
    (
        core.Interval.from_values(2.0, 5.3),
        core.Interval.from_values(1, 8),
        core.Interval.from_values(2.0, 5.3),
    ),
    (
        core.Interval.from_values(-2.7, 5),
        core.Interval.from_values(1, 8.2),
        core.Interval.from_values(1, 5),
    ),
    # Whatever cases
    (
        core.Interval.from_values(2, 5),
        core.Interval.from_values(1, 8),
        core.Interval.from_values(2, 5)
    ),
    (
        core.Interval.from_values(1, 8),
        core.Interval.from_values(2, 5),
        core.Interval.from_values(2, 5),
    ),
    # Boundary cases
    (
        core.Interval.from_values(1, 2, False, True),
        core.Interval.from_values(1, 2, True, True),
        core.Interval.from_values(1, 2, False, True),
    ),
    (
        core.Interval.from_values(1., 2., True, True),
        core.Interval.from_values(1., 2., True, False),
        core.Interval.from_values(1., 2., True, False),
    ),
    (
        core.Interval.from_values(1, 2, True, True),
        core.Interval.from_values(1., 2., False, False),
        core.Interval.from_values(1., 2., False, False),
    ),
])
def test_Interval_intersection(itvl1, itvl2, result):
    assert itvl1.intersection(itvl2) == result


def test_Interval_intersection_err():
    itvl = core.Interval.from_values(1, 2)
    with pytest.raises(TypeError):
        itvl.intersection(1.5)


#------------------------------------------------------------------------------

def test_DisjointInterval_init():
    itvl = core.DisjointInterval()
    assert itvl._bounds == ()


@pytest.mark.parametrize('pairs, expt_bounds', [
    ([], ()),
    ([(0, 1)], (0-core.eps, 1-core.eps)),
    ([(0, 0)], ()),
    ([(0, -1)], ()),

    (
        [(0, 1), (2.5, 3.5)],
        (0-core.eps, 1-core.eps, 2.5-core.eps, 3.5-core.eps),
    ),
    (
        [(2.5, 3.5), (0, 1)],
        (0-core.eps, 1-core.eps, 2.5-core.eps, 3.5-core.eps),
    ),
    ([(0, 1), (0.5, 3.5)], (0-core.eps, 3.5-core.eps)),
    ([(0, 1), (1, 3.5)], (0-core.eps, 3.5-core.eps)),
    (
        [(0, 1-core.eps), (1+core.eps, 3.5)],
        (0-core.eps, 1-core.eps, 1+core.eps, 3.5-core.eps),
    ),

    (
        [(None, 1), (2, None)],
        (-inf-core.eps, 1-core.eps, 2-core.eps, inf-core.eps)
    ),
])
def test_DisjointInterval_from_ranges(pairs, expt_bounds):
    itvl = core.DisjointInterval.from_ranges(*pairs)
    assert itvl._bounds == expt_bounds


@pytest.mark.parametrize('itvl, value, expt_result', [
    (core.DisjointInterval(), 0, False),

    (core.DisjointInterval.from_ranges((0, 1), (2, 3), (4, 5)), 0.5, True),
    (core.DisjointInterval.from_ranges((0, 1), (2, 3), (4, 5)), 1.5, False),
    (core.DisjointInterval.from_ranges((0, 1), (2, 3), (4, 5)), 1, False),
    (core.DisjointInterval.from_ranges((0, 1), (2, 3), (4, 5)), 2, True),

    (core.DisjointInterval.from_ranges((0, 1), (1, 2)), 1, True),
    (core.DisjointInterval.from_ranges((0, 1), (1+core.eps, 2)), 1, False),
])
def test_DisjointInterval_contains(itvl, value, expt_result):
    assert (value in itvl) == expt_result


@pytest.mark.parametrize('itvl, expt_result', [
    (core.DisjointInterval(), 0),
    (core.DisjointInterval.from_ranges((0, 1)), 1),
    (core.DisjointInterval.from_ranges((0, 1+core.eps)), 1),
    (core.DisjointInterval.from_ranges((0, 1), (2, 3), (4, 5)), 3),
])
def test_DisjointInterval_breadth(itvl, expt_result):
    assert itvl.breadth() == expt_result


@pytest.mark.parametrize('itvl, expt_result', [
    (core.DisjointInterval(), False),
    (core.DisjointInterval.from_ranges((0, 0+core.eps)), True),
    (core.DisjointInterval.from_ranges((0, 1), (2, 3), (4, 5)), True),
])
def test_DisjointInterval_bool(itvl, expt_result):
    assert bool(itvl) == expt_result


def test_DisjointInterval_eq():
    assert core.DisjointInterval() == core.DisjointInterval()
    assert (
        core.DisjointInterval.from_ranges((0, 0))
        != core.DisjointInterval.from_ranges((0, 0+core.eps))
    )


@pytest.mark.parametrize('itvl1, itvl2, expt_result', [
    (
        core.DisjointInterval(),
        core.DisjointInterval(),
        core.DisjointInterval(),
    ),
    (
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((0, 1)),
    ),

    (
        core.DisjointInterval(),
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((0, 1)),
    ),
    (
        core.DisjointInterval.from_ranges((0, 2)),
        core.DisjointInterval.from_ranges((1, 3)),
        core.DisjointInterval.from_ranges((0, 3)),
    ),
    (
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((2, 3)),
        core.DisjointInterval.from_ranges((0, 1), (2, 3)),
    ),
    (
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((0+core.eps, 1+core.eps)),
        core.DisjointInterval.from_ranges((0, 1+core.eps)),
    ),

    (
        core.DisjointInterval.from_ranges((0, 2), (4, 6)),
        core.DisjointInterval.from_ranges((1, 5)),
        core.DisjointInterval.from_ranges((0, 6)),
    ),
])
def test_DisjointInterval_union(itvl1, itvl2, expt_result):
    assert itvl1.union(itvl2) == expt_result
    assert itvl2.union(itvl1) == expt_result


@pytest.mark.parametrize('itvl1, itvl2, expt_result', [
    (
        core.DisjointInterval(),
        core.DisjointInterval(),
        core.DisjointInterval(),
    ),
    (
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((0, 1)),
    ),

    (
        core.DisjointInterval(),
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval(),
    ),
    (
        core.DisjointInterval.from_ranges((0, 2)),
        core.DisjointInterval.from_ranges((1, 3)),
        core.DisjointInterval.from_ranges((1, 2)),
    ),
    (
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((2, 3)),
        core.DisjointInterval(),
    ),
    (
        core.DisjointInterval.from_ranges((0, 1)),
        core.DisjointInterval.from_ranges((0+core.eps, 1+core.eps)),
        core.DisjointInterval.from_ranges((0+core.eps, 1)),
    ),

    (
        core.DisjointInterval.from_ranges((0, 2), (4, 6)),
        core.DisjointInterval.from_ranges((1, 5)),
        core.DisjointInterval.from_ranges((1, 2), (4, 5)),
    ),
])
def test_DisjointInterval_intersection(itvl1, itvl2, expt_result):
    assert itvl1.intersection(itvl2) == expt_result
    assert itvl2.intersection(itvl1) == expt_result


if __name__ == "__main__":
    pytest.main()