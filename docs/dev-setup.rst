To prepare your development environment, check out the repository,
create a Python virtual environment, and activate it.
Then install the driver in editable mode using `pip`.

Check out the Git repository to your local machine:

.. code-block:: console

   git clone <url-of-driver-repository>
   cd <checkout-folder>

Create a Python virtual environment:

.. code-block:: console

   python -m venv .venv

Activate the virtual environment:

.. tabs::

   .. group-tab:: Bash

      .. code-block:: console

         source .venv/bin/activate

   .. group-tab:: PowerShell

      .. code-block:: console

         .venv\Scripts\Activate.ps1

   .. group-tab:: Command Prompt

      .. code-block:: console

         .venv\Scripts\activate.bat

Install the driver in editable mode together with the development dependencies:

.. code-block:: console

   python -m pip install -e .

