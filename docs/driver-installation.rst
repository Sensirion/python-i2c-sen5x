The driver installation consists of creating a Python virtual environment,
activating it, and installing the driver using `pip`.

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

Install the driver:

.. code-block:: console

   python -m pip install sensirion_i2c_sen5x
