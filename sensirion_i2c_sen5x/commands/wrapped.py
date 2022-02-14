# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from .generated import \
    Sen5xI2cCmdGetTemperatureOffsetParameters as GetTemperatureOffsetParametersGenerated, \
    Sen5xI2cCmdGetVersion as GetVersionGenerated, \
    Sen5xI2cCmdGetWarmStartParameter as GetWarmStartParameterGenerated, \
    Sen5xI2cCmdReadAndClearDeviceStatus as ReadAndClearDeviceStatusGenerated, \
    Sen5xI2cCmdReadDataReady as ReadDataReadyGenerated, \
    Sen5xI2cCmdReadDeviceStatus as ReadDeviceStatusGenerated, \
    Sen5xI2cCmdReadMeasuredValues as ReadMeasuredValuesGenerated, \
    Sen5xI2cCmdSetTemperatureOffsetParameters as SetTemperatureOffsetParametersGenerated, \
    Sen5xI2cCmdSetWarmStartParameter as SetWarmStartParameterGenerated
from ..measured_values import Sen5xMeasuredValues
from ..response_types import Sen5xDeviceStatus, Sen5xFirmwareVersion, \
    Sen5xHardwareVersion, Sen5xProtocolVersion, Sen5xVersion

import logging
log = logging.getLogger(__name__)


class Sen5xI2cCmdReadDataReady(ReadDataReadyGenerated):
    """
    Read Data Ready I²C Command

    This command can be used to check if new measurement results are ready to
    read. The data ready flag is automatically reset after reading the
    measurement values with the 0x03.. "Read Measured Values" commands.

    .. note:: During fan (auto-)cleaning, no measurement data is available for
              several seconds and thus this flag will not be set until cleaning
              has finished. So please expect gaps of several seconds at any
              time if fan auto-cleaning is enabled.
    """

    def interpret_response(self, data):
        """
        Validates the CRCs of the received data from the device and returns
        the interpreted data.

        :param bytes data:
            Received raw bytes from the read operation.
        :return:
            ``True`` if data is ready, ``False`` if not.
            When no measurement is running, ``False`` will be returned.
        :rtype: bool
        :raise ~sensirion_i2c_driver.errors.I2cChecksumError:
            If a received CRC was wrong.
        """
        padding, data_ready = ReadDataReadyGenerated.interpret_response(self, data)
        return data_ready


class Sen5xI2cCmdReadMeasuredValues(ReadMeasuredValuesGenerated):
    """
    Read Measured Values I²C Command

    Returns the measured values.

    The command 0x0202 "Read Data Ready" can be used to check if new data is
    available since the last read operation. If no new data is available, the
    previous values will be returned again.
    """

    def interpret_response(self, data):
        """
        Validates the CRCs of the received data from the device and returns
        the interpreted data.

        :param bytes data:
            Received raw bytes from the read operation.
        :return:
            Object containing all measured values.
        :rtype:
            ~sensirion_i2c_sen5x.measured_values.Sen5xMeasuredValues
        :raise ~sensirion_i2c_driver.errors.I2cChecksumError:
            If a received CRC was wrong.
        """
        values = ReadMeasuredValuesGenerated.interpret_response(self, data)
        return Sen5xMeasuredValues(values)


class Sen5xI2cCmdGetTemperatureOffsetParameters(GetTemperatureOffsetParametersGenerated):
    """
    Get Temperature Offset Parameters I²C Command

    Gets the temperature offset parameters from the device.
    """

    def __init__(self, raw=False):
        """
        Constructor.

        :param bool raw:
            If ``False`` (the default), physical values are returned ([°C] for
            offset, [1] for slope). Otherwise the raw received integer values
            of offset (scaled with factor 200) and slope (scaled with factor
            10000) are returned.
        """
        super(Sen5xI2cCmdGetTemperatureOffsetParameters, self).__init__()
        self._raw = raw

    def interpret_response(self, data):
        """
        Validates the CRCs of the received data from the device and returns
        the interpreted data.

        :param bytes data:
            Received raw bytes from the read operation.
        :return:
            - offset (float/int) -
              Constant temperature offset.
            - slope (float/int) -
              Normalized temperature offset slope.
            - time_constant (int) -
              Time constant [s] how fast the slope and offset are applied.
              After the specified value in seconds, 63% of the new slope and
              offset are applied.
        :rtype: tuple
        :raise ~sensirion_i2c_driver.errors.I2cChecksumError:
            If a received CRC was wrong.
        """
        offset, slope, time_constant = \
            GetTemperatureOffsetParametersGenerated.interpret_response(self, data)
        if self._raw:
            return offset, slope, time_constant
        else:
            return offset / 200.0, slope / 10000.0, time_constant


class Sen5xI2cCmdSetTemperatureOffsetParameters(SetTemperatureOffsetParametersGenerated):
    """
    Set Temperature Offset Parameters I²C Command

    Sets the temperature offset parameters for the device.

    .. note:: This configuration is volatile, i.e. the parameters will be
              reverted to their default value of zero after a device reset.
    """

    def __init__(self, offset, slope, time_constant, raw=False):
        """
        Constructor.

        :param float/int offset:
            Constant temperature offset. The default value is 0.
        :param float/int slope:
            Normalized temperature offset slope. The default value is 0.
        :param int time_constant:
            Time constant [s] how fast the new slope and offset will be
            applied. After the specified value in seconds, 63% of the new slope
            and offset are applied. A time constant of zero means the new
            values will be applied immediately (within the next measure
            interval of 1 second).
        :param bool raw:
            If ``False`` (the default), physical values are expected ([°C] for
            offset, [1] for slope). Otherwise, raw integer values are expected
            for offset (scaled with factor 200) and slope (scaled with factor
            10000).
        """
        super(Sen5xI2cCmdSetTemperatureOffsetParameters, self).__init__(
            offset if raw else round(offset * 200.0),
            slope if raw else round(slope * 10000.0),
            time_constant if raw else round(time_constant),
        )


class Sen5xI2cCmdGetWarmStartParameter(GetWarmStartParameterGenerated):
    """
    Get Warm Start Parameter I²C Command

    Gets the warm start parameter from the device.
    """

    def __init__(self, raw=False):
        """
        Constructor.

        :param bool raw:
            If ``False`` (the default), a normalized value in the range from
            0.0 (cold start) to 1.0 (warm start) is returned. Otherwise,
            the raw received integer value is returned (0..65535).
        """
        super(Sen5xI2cCmdGetWarmStartParameter, self).__init__()
        self._raw = raw

    def interpret_response(self, data):
        """
        Validates the CRCs of the received data from the device and returns
        the interpreted data.

        :param bytes data:
            Received raw bytes from the read operation.
        :return:
            Warm start parameter value.
        :rtype:
            float/int
        :raise ~sensirion_i2c_driver.errors.I2cChecksumError:
            If a received CRC was wrong.
        """
        warm_start = GetWarmStartParameterGenerated.interpret_response(self, data)
        return warm_start if self._raw else (warm_start / 65535.0)


class Sen5xI2cCmdSetWarmStartParameter(SetWarmStartParameterGenerated):
    """
    Set Warm Start Parameter I²C Command

    Sets the warm start parameter for the device.

    .. note:: This parameter can be changed in any state of the device (and the
              getter immediately returns the new value), but it is applied only
              the next time starting a measurement, i.e. when sending a "Start
              Measurement" command! So the parameter needs to be set *before* a
              warm-start measurement is started.

    .. note:: This configuration is volatile, i.e. the parameter will be
              reverted to its default value of zero after a device reset.
    """

    def __init__(self, warm_start, raw=False):
        """
        Constructor.

        :param float/int warm_start:
            Warm start parameter value. The default value is 0.
        :param bool raw:
            If ``False`` (the default), a normalized value in the range
            from 0.0 (cold start) to 1.0 (warm start) is expected. Otherwise
            a raw integer value is expected (0..65535).
        """
        super(Sen5xI2cCmdSetWarmStartParameter, self).__init__(
            warm_start if raw else round(warm_start * 65535.0)
        )


class Sen5xI2cCmdGetVersion(GetVersionGenerated):
    """
    Get Version I²C Command

    Gets the version information for the hardware, firmware and communication
    protocol.
    """

    def interpret_response(self, data):
        """
        Validates the CRCs of the received data from the device and returns
        the interpreted data.

        :param bytes data:
            Received raw bytes from the read operation.
        :return:
            The device version as an object.
        :rtype:
            ~sensirion_i2c_sen5x.response_types.Sen5xVersion
        :raise ~sensirion_i2c_driver.errors.I2cChecksumError:
            If a received CRC was wrong.
        """
        firmware_major, firmware_minor, firmware_debug, hardware_major, \
            hardware_minor, protocol_major, protocol_minor, _ = \
            GetVersionGenerated.interpret_response(self, data)
        return Sen5xVersion(
            firmware=Sen5xFirmwareVersion(
                major=firmware_major,
                minor=firmware_minor,
                debug=firmware_debug
            ),
            hardware=Sen5xHardwareVersion(
                major=hardware_major,
                minor=hardware_minor
            ),
            protocol=Sen5xProtocolVersion(
                major=protocol_major,
                minor=protocol_minor
            )
        )


class Sen5xI2cCmdReadDeviceStatus(ReadDeviceStatusGenerated):
    """
    Read Device Status I²C Command

    Reads the current device status flags.

    .. note:: The status flags of type "Error" are sticky, i.e. they are not
              cleared automatically even if the error condition no longer
              exists. So they can only be cleared manually with the command
              0xD210 "Read And Clear Device Status" or with a device reset. All
              other flags are not sticky, i.e. they are cleared automatically
              if the trigger condition disappears.
    """

    def interpret_response(self, data):
        """
        Validates the CRCs of the received data from the device and returns
        the interpreted data.

        :param bytes data:
            Received raw bytes from the read operation.
        :return:
            Device status as an object.
        :rtype:
            ~sensirion_i2c_sen5x.response_types.Sen5xDeviceStatus
        :raise ~sensirion_i2c_driver.errors.I2cChecksumError:
            If a received CRC was wrong.
        """
        value = ReadDeviceStatusGenerated.interpret_response(self, data)
        return Sen5xDeviceStatus(value)


class Sen5xI2cCmdReadAndClearDeviceStatus(ReadAndClearDeviceStatusGenerated):
    """
    Read And Clear Device Status I²C Command

    Reads the current device status (like command 0xD206 "Read Device Status")
    and afterwards clears all flags.
    """

    def interpret_response(self, data):
        """
        Validates the CRCs of the received data from the device and returns
        the interpreted data.

        :param bytes data:
            Received raw bytes from the read operation.
        :return:
            Device status as an object.
        :rtype:
            ~sensirion_i2c_sen5x.response_types.Sen5xDeviceStatus
        :raise ~sensirion_i2c_driver.errors.I2cChecksumError:
            If a received CRC was wrong.
        """
        value = ReadAndClearDeviceStatusGenerated.interpret_response(self, data)
        return Sen5xDeviceStatus(value)
