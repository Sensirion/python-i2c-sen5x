# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import importlib.metadata as metadata
import os
import sys
from datetime import datetime

# sys.path.insert(0, os.path.abspath('.'))

import sensirion_i2c_sen5x

# Add project directory such that sphinx can detect the package.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# -- Project information -----------------------------------------------------
distribution = metadata.distribution("sensirion_i2c_sen5x")

project = distribution.name
copyright = "{} Sensirion AG, Switzerland".format(datetime.now().year)
author = "Sensirion AG"

# The short X.Y version
version = distribution.version
# The full version, including alpha/beta/rc tags
release = distribution.version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_tabs.tabs",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Configure that index.rst is master and not contents.rst
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_favicon = "favicon.ico"

# -- Extension configuration -------------------------------------------------
autodoc_default_options = {
    "members": None,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
}


def autodoc_skip_member(app, what, name, obj, skip, options):
    whitelist = ("__init__",)
    exclude = name.startswith("__") and (name not in whitelist)
    return skip or exclude


def setup(app):
    app.connect("autodoc-skip-member", autodoc_skip_member)


scv_whitelist_branches = ("main",)

scv_grm_exclude = (".gitignore", ".nojekyll")

intersphinx_mapping = {
    "sensirion_i2c_driver": ("https://sensirion.github.io/python-i2c-driver/", None),
}
