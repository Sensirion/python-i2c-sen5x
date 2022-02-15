Quick Start
===========

.. important::  In order to correctly select I²C as interface, the interface
                select pin must be pulled low to GND before or at the same
                time the sensor is powered up.

Linux I²C Bus Example
---------------------

Following example code shows how to use this driver with a Sensirion SEN5x
connected to a Linux I²C bus (e.g. Raspberry Pi).


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


SensorBridge Example
--------------------

Following example code shows how to use this driver with a Sensirion SEN5x
connected to the computer using a `Sensirion SEK-SensorBridge`_. The driver
for the SensorBridge can be installed with
``pip install sensirion-shdlc-sensorbridge``.


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


.. _Sensirion SEK-SensorBridge: https://sensirion.com/sensorbridge
