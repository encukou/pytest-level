import pathlib
from setuptools import setup

setup(
    name="pytest-level",
    version='0.1.1',
    py_modules=["pytest_level"],
    description='Select tests of a given level or lower',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type="text/markdown",
    author='Petr Viktorin',
    author_email='encukou@gmail.com',
    license='MIT',
    url='https://github.com/encukou/pytest-level',
    entry_points={"pytest11": ["name_of_plugin = pytest_level"]},
    classifiers=[
        'Framework :: Pytest',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    setup_requires=['pytest'],
    zip_safe=False,
)
