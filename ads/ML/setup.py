from setuptools import find_packages
from setuptools import setup

setup(
    name='ML assignments',
    version='0.0.1',
    include_package_data=True,
    author='shiekh Abdullah & Obaid sab & nobody special',
    description='Machine learning assignments for Applied Data',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'scikit-learn',
	    'textblob',
        'ipython'
    ],
    zip_safe=True)
