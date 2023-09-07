"""
This type stub file was generated by pyright.
"""

"""Variation fonts interpolation models."""
__all__ = ["normalizeValue", "normalizeLocation", "supportScalar", "VariationModel"]
def nonNone(lst): # -> list[Unknown]:
    ...

def allNone(lst): # -> bool:
    ...

def allEqualTo(ref, lst, mapper=...): # -> bool:
    ...

def allEqual(lst, mapper=...): # -> bool:
    ...

def subList(truth, lst): # -> list[Unknown]:
    ...

def normalizeValue(v, triple, extrapolate=...): # -> float:
    """Normalizes value based on a min/default/max triple.

    >>> normalizeValue(400, (100, 400, 900))
    0.0
    >>> normalizeValue(100, (100, 400, 900))
    -1.0
    >>> normalizeValue(650, (100, 400, 900))
    0.5
    """
    ...

def normalizeLocation(location, axes, extrapolate=...): # -> dict[Unknown, Unknown]:
    """Normalizes location based on axis min/default/max values from axes.

    >>> axes = {"wght": (100, 400, 900)}
    >>> normalizeLocation({"wght": 400}, axes)
    {'wght': 0.0}
    >>> normalizeLocation({"wght": 100}, axes)
    {'wght': -1.0}
    >>> normalizeLocation({"wght": 900}, axes)
    {'wght': 1.0}
    >>> normalizeLocation({"wght": 650}, axes)
    {'wght': 0.5}
    >>> normalizeLocation({"wght": 1000}, axes)
    {'wght': 1.0}
    >>> normalizeLocation({"wght": 0}, axes)
    {'wght': -1.0}
    >>> axes = {"wght": (0, 0, 1000)}
    >>> normalizeLocation({"wght": 0}, axes)
    {'wght': 0.0}
    >>> normalizeLocation({"wght": -1}, axes)
    {'wght': 0.0}
    >>> normalizeLocation({"wght": 1000}, axes)
    {'wght': 1.0}
    >>> normalizeLocation({"wght": 500}, axes)
    {'wght': 0.5}
    >>> normalizeLocation({"wght": 1001}, axes)
    {'wght': 1.0}
    >>> axes = {"wght": (0, 1000, 1000)}
    >>> normalizeLocation({"wght": 0}, axes)
    {'wght': -1.0}
    >>> normalizeLocation({"wght": -1}, axes)
    {'wght': -1.0}
    >>> normalizeLocation({"wght": 500}, axes)
    {'wght': -0.5}
    >>> normalizeLocation({"wght": 1000}, axes)
    {'wght': 0.0}
    >>> normalizeLocation({"wght": 1001}, axes)
    {'wght': 0.0}
    """
    ...

def supportScalar(location, support, ot=..., extrapolate=..., axisRanges=...): # -> float:
    """Returns the scalar multiplier at location, for a master
    with support.  If ot is True, then a peak value of zero
    for support of an axis means "axis does not participate".  That
    is how OpenType Variation Font technology works.

    If extrapolate is True, axisRanges must be a dict that maps axis
    names to (axisMin, axisMax) tuples.

      >>> supportScalar({}, {})
      1.0
      >>> supportScalar({'wght':.2}, {})
      1.0
      >>> supportScalar({'wght':.2}, {'wght':(0,2,3)})
      0.1
      >>> supportScalar({'wght':2.5}, {'wght':(0,2,4)})
      0.75
      >>> supportScalar({'wght':2.5, 'wdth':0}, {'wght':(0,2,4), 'wdth':(-1,0,+1)})
      0.75
      >>> supportScalar({'wght':2.5, 'wdth':.5}, {'wght':(0,2,4), 'wdth':(-1,0,+1)}, ot=False)
      0.375
      >>> supportScalar({'wght':2.5, 'wdth':0}, {'wght':(0,2,4), 'wdth':(-1,0,+1)})
      0.75
      >>> supportScalar({'wght':2.5, 'wdth':.5}, {'wght':(0,2,4), 'wdth':(-1,0,+1)})
      0.75
      >>> supportScalar({'wght':3}, {'wght':(0,1,2)}, extrapolate=True, axisRanges={'wght':(0, 2)})
      -1.0
      >>> supportScalar({'wght':-1}, {'wght':(0,1,2)}, extrapolate=True, axisRanges={'wght':(0, 2)})
      -1.0
      >>> supportScalar({'wght':3}, {'wght':(0,2,2)}, extrapolate=True, axisRanges={'wght':(0, 2)})
      1.5
      >>> supportScalar({'wght':-1}, {'wght':(0,2,2)}, extrapolate=True, axisRanges={'wght':(0, 2)})
      -0.5
    """
    ...

class VariationModel:
    """Locations must have the base master at the origin (ie. 0).

    If the extrapolate argument is set to True, then values are extrapolated
    outside the axis range.

      >>> from pprint import pprint
      >>> locations = [ \
      {'wght':100}, \
      {'wght':-100}, \
      {'wght':-180}, \
      {'wdth':+.3}, \
      {'wght':+120,'wdth':.3}, \
      {'wght':+120,'wdth':.2}, \
      {}, \
      {'wght':+180,'wdth':.3}, \
      {'wght':+180}, \
      ]
      >>> model = VariationModel(locations, axisOrder=['wght'])
      >>> pprint(model.locations)
      [{},
       {'wght': -100},
       {'wght': -180},
       {'wght': 100},
       {'wght': 180},
       {'wdth': 0.3},
       {'wdth': 0.3, 'wght': 180},
       {'wdth': 0.3, 'wght': 120},
       {'wdth': 0.2, 'wght': 120}]
      >>> pprint(model.deltaWeights)
      [{},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0, 4: 1.0, 5: 1.0},
       {0: 1.0, 3: 0.75, 4: 0.25, 5: 1.0, 6: 0.6666666666666666},
       {0: 1.0,
        3: 0.75,
        4: 0.25,
        5: 0.6666666666666667,
        6: 0.4444444444444445,
        7: 0.6666666666666667}]
    """
    def __init__(self, locations, axisOrder=..., extrapolate=...) -> None:
        ...
    
    def getSubModel(self, items): # -> tuple[Self@VariationModel, Unknown] | tuple[VariationModel | Unknown, list[Unknown]]:
        ...
    
    @staticmethod
    def computeAxisRanges(locations): # -> dict[Unknown, Unknown]:
        ...
    
    @staticmethod
    def getMasterLocationsSortKeyFunc(locations, axisOrder=...): # -> (loc: Unknown) -> tuple[int, int, tuple[Unknown | Literal[65536], ...], tuple[Unknown, ...], tuple[Literal[-1, 1, 0], ...], tuple[Unknown, ...]]:
        ...
    
    def reorderMasters(self, master_list, mapping): # -> list[Unknown]:
        ...
    
    def getDeltas(self, masterValues, *, round=...): # -> list[Unknown]:
        ...
    
    def getDeltasAndSupports(self, items, *, round=...): # -> tuple[list[Unknown] | Unknown, Unknown | list[Unknown]]:
        ...
    
    def getScalars(self, loc): # -> list[float | Unknown]:
        ...
    
    @staticmethod
    def interpolateFromDeltasAndScalars(deltas, scalars): # -> None:
        ...
    
    def interpolateFromDeltas(self, loc, deltas): # -> None:
        ...
    
    def interpolateFromMasters(self, loc, masterValues, *, round=...): # -> None:
        ...
    
    def interpolateFromMastersAndScalars(self, masterValues, scalars, *, round=...): # -> None:
        ...
    


def piecewiseLinearMap(v, mapping):
    ...

def main(args=...): # -> None:
    """Normalize locations on a given designspace"""
    ...

if __name__ == "__main__":
    ...
