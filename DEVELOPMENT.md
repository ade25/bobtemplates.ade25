# How to use this package


This package provides *mr.bob* templates to generate packages for
Plone and Pyramid projects.

Available templates are:

- *Pyramid*: a template for a full featured Pyramid project
- *Plone*: a template for a full featured Plone project
- *Diazo*: a Diazo theme template
- *addon*: a new plone addon with dexterity content types
- *contenttype*: a single content type


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
$ mrbob --config ~/.mrbob bobtemplate:template_name
```

Using mrbob inside a buildout requires you to change directories (example
creating a diazo theme package)

```bash
$ cd src/
$ $ mrbob --config ~/.mrbob projectname.sitetheme bobtemplate:diazo
```
