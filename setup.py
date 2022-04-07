from setuptools import setup

setup(
    name = 'hbs',
    description = 'Code to accompany the paper "Saving proof-of-work by hierarchical block structure: Bitcoin 2.0?"',
    author = 'Qui Somnium',
    author_email = 'Qui.Somnium@tuta.io',
    license = 'MIT',
    classifiers = [
        'Programming Language :: Python :: 3.9',
    ],
    keywords = 'Blockchain PoW Bitcoin Scaling Finance',
    install_requires = ['numpy', 'scipy', 'pandas', 'hdfs', 'tables', 'matplotlib', 'blockchain_parser'],
)