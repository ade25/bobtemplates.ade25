# Introduction


This package provides *mr.bob* templates to generate packages for
Plone and Pyramid projects.

Available templates are:

- *Pyramid*: a template for a full featured Pyramid project
- *Plone*: a template for a full featured Plone add-on


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
package.namespace = ade25
```

Use it by passing it as configuration parameter (example):

```bash
$ mrbob --config ~/.mrbob mrbob:template_sample/
```

## Creating a Pyramid project

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

    $ cd foo
    $ make

Great, you are now ready to start Pyramid::

    $ make db
    $ bin/pserve etc/development.ini
