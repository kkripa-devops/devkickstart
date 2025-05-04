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
