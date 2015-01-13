#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Render bobtemplates.plone hooks.
"""
from mrbob.bobexceptions import ValidationError

import os
import shutil
import string
import subprocess
import sys


def to_boolean(configurator, question, answer):
    """
    If you want to convert an answer to Python boolean, you can
    use this function as :ref:`post-question-hook`:

    .. code-block:: ini

        [questions]
        idiot.question = Are you young?
        idiot.post_ask_question = mrbob.hooks:to_boolean

    Following variables can be converted to a boolean: **y, n, yes, no, true,
    false, 1, 0**
    """
    if isinstance(answer, bool):
        return answer
    value = answer.lower()
    if value in ['y', 'yes', 'true', '1']:
        return True
    elif value in ['n', 'no', 'false', '0']:
        return False
    else:
        raise ValidationError('Value must be a boolean (y/n)')


def get_git_info(value):
    """Try to get information from the git-config.
    """
    gitargs = ['git', 'config', '--get']
    try:
        result = subprocess.check_output(gitargs + [value]).strip()
        return result
    except (OSError, subprocess.CalledProcessError):
        pass


def validate_packagename(configurator):
    """Find out if the name target-dir entered when invoking the command
    can be a valid python-package.
    """
    package_dir = configurator.target_directory.split('/')[-1]
    fail = False

    allowed = set(string.ascii_letters + string.digits + '.-_')
    if not set(package_dir).issubset(allowed):
        fail = True

    if package_dir.startswith('.') or package_dir.endswith('.'):
        fail = True

    parts = len(package_dir.split('.'))
    if parts < 2 or parts > 3:
        fail = True

    if fail:
        msg = "Error: '{0}' is not a valid packagename.\n".format(package_dir)
        msg += "Please use a valid name (like collective.myaddon or "
        msg += "plone.app.myaddon)"
        sys.exit(msg)


def pre_username(configurator, question):
    """Get email from git and validate package name.
    """
    # validate_packagename should be run before asking the first question.
    validate_packagename(configurator)

    default = get_git_info('user.name')
    if default:
        question.default = default


def pre_email(configurator, question):
    """Get email from git.
    """
    default = get_git_info('user.email')
    if default:
        question.default = default


def post_travis(configurator, question, answer):
    """ Skip questions on travis.
    """
    value = to_boolean(configurator, question, answer)
    mto = 'info@ade25.de'
    if not value:
        configurator.variables['travis.notifications.type'] = 'email'
        configurator.variables['travis.notifications.destination'] = mto
    return value


def cleanup_package(configurator):
    """ Cleanup and delete unneeded configuration"""

    # path for object and file deletion
    base_path = configurator.target_directory

    # find out what to delete
    to_delete = []

    if not configurator.variables['package.profile']:
        to_delete.extend([
            "{0}/profiles",
            "{0}/testing.zcml",
            "{0}/setuphandlers.py",
            "{0}/interfaces.py",
        ])

    if not configurator.variables['package.setuphandlers']:
        to_delete.extend([
            "{0}/setuphandlers.py",
        ])

    if not configurator.variables['package.locales']:
        to_delete.extend([
            "{0}/locales",
        ])

    if not configurator.variables['package.example']:
        to_delete.extend([
            "{0}/browser/templates",
            "{0}/browser/views.py",
        ])

    if not configurator.variables['package.testing']:
        to_delete.extend([
            "{0}/tests",
            "{0}/testing.py",
            "{0}/testing.zcml",
            "{0}/.coveragerc".format(configurator.target_directory),
            "{0}/buildout.d/jenkins.cfg".format(configurator.target_directory),
        ])

    if not configurator.variables['travis.integration.enabled']:
        to_delete.extend([
            "{0}/.travis.yml".format(configurator.target_directory),
            "{0}/travis.cfg".format(configurator.target_directory),
        ])

    if not configurator.variables['package.theme']:
        to_delete.extend([
            "{0}/theme",
            "{0}/profiles/default/theme.xml",
        ])

    # remove parts
    for path in to_delete:
        path = path.format(base_path)
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
