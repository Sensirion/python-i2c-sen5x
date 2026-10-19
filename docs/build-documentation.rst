Build documentation
===================

The documentation is built with `Sphinx <http://www.sphinx-doc.org>`_:

.. code-block:: bash

    python -m pip install .[docs]           # Install doc requirements
    sphinx-build -b html docs docs/_build/html     # Build documentation
