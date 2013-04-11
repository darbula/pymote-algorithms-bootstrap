import os, sys
import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages


setup(
    name = "<name>", # i.e. Pymote example algorithms
    version = '<version', # i.e. 0.1.1
    url = '<url>', # i.e. https://github.com/<user>/pymote-algorithms-example
    author = '<author>',
    author_email = 'username@example.com',
    description = 'An algorithm extension package for Pymote - high-level Python library for simulation of distributed algorithms.',
    download_url = '',
    packages = find_packages(),
    exclude_package_data = { '': ['README.rst'] },
    install_requires=[
        'Pymote',
    ],
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),

    # http://pythonhosted.org/distribute/setuptools.html#dynamic-discovery-of-services-and-plugins
    entry_points = {
        'pymote.algorithms': ['example = pymote.algorithms.example'],
    },
)
