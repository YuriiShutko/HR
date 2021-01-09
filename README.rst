HR
==

CLI tool for managing users on Linux systems.

Preparing the Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:YuriiShutko/HR``
3. ``cd`` into the repository
4. Fetch development depencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make
