Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_:

.. code-block:: bash

    pip install -e .[test]                       # Install test requirements


Connect your SEN5x sensor to a
`SensorBridge <https://sensirion.com/products/catalog/SEK-SensorBridge/>`_ on port 1. Assuming the SensorBridge is
attached to COM1 you can start the tests with the following command:

.. code-block:: bash

    pytest --serial-port=COM1                    # Run all tests for SEN5x on the sensor attached to COM1


.. note::
    The SensorBridge must have default settings (baudrate 460800, address 0)

In order to select tests that do not need an actual SEN5x device, you can use the ``-m`` option of pytest:

.. code-block:: bash

    pytest -m "not needs_device"   # Run all tests that do not need an actual SEN5x device

