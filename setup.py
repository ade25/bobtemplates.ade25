from setuptools import find_packages
from setuptools import setup

version = '1.0.0'

setup(
    name='bobtemplates.ade25',
    version=version,
    description="Templates for ade25 projects.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    keywords='',
    author='ade25',
    author_email='info@ade25.de',
    url='https://github.com/ade25/bobtemplates.ade25',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    extras_require={
        'test': [
            'coverage',
            'nose',
            'nose-selecttests',
            'scripttest',
            'unittest2',
        ]
    },
    entry_points={},
)
