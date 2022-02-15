# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import sphinx.ext.autodoc
from datetime import datetime

import pkg_resources

# Add project directory such that sphinx can detect the package.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# -- Project information -----------------------------------------------------
distribution = pkg_resources.get_distribution('sensirion_i2c_sen5x')

project = distribution.project_name
copyright = u'{} Sensirion AG, Switzerland'.format(datetime.now().year)
author = 'Sensirion AG'
version = distribution.version
release = distribution.version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
]

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_favicon = 'favicon.ico'

# Workaround for weirdly formatted function parameters. See https://github.com/readthedocs/sphinx_rtd_theme/issues/766
html4_writer = True


# -- Extension configuration -------------------------------------------------

autodoc_member_order = 'bysource'

autodoc_default_flags = [
    'members',
    'special-members',      # To see __init__()
    'inherited-members',    # To see the methods from base classes
]


def autodoc_skip_member(app, what, name, obj, skip, options):
    whitelist = ('__init__',)
    exclude = name.startswith('__') and (name not in whitelist)
    return skip or exclude


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)


# Workaround for "=None" documentation of instance attributes
# (see https://github.com/sphinx-doc/sphinx/issues/2044)
sphinx.ext.autodoc.InstanceAttributeDocumenter.add_directive_header = \
    sphinx.ext.autodoc.ClassLevelDocumenter.add_directive_header

scv_whitelist_branches = ('master',)

scv_grm_exclude = ('.gitignore', '.nojekyll')

intersphinx_mapping = {
    'sensirion_i2c_driver': (
        'https://sensirion.github.io/python-i2c-driver/',
        None
    ),
}
