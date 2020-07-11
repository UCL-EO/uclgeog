"""setuptools for uclgeog_core Scientific Computing, UCL 

https://github.com/profLewis/uclgeog_core
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# override from META if given
# to allow consistency

setup_info = {
  'readme'  : 'This is autogenerated by setup.py: do not edit this file directly',
  'url'     : 'https://github.com/profLewis/uclgeog_core',
  'version' : '1.0.11',
  'meta'    : 'meta.yaml', 
  'name'    : 'uclgeog'
}

# get version & name from meta
# eg 
'''
package:
  name:    uclgeog
  version: 1.0.11

source:
  git_rev: 1.0.0
  git_url: https://github.com/UCL-EO/uclgeog_core

build:
  noarch: python
  number: 0
  script: python -m pip install --no-deps --ignore-installed .


requirements:
  build:
    - python>=3.7
    - setuptools

  run:
    - python

test:
  imports:
    - uclgeog

about:
  home: https://github.com/UCL-EO/uclgeog_core
'''

# try reading from META
try:
  with open(setup_info['meta'],'r') as f:
    # read the last line
    lines = [i.strip() for i in f.readlines()] 

  # package info
  # keep this low level for robustness
  package = [i == 'package:' for i in lines]
  end_package = [i == '' for i in lines]
  version = ['version:' in i for i in lines]
  version_no = [''.join(i.split('version:')[1:]).strip() for i in lines]
  name =  [''.join(i.split('name:')[1:]).strip() for i in lines]
  info = list(zip(package,version,end_package,version_no,name))
  for i,t in enumerate(info):
    package,version,end_package,version_no,name = t
    # package, so start parsing following lines
    if package:
      for j in range(i,len(info)):
        package,version,end_package,version_no,name = info[j]
        if version:
          setup_info['version'] = version_no
        if len(name):
          setup_info['name'] = name
        if end_package:
          break

  # source info
  package = [i == 'source:' for i in lines]
  end_package = [i == '' for i in lines]
  version = [''.join(i.split('version:')[1:]).strip() for i in lines]
  info = list(zip(package,version,end_package))
  for i,t in enumerate(info):
    package,version,end_package = t
    if package:
      for j in range(i,len(info)):
        package,version,end_package = info[j]
        if len(version):
          setup_info['url'] = version
        if end_package:
          break

  # test

except:
  del setup_info['meta']

try:
  import pprint
  print = pprint.PrettyPrinter(indent=4).pprint
  # test pretty printer
  print('I feel pretty, oh so pretty')
except:
  pass
  
print('-'*40)
print(setup_info)
print('-'*40)
# store this in VERSION file
try:
  import json
  with open('setup_info.json', 'w') as fp:
    json.dump(setup_info, fp)
except:
  pass

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = ''

setup(
    name=setup_info['name'],

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=setup_info['version'],

    description='UCL MSc notes',
    long_description=long_description,

    # The project's main homepage.
    url=setup_info['url'],

    # Author details
    author='Prof. P. Lewis',
    author_email='p.lewis@ucl.ac.uk',

    # Choose your license
    license='MIT',

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
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='scientific computing',

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
