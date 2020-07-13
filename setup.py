"""setuptools 

https://github.com/profLewis/uclgeog

over-ride with env variables

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding

"""
from codecs import open
from os import path
import os

here = path.abspath(path.dirname(__file__))

# defaults in here
url='https://github.com/profLewis/uclgeog'
version='1.0.0'
name='uclgeog'
description='UCL Geography MSc notes'
author='Prof. P. Lewis'
author_email='p.lewis@ucl.ac.uk'
license='MIT'
keywords='scientific computing'

# see if all required environment variables are set
# could do this neater for over-ride
try:
    # read env from env.sh
    with open('env.sh','r') as f:
        lines = f.readlines()
    # simple form read of the env file
    # assumes # at 1st character of comment line
    # and that format is
    # export x=y
    for i in ((l.split()[1].split('=')) for l in lines if(l[0] != '#')):
        os.environ[i[0]] = i[1]

    # The project's main homepage.
    url=os.environ['SETUP_URL']
    version=os.environ['SETUP_VERSION']
    name=os.environ['SETUP_NAME']
    description=os.environ['SETUP_DESCRIPTION']
    author=os.environ['SETUP_AUTHOR']
    author_email=os.environ['SETUP_AUTHOR_EMAIL']
    license=os.environ['SETUP_LICENSE']
    keywords=os.environ['SETUP_KEYWORDS']
except:
    pass

setup(  
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
  
    # Get the long description from the relevant file
    try:
      with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = ''
    except:
      long_description = ''
    
    pyver='Python '+".".join([str(sys.version_info.major),str(sys.version_info.minor),str(sys.version_info.micro)])

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        f'License :: OSI Approved :: {license} License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        f'Programming Language :: Python :: {pyver}',
    ],

    # What does your project relate to?

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    #install_requires=['numpy', 'matplotlib', 'pandas', 'jupyter','gdal'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file.txt'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
