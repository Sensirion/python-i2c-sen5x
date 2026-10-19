Install the SEN5x Driver
--------------------------

.. include:: driver-installation.rst


Use the SensorBridge on Windows
-------------------------------

1. Install the driver for the `Sensirion SEK-SensorBridge`_:

   .. code-block:: console

      python -m pip install sensirion-shdlc-sensorbridge

2. Connect the SEK-SensorBridge to your PC over USB.

   If the SEK-SensorBridge is not detected by your system, follow the
   `SensorBridge FTDI Driver Installation`_.

3. Connect the SEN5x sensor to the SEK-SensorBridge.

4. Run an example script in the activated virtual environment.

   By default, the script assumes that the SensorBridge is connected to the
   ``COM1`` serial port. If a different port is used, specify it with the
   ``--serial-port`` parameter:

   .. code-block:: console

        python <example>.py --serial-port <your COM port>


.. _Sensirion SEK-SensorBridge: https://developer.sensirion.com/product-support/sek-sensorbridge/
.. _SensorBridge FTDI Driver Installation: https://sensirion.github.io/python-shdlc-sensorbridge/sensor-bridge-installation.html

Example script
~~~~~~~~~~~~~~

.. sourcecode:: python

    import time
    from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
    from sensirion_shdlc_sensorbridge import SensorBridgePort, \
        SensorBridgeShdlcDevice, SensorBridgeI2cProxy
    from sensirion_i2c_driver import I2cConnection
    from sensirion_i2c_sen5x import Sen5xI2cDevice

    # Connect to the SensorBridge with default settings:
    #  - baudrate:      460800
    #  - slave address: 0
    with ShdlcSerialPort(port='COM1', baudrate=460800) as port:
        bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
        print("SensorBridge SN: {}".format(bridge.get_serial_number()))

        # Configure SensorBridge port 1 for SEN5x
        bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
        bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=5.0)
        bridge.switch_supply_on(SensorBridgePort.ONE)

        # Create SEN5x device
        i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
        device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))

        # Print some device information
        print("Version: {}".format(device.get_version()))
        print("Product Name: {}".format(device.get_product_name()))
        print("Serial Number: {}".format(device.get_serial_number()))

        # Perform a device reset (reboot firmware)
        device.device_reset()

        # Start measurement
        device.start_measurement()
        for i in range(10):
            # Wait until next result is available
            print("Waiting for new data...")
            while device.read_data_ready() is False:
                time.sleep(0.1)

            # Read measured values -> clears the "data ready" flag
            values = device.read_measured_values()
            print(values)

            # Access a specific value separately (see Sen5xMeasuredValues)
            mass_concentration = values.mass_concentration_2p5.physical
            ambient_temperature = values.ambient_temperature.degrees_celsius

            # Read device status
            status = device.read_device_status()
            print("Device Status: {}\n".format(status))

        # Stop measurement
        device.stop_measurement()
        print("Measurement stopped.")




Use the Linux I²C Driver
------------------------

On Linux systems, the sensor can alternatively be accessed directly through
the Linux user-space I²C driver.

1. Connect the SEN5x sensor to an I²C port of your system, for example I²C
   port 1 of a Raspberry Pi.

2. Run the example in the activated virtual environment

   By default, the script assumes that the sensor is connected to
   ``/dev/i2c-1``. If a different port is used, specify it with the
   ``--i2c-port`` parameter:

   .. code-block:: console

      python <example.py>.py --i2c-port <your I2C port>

Example script
~~~~~~~~~~~~~~

.. sourcecode:: python

    import time
    from sensirion_i2c_driver import I2cConnection, LinuxI2cTransceiver
    from sensirion_i2c_sen5x import Sen5xI2cDevice


    with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
        device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))

        # Print some device information
        print("Version: {}".format(device.get_version()))
        print("Product Name: {}".format(device.get_product_name()))
        print("Serial Number: {}".format(device.get_serial_number()))

        # Perform a device reset (reboot firmware)
        device.device_reset()

        # Start measurement
        device.start_measurement()
        for i in range(10):
            # Wait until next result is available
            print("Waiting for new data...")
            while device.read_data_ready() is False:
                time.sleep(0.1)

            # Read measured values -> clears the "data ready" flag
            values = device.read_measured_values()
            print(values)

            # Access a specific value separately (see Sen5xMeasuredValues)
            mass_concentration = values.mass_concentration_2p5.physical
            ambient_temperature = values.ambient_temperature.degrees_celsius

            # Read device status
            status = device.read_device_status()
            print("Device Status: {}\n".format(status))

        # Stop measurement
        device.stop_measurement()
        print("Measurement stopped.")

