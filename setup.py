from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name='Cython Demo',
    ext_modules=cythonize("fib_cython.pyx"),
    include_dirs=[numpy.get_include()]
)