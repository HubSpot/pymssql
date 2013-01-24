from setuptools import setup, find_packages

setup(
    name='pymssql',
    version='1.0.2osx',
    description='A simple database interface to MS-SQL for Python. Contains prebuilt _mssql.so for 64-bit OSX.',
    long_description='A simple database interface to MS-SQL for Python. Contains prebuilt _mssql.so for 64-bit OSX.',
    author='Tom Petr',
    author_email='tpetr@hubspot.com',
    license='LGPL',
    url='http://pymssql.sourceforge.net',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    setup_requires=["Cython>=0.12"],
    platforms=["any"],  # TODO: find a better value
)
