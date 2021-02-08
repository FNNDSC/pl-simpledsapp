pl-simpledsapp
==============

.. image:: https://img.shields.io/docker/v/fnndsc/pl-simpledsapp
    :target: https://hub.docker.com/r/fnndsc/pl-simpledsapp

.. image:: https://img.shields.io/github/license/fnndsc/pl-simpledsapp
    :target: https://github.com/FNNDSC/pl-simpledsapp/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-simpledsapp/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-simpledsapp/actions


.. contents:: Table of Contents


Abstract
--------

A simple ChRIS ds app demo.


Description
-----------

``simpledsapp`` basically does an explicit copy of each file in an input directory to the
output directory, prefixing an optional string to each filename.


Usage
-----

.. code::

        python simpledsapp.py
            [-h] [--help]
            [--json]
            [--man]
            [--meta]
            [--savejson <DIR>]
            [-v <level>] [--verbosity <level>]
            [--version]
            <inputDir>
            <outputDir>
            [--prefix <PREFIX>]
            [--ignoreInputDir]
            [--sleepLength <SECONDS>]
            [--dummyInt <INT>]
            [--dummyFloat <FLOAT>]


Arguments
~~~~~~~~~

.. code::

        [-h] [--help]
        If specified, show help message and exit.

        [--json]
        If specified, show json representation of app and exit.

        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.

        [--savejson <DIR>]
        If specified, save json representation file to DIR and exit.

        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.

        [--version]
        If specified, print version number and exit.

        <inputDir>
        Input directory.

        <outputDir>
        Output directory.

        [--prefix <PREFIX>]
        If specified, append this prefix to resulting output files.

        [--ignoreInputDir]
        If specified, ignore the input dir completely.

        [--sleepLength <SECONDS>]
        If specified, time to sleep before performing plugin action.

        [--dummyInt <INT>]
        If specified, this is a dummy (not used) input integer parameter.

        [--dummyFloat <FLOAT>]
        If specified, this is a dummy (not used) input float parameter.


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-simpledsapp simpledsapp --man

Run
~~~

You need you need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-simpledsapp simpledsapp                        \
        /incoming /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-simpledsapp .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-simpledsapp nosetests

Examples
--------

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-simpledsapp simpledsapp                        \
        /incoming /outgoing --prefix lolo


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
