# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import logging
log = logging.getLogger(__name__)


class Sen5xMassConcentration:
    """
    Represents a SEN5x measurement response for the particulate matter mass
    concentration.

    With the :py:attr:`ticks` attribute you can access the raw data as received
    from the device. For the converted physical value the :py:attr:`physical`
    attribute is available. The attribute :py:attr:`available` can be used to
    check whether the value is available or not.
    """
    def __init__(self, ticks):
        """
        Creates an instance from the received raw data.

        :param int ticks:
            The read ticks as received from the device.
        """
        super(Sen5xMassConcentration, self).__init__()

        #: The ticks (int) as received from the device.
        self.ticks = int(ticks)

        #: Flag (bool) whether the received value is available or not.
        self.available = self.ticks != 0xFFFF

        #: The converted physical value (float) in µg/m³. This is NaN if the
        #: value is not available.
        self.physical = (ticks / 10.0) if self.available else float('nan')

    def __str__(self):
        return '{:0.1f} µg/m^3'.format(self.physical) if self.available \
            else 'N/A'


class Sen5xHumidity:
    """
    Represents a SEN5x measurement response for the humidity.

    With the :py:attr:`ticks` attribute you can access the raw data as received
    from the device. For the converted value the :py:attr:`percent_rh`
    attribute is available. The attribute :py:attr:`available` can be used to
    check whether the value is available or not.
    """
    def __init__(self, ticks):
        """
        Creates an instance from the received raw data.

        :param int ticks:
            The read ticks as received from the device.
        """
        super(Sen5xHumidity, self).__init__()

        #: The ticks (int) as received from the device.
        self.ticks = int(ticks)

        #: Flag (bool) whether the received value is available or not.
        self.available = self.ticks != 0x7FFF

        #: The converted humidity (float) in %RH. This is NaN if the
        #: value is not available.
        self.percent_rh = (ticks / 100.0) if self.available else float('nan')

    def __str__(self):
        return '{:0.2f} %RH'.format(self.percent_rh) if self.available \
            else 'N/A'


class Sen5xTemperature:
    """
    Represents a SEN5x measurement response for the temperature.

    With the :py:attr:`ticks` attribute you can access the raw data as received
    from the device. For the converted values you can choose between
    :py:attr:`degrees_celsius` and :py:attr:`degrees_fahrenheit`. The
    attribute :py:attr:`available` can be used to check whether the value is
    available or not.
    """
    def __init__(self, ticks):
        """
        Creates an instance from the received raw data.

        :param int ticks:
            The read ticks as received from the device.
        """
        super(Sen5xTemperature, self).__init__()

        #: The ticks (int) as received from the device.
        self.ticks = int(ticks)

        #: Flag (bool) whether the received value is available or not.
        self.available = self.ticks != 0x7FFF

        #: The converted temperature (float) in °C. This is NaN if the
        #: value is not available.
        self.degrees_celsius = (ticks / 200.0) if self.available else float('nan')

        #: The converted temperature (float) in °F. This is NaN if the
        #: value is not available.
        self.degrees_fahrenheit = ((self.degrees_celsius * 9.0 / 5.0) + 32.0) \
            if self.available else float('nan')

    def __str__(self):
        return '{:0.2f} °C'.format(self.degrees_celsius) if self.available \
            else 'N/A'


class Sen5xAirQualityIndex:
    """
    Represents a SEN5x measurement response for the air quality index.

    With the :py:attr:`ticks` attribute you can access the raw data as received
    from the device. For the converted value the :py:attr:`scaled` attribute is
    available. The attribute :py:attr:`available` can be used to check whether
    the value is available or not.
    """
    def __init__(self, ticks):
        """
        Creates an instance from the received raw data.

        :param int ticks:
            The read ticks as received from the device.
        """
        super(Sen5xAirQualityIndex, self).__init__()

        #: The ticks (int) as received from the device.
        self.ticks = int(ticks)

        #: Flag (bool) whether the received value is available or not.
        self.available = self.ticks != 0x7FFF

        #: The converted/scaled index (float). This is NaN if the
        #: value is not available.
        self.scaled = (ticks / 10.0) if self.available else float('nan')

    def __str__(self):
        return '{:.1f}'.format(self.scaled) if self.available else 'N/A'


class Sen5xDeviceStatus:
    """
    Represents a SEN5x device status response.

    With the :py:attr:`value` attribute you can access the raw value as
    received from the device. The convenience attribute :py:attr:`flags`
    allows you to get all set flags as strings. In addition, each flag is
    provided as separate bool attribute.
    """
    def __init__(self, value):
        """
        Creates an instance from the received raw data.

        :param int value:
            The raw device status value as received from the device.
        """
        super(Sen5xDeviceStatus, self).__init__()

        #: The value (int) as received from the device.
        self.value = value

        #: All currently set flags as a list of flag names, i.e. list(str)
        self.flags = []

        #: Flag (bool) whether a fan error occurred.
        self.fan_error = self._add(4, 'fan_error')

        #: Flag (bool) whether a laser error occurred.
        self.laser_error = self._add(5, 'laser_error')

        #: Flag (bool) whether an SHT error occurred.
        self.sht_error = self._add(6, 'sht_error')

        #: Flag (bool) whether an SGP error occurred.
        self.sgp_error = self._add(7, 'sgp_error')

        #: Flag (bool) whether the fan cleaning is currently active.
        self.fan_cleaning = self._add(19, 'fan_cleaning')

        #: Flag (bool) whether the fan speed is currently out of specs.
        self.fan_speed_out_of_specs = self._add(21, 'fan_speed_out_of_specs')

    def _add(self, index, name):
        is_set = (self.value & (1 << index)) != 0
        if is_set:
            self.flags.append(name)
        return is_set

    def __str__(self):
        return "0x{:08X} [{}]".format(
            self.value, ', '.join(self.flags) if len(self.flags) else 'OK')


class Sen5xFirmwareVersion:
    """
    Class representing the firmware version of a device.
    """

    def __init__(self, major, minor, debug):
        """
        Constructor.

        :param byte major: Major version.
        :param byte minor: Minor version.
        :param bool debug: Debug flag (False for official releases).
        """
        super(Sen5xFirmwareVersion, self).__init__()
        self.major = major
        self.minor = minor
        self.debug = debug

    def __str__(self):
        return '{}.{}{}'.format(self.major, self.minor,
                                self.debug and '-debug' or '')


class Sen5xHardwareVersion:
    """
    Class representing the hardware version of a device.
    """

    def __init__(self, major, minor):
        """
        Constructor.

        :param byte major: Major version.
        :param byte minor: Minor version.
        """
        super(Sen5xHardwareVersion, self).__init__()
        self.major = major
        self.minor = minor

    def __str__(self):
        return '{}.{}'.format(self.major, self.minor)


class Sen5xProtocolVersion:
    """
    Class representing the I2C protocol version of an I2C device.
    """

    def __init__(self, major, minor):
        """
        Constructor.

        :param byte major: Major version.
        :param byte minor: Minor version.
        """
        super(Sen5xProtocolVersion, self).__init__()
        self.major = major
        self.minor = minor

    def __str__(self):
        return '{}.{}'.format(self.major, self.minor)


class Sen5xVersion:
    """
    Class representing all version numbers of an I2C device. This is used for
    the "Get Version" command.
    """

    def __init__(self, firmware, hardware, protocol):
        """
        Constructor.

        :param ~sensirion_i2c_sen5x.response_types.Sen5xFirmwareVersion firmware:
            Firmware version.
        :param ~sensirion_i2c_sen5x.response_types.Sen5xHardwareVersion hardware:
            Hardware version.
        :param ~sensirion_i2c_sen5x.response_types.Sen5xProtocolVersion protocol:
            SHDLC protocol version.
        """
        super(Sen5xVersion, self).__init__()
        self.firmware = firmware
        self.hardware = hardware
        self.protocol = protocol

    def __str__(self):
        return 'Firmware {}, Hardware {}, Protocol {}'.format(
            self.firmware, self.hardware, self.protocol
        )
