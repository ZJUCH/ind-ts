import indts
from setuptools import setup, find_packages

DISTNAME = 'ind-ts'
VERSION = indts.__version__

setup(
    name=DISTNAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'scikit-learn',
        'matplotlib',
    ],
    author='zjuch',
)
