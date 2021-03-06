Introduction
============

``bobtemplates.ade25`` provides `mr.bob`_ templates to generate packages for
Plone and Pyramid projects. Templates are designed to be reusable by others,
individuals and teams. All templates have tests for verifying which files and
folders were generated, along with tests that run on the actual generated
package.

Available templates are:

* `Plone`_: a template for a full featured Plone add-on, including:

  * zc.buildout best practices
  * GenericSetup install profile
  * Zope 3 browser layer
  * `z3c.jbot`_ overrides folder
  * ``static/`` resourceDirectory for serving static resources (images, CSS,
    JS, etc.)
  * `Sphinx`_ documentation
  * test suite with a solid test coverage
  * `Travis CI`_ integration

* `Pyramid`_: a template for a full featured Pyramid project, including:

  * zc.buildout best practices
  * SQLite for development, PostgreSQL for production
  * A sample view with a Chameleon template
  * A sample model
  * ``static`` resources filled with Twitter Bootstrap niceties
  * `Sphinx`_ documentation
  * Exemplary test suite
  * `Travis CI`_ continuous integration
  * `Heroku` continuous deployment


Global settings
---------------

Some answers to bob's questions can be pre-filled based on global configuration
so you don't have to answer them every time. You can store this configuration
either on you local computer, or if you are working in a team, somewhere
online. We, at `ade25 Ltd.`_, for example, have these answers always
available for us at http://www.ade25.com/mrbob.ini.


Creating a Plone add-on package
-------------------------------

To create a Plone add-on first install (or upgrade to latest) ``mr.bob`` and
the ``bobtemplates.ade25`` package and then run `mrbob`::

    $ easy_install -U mr.bob
    $ easy_install -U bobtemplates.ade25
    $ mrbob --config ~/.mrbob.ini -O collective.foo bobtemplates:plone

Then answer some questions::

    Welcome to mr.bob interactive mode. Before we generate directory structure,
    some questions need to be answered.

    Answer with a question mark to display help.
    Value in square brackets at the end of the questions present default value
    if there is no answer.


    --> Name of the package: foo
    (namespace is already set in the ~/.mrbob.ini)

    ...

And your package is ready! Let's build the development environment and see
if all tests pass::

    $ cd collective.foo
    $ make

Great, you are now set to start Zope in foreground mode: ``bin/instance fg``.
Once Zope is up, point your browser to ``http://localhost:8080``, login as
``admin:admin``, create a new Plone site while selecting ``collective.foo``
from the list of Add-ons and voilá: a Plone site with your very own add-on
installed.

Now you can add some customizations to views and templates, or maybe write some
CSS and JS.


Creating a Pyramid project
--------------------------

To create a Pyramid project first install (or upgrade to latest) ``mr.bob`` and
the ``bobtemplates.ade25`` package and then run `mrbob`::

    $ easy_install -U mr.bob
    $ easy_install -U bobtemplates.ade25
    $ mrbob --config ~/.mrbob.ini -O foo bobtemplates:pyramid

Then answer some questions::

    Welcome to mr.bob interactive mode. Before we generate directory structure,
    some questions need to be answered.

    Answer with a question mark to display help.
    Value in square brackets at the end of the questions present default value
    if there is no answer.


    --> Name of the package: foo
    ...

And your package is ready! Let's build the development environment and see
if all tests pass::

    $ cd foo
    $ make

Great, you are now ready to start Pyramid::

    $ make db
    $ bin/pserve etc/development.ini


.. _mr.bob: http://mrbob.readthedocs.org/en/latest/
.. _ade25 Ltd.: http://www.ade25.com
.. _Plone: http://plone.org
.. _Pyramid: http://docs.pylonsproject.org/en/latest/
.. _z3c.jbot: http://pypi.python.org/pypi/z3c.jbot
.. _Sphinx: http://sphinx-doc.org/
.. _Travis CI: http://travis-ci.org/
.. _Heroku: http://heroku.com/
