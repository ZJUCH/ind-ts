import ind-ts
from setuptools import setup, find_packages

DISTNAME = 'ind-ts'
VERSION = ind-ts.__version__

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
        'seaborn',
        'statsmodels',
        'tqdm',
        'joblib',
        'pyarrow',
        'xgboost',
        'lightgbm',
        'catboost'
    ],
    python_requires='>=3.6',
    author='zjuch',
)
