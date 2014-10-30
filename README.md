# Introduction


This package provides *mr.bob* templates to generate packages for
Plone and Pyramid projects.

Available templates are:

- *Pyramid*: a template for a full featured Pyramid project
- *Plone*: a template for a full featured Plone buildout
- *Addon*: a template for a Plone addon including Dexterity
- *contenttype*: a template for a single Dexterity contenttype
- *Diazo* (deprecated): a template for a Diazo theme package skeleton


## Global settings

Some answers to bob's questions can be pre-filled based on global configuration
so you don't have to answer them every time. You can store this configuration
on you local computer, by adding a file '~/.mrbob' and providing some defaults.

```
[variables]
author.name = John Doe
author.email = john@ade25.de
author.github.user = ade25
author.irc = irc.freenode.org#ade25
```

Use it by passing it as configuration parameter (example):

```bash
$ mrbob --config ~/.mrbob -O projectname bobtemplates:template_name
```

Using mrbob inside a buildout requires you to change directories (example
creating a diazo theme package)

```bash
$ cd src/
<<<<<<< HEAD
$ ../bin/mrbob --config ~/.mrbob -O projectname.sitetheme bobtemplates:plone
=======
$ $ mrbob --config ~/.mrbob projectname.sitetheme bobtemplates:diazo
>>>>>>> 0c9d2f736030dffeacb33907a7e5538353b1e0d3
```

## Setup local development environment

In orde to run mrbob templates for project scaffolding you need to setup a 
dedicated virtual env (e.g. unter ~/dev/mrbob)

```bash
$ ../path/to/python/bin/virtualenv-2.7 mrbob
$ cd ./mrbob
$ git clone git@github.com:ade25/bobtemplates.ade25.git
$ cd ./bobtemplates.ade25
$ ../bin/python setup.py develop
```

## Creating a project (Plone)

To create a full featured buildout for a Plone project including ready to use deployment configurations you need to run `mrbob` like this:

```bash
$ mrbob --config ~/.mrbob -O projectname bobtemplates:plone
```

Answer the questions accordingly.


## Creating a project (Pyramid example)

To create a Pyramid project first install (or upgrade to latest) *mr.bob* and
the *ade25.bobtemplates* package and then run `mrbob`:

```bash
$ easy_install -U mr.bob
$ easy_install -U bobtemplates.ade25
$ mrbob --config ~/.mrbob.ini -O foo bobtemplates:pyramid
```

Then answer some questions::

```bash
Welcome to mr.bob interactive mode. Before we generate directory structure,
some questions need to be answered.

Answer with a question mark to display help.
Value in square brackets at the end of the questions present default value
if there is no answer.


--> Name of the package: foo
...
```

And your package is ready! Let's build the development environment and see
if all tests pass::

```bash
$ cd foo
$ make
```

Great, you are now ready to start Pyramid::

```bash
$ make db
$ bin/pserve etc/development.ini
```
