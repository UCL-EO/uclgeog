# Welcome to uclgeog: Python computing base
UCL Geography: Computing base setup for python and jupyter

![](images/ucl_logo.png)

[![Build Status](https://travis-ci.org/UCL-EO/uclgeog.svg?branch=master)](https://travis-ci.org/UCL-EO/uclgeog)

[![docker pulls](https://img.shields.io/docker/pulls/proflewis/uclgeog.svg)](https://hub.docker.com/proflewis/uclgeog) [![docker stars](https://img.shields.io/docker/stars/proflewis/uclgeog.svg)](https://hub.docker.com/r/proflewis/uclgeog) 
[![metadata](https://images.microbadger.com/badges/image/proflewis/uclgeog.svg)](https://microbadger.com/images/proflewis/uclgeog "proflewis/uclgeog image metadata")

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCL-EO/uclgeog.git/master)

This repository contains the base settings for software several UCL Geography courses.

It is designed to allow users to install the software necessary to partipate in these courses.


Prerequisites: install Docker
-------------

You need a computer with internet access, although once the software is downloaded you should be able to run things mainly stand-alone.

You will need at least 10 GB of disk space, ideally more. The docker image for this repository is around 1.5 GB compressed.

The simplest way to install this software that does not interfere with any other settings on your computer is to make use of [Docker](https://www.docker.com/products/docker-desktop).

First then, install [Docker](https://www.docker.com/products/docker-desktop) on your computer.

Pull docker image and test
-----------------

Next, pull the docker image and run a test. In a terminal, type:

	docker run proflewis/uclgeog:latest bash -c "cat meta.yaml| grep version"
	
which should print out the version number. If this is up to date it should show the same version number as in [meta.yaml](meta.yaml).

To run jupyter (to run notebooks):

	docker run -p 8888:8888 proflewis/uclgeog 

This should download the docker image (if it isnt already downloaded) and print some text such as:

	http://127.0.0.1:8888/?token=780c0c7038061608a8e9c92a293c8ecc3b04f173ef281734

Open a browser with that address, then navigate to the notebook you want to use.

If you want to play about on the docker machine:

	docker run -it proflewis/uclgeog bash

will open a `bash` shell for you. If you need to be root on the machine for some reason:

	docker run -u 0 -it proflewis/uclgeog bash

Conda package
-----------------

To install the repo conda package:

	conda install -c proflewis uclgeog

### Course Convenor

[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)

### Course and Contributing Staff

[Prof Philip Lewis](http://www.geog.ucl.ac.uk/~plewis)  

[Dr. Jose Gomez-Dans](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/research-staff/jose-gomez-dans/)

[Dr Qingling Wu](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/research-staff/qingling-wu/)

Other information
-----------------

For reference:

* the docker file is stored on [hub.docker.com](https://hub.docker.com/r/proflewis/uclgeog).
* the codebase is stored on [anaconda.org](https://anaconda.org/profLewis/uclgeog).
* the git is stored on [github.com](https://github.com/UCL-EO/uclgeog).
* the binder is stored on [mybinder.org](https://mybinder.org/v2/gh/UCL-EO/uclgeog.git/master)
