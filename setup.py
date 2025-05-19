from setuptools import setup, find_packages

setup(
    name='et772_python_pip',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "et772_python_pip = et772_python_pip.main:main",
        ]
    }
)