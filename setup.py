from setuptools import setup

setup(
    name='devkickstart',
    version='0.2',
    py_modules=['devkickstart', 'utils'],
    entry_points={
        'console_scripts': [
            'devkickstart=devkickstart:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['templates/**/*'],
    },
)
