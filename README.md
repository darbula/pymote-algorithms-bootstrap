Pymote algorithms bootstrap
===========================
This repo should be used as a template to quickly start a new project that provides Pymote algorithms.



Usage
-----

1. Fork or download this repo and rename root folder from `pymote-algorithms-bootstrap` to `pymote-algorithms-<package>` - replace `<package>` part with some custom name.
2. Organize your algorithms in modules and subpackages under `pymote/algorithms` directory.
3. To make the package importable the proper way is to edit provided `setup.py` script and install it. Alternative is to write `<package>.pth` file containing path to package inside appropriate, i.e. virtual environment or systemwide, `site-packages` directory. One more alternative is to write the path to package into `PYTHONPATH` environment variable.

When implementing algorithms from (or for) some scientific publications the proper way to name the subpackage or module should be `<author_last_name><year>` i.e. for *DV based positioning in ad hoc networks*, by Dragoş Niculescu and Badri Nath name should be `niculescu2003`.


Source distribution
-------------------

If you want to distribute your pymote algorithms on [PyPI](https://pypi.python.org/pypi) please follow these steps:

1. Edit `setup.py` and enter relevant data
2. `python setup.py sdist upload register`

For details visit documentation [here](http://docs.python.org/2/distutils/index.html#distutils-index).
