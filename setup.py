from setuptools import setup, find_packages

setup(
    name='devkickstart',
    version='0.1',
    py_modules=['devkickstart', 'utils'],
    package_data={
        '': ['templates/*/*'],  # include all files in templates/**/*
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'devkickstart=devkickstart:main',
        ],
    },
)
