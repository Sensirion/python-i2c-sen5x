# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from .response_types import Sen5xMassConcentration, Sen5xHumidity, \
    Sen5xTemperature, Sen5xAirQualityIndex

import logging
log = logging.getLogger(__name__)


class Sen5xMeasuredValues:
    """
    Represents a SEN5x measurement response for the "Read Measured Values"
    command.
    """

    def __init__(self, values):
        """
        Constructor.

        Example how to use this class:

        .. code-block:: python

            values = device.read_measured_values()

            # Pretty-print all values:
            print(values)

            # Access each physical value (as floats) separately:
            mc_1p0 = values.mass_concentration_1p0.physical
            mc_2p5 = values.mass_concentration_2p5.physical
            mc_4p0 = values.mass_concentration_4p0.physical
            mc_10p0 = values.mass_concentration_10p0.physical
            ambient_rh = values.ambient_humidity.percent_rh
            ambient_t = values.ambient_temperature.degrees_celsius
            voc_index = values.voc_index.scaled
            nox_index = values.nox_index.scaled

            # Check if a value is available or not:
            if values.nox_index.available:
                print("NOx ticks: {}".format(values.nox_index.ticks))
            else:
                print("NOx is not available.")

        :param tuple(int) values:
            Raw integer values as received from the device.
        """
        super(Sen5xMeasuredValues, self).__init__()

        #: All received raw values as a tuple of integers.
        self.values = values

        #: Mass concentration PM1.0
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xMassConcentration`).
        self.mass_concentration_1p0 = Sen5xMassConcentration(values[0])

        #: Mass concentration PM2.5
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xMassConcentration`).
        self.mass_concentration_2p5 = Sen5xMassConcentration(values[1])

        #: Mass concentration PM4.0
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xMassConcentration`).
        self.mass_concentration_4p0 = Sen5xMassConcentration(values[2])

        #: Mass concentration PM10.0
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xMassConcentration`).
        self.mass_concentration_10p0 = Sen5xMassConcentration(values[3])

        #: Ambient humidity
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xHumidity`).
        self.ambient_humidity = Sen5xHumidity(values[4])

        #: Ambient temperature
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xTemperature`).
        self.ambient_temperature = Sen5xTemperature(values[5])

        #: VOC index
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xAirQualityIndex`).
        self.voc_index = Sen5xAirQualityIndex(values[6])

        #: NOx index
        #: (:py:class:`~sensirion_i2c_sen5x.response_types.Sen5xAirQualityIndex`).
        self.nox_index = Sen5xAirQualityIndex(values[7])

    def to_str(self, separator="\n"):
        """
        Convert to printable string representation.

        :param str separator:
            Separator string.
        :return:
            Printable representation.
        :rtype:
            str
        """
        lines = []
        lines.append("Mass Concentration PM1.0:    {}".format(
            self.mass_concentration_1p0))
        lines.append("Mass Concentration PM2.5:    {}".format(
            self.mass_concentration_2p5))
        lines.append("Mass Concentration PM4.0:    {}".format(
            self.mass_concentration_4p0))
        lines.append("Mass Concentration PM10.0:   {}".format(
            self.mass_concentration_10p0))
        lines.append("Ambient Humidity:            {}".format(
            self.ambient_humidity))
        lines.append("Ambient Temperature:         {}".format(
            self.ambient_temperature))
        lines.append("VOC Index:                   {}".format(
            self.voc_index))
        lines.append("NOx Index:                   {}".format(
            self.nox_index))
        return separator.join(lines)

    def __str__(self):
        """
        Convert to printable string representation.

        :return:
            Printable representation.
        :rtype:
            str
        """
        return self.to_str()
