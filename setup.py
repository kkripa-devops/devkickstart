from setuptools import setup, find_packages

setup(
    name='devkickstart',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'devkickstart': ['templates/**/*']
    },
    entry_points={
        'console_scripts': [
            'devkickstart=devkickstart.devkickstart:main',
        ],
    },
)
