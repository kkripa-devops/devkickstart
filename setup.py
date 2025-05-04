<<<<<<< HEAD
# Copyright (c) 2025 Radhakrishnan Krishna Kripa
# Licensed under the MIT License

=======
>>>>>>> f6bee0a86908175272c6e737d111f233e2686de6
from setuptools import setup, find_packages

setup(
    name='devkickstart',
    version='0.1',
    packages=find_packages(include=['devkickstart_module', 'devkickstart_module.*']),
    include_package_data=True,
    package_data={
        'devkickstart_module': ['templates/**/*']
    },
    entry_points={
        'console_scripts': [
            'devkickstart=devkickstart_module.devkickstart:main',
        ],
    },
)
