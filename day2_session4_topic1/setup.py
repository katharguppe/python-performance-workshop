# setup.py
# run python setup.py build_ext --inplace

from setuptools import setup
from Cython.Build import cythonize

extensions = [
    'sum_cython.pyx',
    'distance_cython.pyx',
    'array_sum_cython.pyx',
    'parallel_sum_cython.pyx'
]

setup(
    name='Cython Benchmarks',
    ext_modules=cythonize(extensions, language_level=3),
    zip_safe=False,
)