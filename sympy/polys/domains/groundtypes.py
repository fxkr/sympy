"""Ground types for various mathematical domains in SymPy. """

HAS_GMPY = True

try:
    import gmpy
except ImportError:
    HAS_GMPY = False
else:
    try:
        int(gmpy.mpz(2**256))
    except OverflowError:
        from warnings import warn
        warn("gmpy library is too old, can't take advantage of it")
        HAS_GMPY = False

from __builtin__ import (
    int     as PythonIntegerType,
    float   as PythonRealType,
    complex as PythonComplexType,
)

from pythonrationaltype import PythonRationalType

def python_factorial(n):
    from sympy.functions.combinatorial.factorials import factorial
    return int(factorial(n))

from sympy.core.numbers import (
    igcdex     as python_gcdex,
    igcd       as python_gcd,
    ilcm       as python_lcm,
)

from sympy import (
    Float     as SymPyRealType,
    Integer  as SymPyIntegerType,
    Rational as SymPyRationalType,
)

if HAS_GMPY:
    from gmpy import (
        mpz    as GMPYIntegerType,
        mpq    as GMPYRationalType,
        fac    as gmpy_factorial,
        numer  as gmpy_numer,
        denom  as gmpy_denom,
        gcdext as gmpy_gcdex,
        gcd    as gmpy_gcd,
        lcm    as gmpy_lcm,
        sqrt   as gmpy_sqrt,
    )
else:
    class GMPYIntegerType(object):
        def __init__(self, obj):
            pass

    class GMPYRationalType(object):
        def __init__(self, obj):
            pass

    gmpy_factorial   = None
    gmpy_numer       = None
    gmpy_denom       = None
    gmpy_gcdex       = None
    gmpy_gcd         = None
    gmpy_lcm         = None
    gmpy_sqrt        = None

from sympy.mpmath import (
    mpf as MPmathRealType,
    mpc as MPmathComplexType,
    mpi as MPmathIntervalType,
)

from sympy.mpmath.libmp.libmpf import isqrt

def python_sqrt(a):
    return int(isqrt(a))
