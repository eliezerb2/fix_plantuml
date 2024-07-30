"""
Setup module for the fix_plantuml package.

This module configures the packaging and distribution of the fix_plantuml project.
It uses setuptools to package the project, specify dependencies, and create console scripts.

To create the distribution packages, run:
    python setup.py sdist bdist_wheel

To install the package locally, run:
    pip uninstall --y fix_plantuml
    pip install .

To install the package globally:
    select the global interpreter
    relaunch the terminal
    pip uninstall --y fix_plantuml
    pip install dist\fix_plantuml-0.x.y-py3-none-any.whl
"""

from setuptools import setup, find_packages


def read(file_name: str) -> str:
    """Read and return the contents of a file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='fix_plantuml',
    version='0.3.18',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fix_plantuml=src.main:main',
        ],
    },
    install_requires=[],
    author='Eliezer Birinbom',
    author_email='eliezerb@matrix.co.il',
    description='A tool to process PlantUML files.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/eliezerb2/fix_plantuml',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8'
)
