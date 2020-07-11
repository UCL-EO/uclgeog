# Welcome to uclcodebase_core: Scientific Computing 
UCL Geography: Level 7 course, Scientific Computing



![](images/ucl_logo.png)

[![Anaconda-Server Badge](https://anaconda.org/proflewis/uclcodebase/badges/platforms.svg)](https://anaconda.org/proflewis/uclcodebase)
[![Anaconda-Server Badge](https://anaconda.org/proflewis/uclcodebase/badges/latest_release_date.svg)](https://anaconda.org/proflewis/uclcodebase)
[![Anaconda-Server Badge](https://anaconda.org/proflewis/uclcodebase/badges/version.svg)](https://anaconda.org/proflewis/uclcodebase)
[![Anaconda-Server Badge](https://anaconda.org/proflewis/uclcodebase/badges/downloads.svg)](https://anaconda.org/proflewis/uclcodebase)
[![Anaconda-Server Badge](https://anaconda.org/proflewis/uclcodebase/badges/installer/conda.svg)](https://conda.anaconda.org/proflewis)

![test](https://github.com/UCL-EO/uclcodebase_core/workflows/test/badge.svg)

[![docker pulls](https://img.shields.io/docker/pulls/proflewis/uclcodebase.svg)](https://hub.docker.com/proflewis/uclcodebase) [![docker stars](https://img.shields.io/docker/stars/proflewis/uclcodebase.svg)](https://hub.docker.com/r/proflewis/uclcodebase) 
[![metadata](https://images.microbadger.com/badges/image/proflewis/uclcodebase.svg)](https://microbadger.com/images/proflewis/uclcodebase "proflewis/uclcodebase image metadata")

This repository contains the core settings for software  several UCL MSc Geography courses.

It is designed to allow users to install the software necessary to partipate in these courses.


Prerequisites: install Docker
-------------

You need a computer with internet access, although once the software is downloaded you should be able to run things mainly stand-alone.

You will need at least 10 GB of disk space, ideally more. The docker image for this repository is around 1.5 GB compressed.

The simplest way to install this software that does not interfere with any other settings on your computer is to make use of [Docker](https://www.docker.com/products/docker-desktop).

First then, install [Docker](https://www.docker.com/products/docker-desktop) on your computer.

Pull docker image and test
-----------------

Next, pull the docker image and run a test notebook. In a terminal, type:

	docker run -p 8888:8888 proflewis/uclcodebase 

This should download the docker image (if it isnt already downloaded) and print some text such as:

	http://127.0.0.1:8888/?token=780c0c7038061608a8e9c92a293c8ecc3b04f173ef281734

Open a browser with that address, then navigate to the notebook you want to use.

Conda package
-----------------

To install the repo conda package:

	conda install -c proflewis uclcodebase

### Course Convenor

[Prof P. Lewis](http://www.geog.ucl.ac.uk/~plewis)

### Course and Contributing Staff

[Prof Philip Lewis](http://www.geog.ucl.ac.uk/~plewis)  

[Dr. Jose Gomez-Dans](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/research-staff/jose-gomez-dans/)

[Dr Qingling Wu](http://www.geog.ucl.ac.uk/about-the-department/people/research-staff/research-staff/qingling-wu/)

Other information
-----------------

For reference, the docker file is stored on [docker hub](https://hub.docker.com/r/proflewis/uclcodebase).

The script [bin/dockerMe](bin/dockerMe) contains all of the docker commands you might need to create such a docker image yourself.

This docker file is derived from [jupyter/base-notebook](https://hub.docker.com/r/jupyter/base-notebook/).
