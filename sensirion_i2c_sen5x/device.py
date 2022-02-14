# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_driver import I2cDevice
from .commands import \
    Sen5xI2cCmdDeviceReset, \
    Sen5xI2cCmdGetFanAutoCleaningInterval, \
    Sen5xI2cCmdGetNoxAlgorithmTuningParameters, \
    Sen5xI2cCmdGetProductName, \
    Sen5xI2cCmdGetRhtAccelerationMode, \
    Sen5xI2cCmdGetSerialNumber, \
    Sen5xI2cCmdGetTemperatureOffsetParameters, \
    Sen5xI2cCmdGetVersion, \
    Sen5xI2cCmdGetVocAlgorithmState, \
    Sen5xI2cCmdGetVocAlgorithmTuningParameters, \
    Sen5xI2cCmdGetWarmStartParameter, \
    Sen5xI2cCmdReadAndClearDeviceStatus, \
    Sen5xI2cCmdReadDataReady, \
    Sen5xI2cCmdReadDeviceStatus, \
    Sen5xI2cCmdReadMeasuredValues, \
    Sen5xI2cCmdSetFanAutoCleaningInterval, \
    Sen5xI2cCmdSetNoxAlgorithmTuningParameters, \
    Sen5xI2cCmdSetRhtAccelerationMode, \
    Sen5xI2cCmdSetTemperatureOffsetParameters, \
    Sen5xI2cCmdSetVocAlgorithmState, \
    Sen5xI2cCmdSetVocAlgorithmTuningParameters, \
    Sen5xI2cCmdSetWarmStartParameter, \
    Sen5xI2cCmdStartFanCleaning, \
    Sen5xI2cCmdStartMeasurement, \
    Sen5xI2cCmdStartMeasurementWithoutPm, \
    Sen5xI2cCmdStopMeasurement

import logging
log = logging.getLogger(__name__)


class Sen5xI2cDevice(I2cDevice):
    """
    SEN5x I²C device.

    This is a low-level driver which just provides all I²C commands as Python
    methods. Typically, calling a method sends one I²C request to the device
    and interprets its response (if any).

    There is no caching functionality in this driver. For example if you call
    :func:`get_serial_number` 100 times, it will send the command 100 times
    over the I²C interface to the device. This makes the driver completely
    stateless.
    """

    def __init__(self, connection, slave_address=0x69):
        """
        Constructs a new SEN5x I²C device.

        :param ~sensirion_i2c_driver.connection.I2cConnection connection:
            The I²C connection to use for communication.
        :param byte slave_address:
            The I²C slave address, defaults to 0x69.
        """
        super(Sen5xI2cDevice, self).__init__(connection, slave_address)

    def get_product_name(self):
        """
        Get the product name of the device.

        :return:
            The product name as an ASCII string.
        :rtype:
            string
        """
        return self.execute(Sen5xI2cCmdGetProductName())

    def get_serial_number(self):
        """
        Get the serial number of the device.

        :return:
            The serial number as an ASCII string.
        :rtype:
            string
        """
        return self.execute(Sen5xI2cCmdGetSerialNumber())

    def get_version(self):
        """
        Get the version of the device firmware, hardware and communication
        protocol.

        :return:
            The device version.
        :rtype:
            ~sensirion_i2c_sen5x.response_types.Sen5xVersion
        """
        return self.execute(Sen5xI2cCmdGetVersion())

    def read_device_status(self, clear=False):
        """
        Read and optionally clear the device status.

        :param bool clear:
            If ``True``, the status flags on the device get cleared after
            reading them. Defaults to ``False``.
        :return:
            The device status as an object containing all status flags.
        :rtype:
            ~sensirion_i2c_sen5x.response_types.Sen5xDeviceStatus
        """
        return self.execute(
            Sen5xI2cCmdReadAndClearDeviceStatus() if clear
            else Sen5xI2cCmdReadDeviceStatus())

    def device_reset(self):
        """
        Execute a device reset (reboot firmware, similar to power cycle).
        """
        return self.execute(Sen5xI2cCmdDeviceReset())

    def start_measurement(self):
        """
        Starts a continuous measurement.

        .. note::

            After starting the measurement, it takes some time (~1s) until the
            first measurement results are available. You could poll with the
            method
            :py:meth:`~sensirion_i2c_sen5x.device.Sen5xI2cDevice.read_data_ready()`
            to check when the results are ready to read.

        .. note::

            If the device is in measure mode without particulate matter
            (low-power) and the firmware version is at least 2.0, this command
            enables PM measurement without affecting the already running
            RH/T/VOC/NOx measurements (except that the "data ready"-flag will
            be cleared). In previous firmware versions, this command is
            supported only in idle mode.
        """
        return self.execute(Sen5xI2cCmdStartMeasurement())

    def start_measurement_without_pm(self):
        """
        Start a continuous measurement without particulate matter (low-power).

        Only RH/T/VOC/NOx are measured in this mode, particulate matter is
        disabled to reduce power consumption.

        .. note::

            After starting the measurement, it takes some time (~1s) until the
            first measurement results are available. You could poll with the
            method
            :py:meth:`~sensirion_i2c_sen5x.device.Sen5xI2cDevice.read_data_ready()`
            to check when the results are ready to read.

        .. note::

            If the device is in measure mode with particulate matter
            (normal measure mode) and the firmware version is at least 2.0,
            this command disables PM measurement without affecting the already
            running RH/T/VOC/NOx measurements (except that the
            "data ready"-flag will be cleared). In previous firmware versions,
            this command is supported only in idle mode.

        .. attention:: SEN50 does not support this feature.
        """
        return self.execute(Sen5xI2cCmdStartMeasurementWithoutPm())

    def stop_measurement(self):
        """
        Stop the running measurement.

        Leaves the measure mode and returns to the idle mode.

        If the device is already in idle mode, this command has no effect.
        """
        return self.execute(Sen5xI2cCmdStopMeasurement())

    def read_data_ready(self):
        """
        Read the data ready flag.

        This command can be used to check if new measurement results are ready
        to read. The data ready flag is automatically reset after reading the
        measured values with
        :py:meth:`~sensirion_i2c_sen5x.device.Sen5xI2cDevice.read_measured_values()`.

        .. note::

            During fan (auto-)cleaning, no measurement data is available for
            several seconds and thus this flag will not be set until cleaning
            has finished. So please expect gaps of several seconds at any
            time if fan auto-cleaning is enabled.

        :return:
            ``True`` if new data is ready, ``False`` if not. When no
            measurement is running, ``False`` will be returned.
        :rtype:
            bool
        """
        return self.execute(Sen5xI2cCmdReadDataReady())

    def read_measured_values(self):
        """
        Read the measured mass concentration, RH/T and VOC/NOx values.

        .. note::

            The method
            :py:meth:`~sensirion_i2c_sen5x.device.Sen5xI2cDevice.read_data_ready()`
            can be used to check if new data is available since the last read
            operation. If no new data is available, the previous values will be
            returned again. If no data is available at all (no measurement
            running or immediately after starting the measurement), the
            returned object will not contain any measurement results (property
            ``available`` of all values is ``False``).

        .. attention::

            The returned object always contains all measurement signals, but
            it depends on the measure mode and the product which signal values
            are actually available. See
            :py:class:`~sensirion_i2c_sen5x.measured_values.Sen5xMeasuredValues`
            for details how it handles values which are not available. In
            particular, mass concentration values are not available in the
            low-power measure mode, RH/T/VOC are not available with SEN50
            and NOx is not available with SEN50 and SEN54. In idle mode,
            no signal values will be available at all.

        :return:
            The latest measurement results.
        :rtype:
            :py:class:`~sensirion_i2c_sen5x.measured_values.Sen5xMeasuredValues`
        """
        return self.execute(Sen5xI2cCmdReadMeasuredValues())

    def get_temperature_offset_parameters(self, raw=False):
        """
        Get the temperature offset parameters of the device.

        .. attention:: SEN50 does not support this feature.

        :param bool raw:
            If ``False`` (the default), physical/normalized values (offset in
            °C, slope with scale factor 1, time constant in seconds) are
            returned. Otherwise the raw received integer values of offset
            (scaled with factor 200) and slope (scaled with factor 10000)
            are returned.
        :return:
            Tuple with offset (°C or ticks), slope (scale factor 1 or 10000)
            and time constant [s].
        :rtype:
            float/int, float/int, int
        """
        return self.execute(Sen5xI2cCmdGetTemperatureOffsetParameters(raw))

    def set_temperature_offset_parameters(self, offset, slope,
                                          time_constant_s, raw=False):
        """
        Set the temperature offset parameters of the device.

        This command allows to compensate temperature effects of the
        design-in at customer side by applying a custom temperature offset
        to the ambient temperature. The compensated ambient temperature is
        calculated as follows:

        ::

            T_Ambient_Compensated = T_Ambient + offset + (slope * T_Ambient)

        Where ``slope`` and ``offset`` are the values set with this command,
        smoothed with the specified time constant.

        All temperatures (``T_Ambient_Compensated``, ``T_Ambient`` and
        ``offset``) in this formula are represented in °C.

        .. note:: This configuration is volatile, i.e. it will be reverted to
                  the default value after a device reset.

        .. attention:: SEN50 does not support this feature.

        :param float/int offset:
            Constant temperature offset (°C or ticks). The default value is 0.
        :param float/int slope:
            Normalized temperature offset slope (scale factor 1 or 10000).
            The default value is 0.
        :param int time_constant:
            Time constant [s] how fast the new slope and offset will be
            applied. After the specified value in seconds, 63% of the new slope
            and offset are applied. A time constant of zero means the new
            values will be applied immediately (within the next measure
            interval of 1 second).
        :param bool raw:
            If ``False`` (the default), physical/normalized values are
            expected (offset in °C, slope with scale factor 1, time constant
            in seconds). Otherwise, raw integer values are expected for
            offset (scaled with factor 200) and slope (scaled with factor
            10000).
        """
        return self.execute(Sen5xI2cCmdSetTemperatureOffsetParameters(
            offset, slope, time_constant_s, raw))

    def get_warm_start_parameter(self, raw=False):
        """
        Get the warm start parameter of the device.

        .. attention:: SEN50 does not support this feature.

        :param bool raw:
            If ``False`` (the default), a normalized value in the range from
            0.0 (cold start) to 1.0 (warm start) is returned. Otherwise
            the raw received integer value is returned (0..65535).
        :return:
            Warm start parameter value (0..1 or 0..65535).
        :rtype:
            float/int
        """
        return self.execute(Sen5xI2cCmdGetWarmStartParameter(raw))

    def set_warm_start_parameter(self, warm_start, raw=False):
        """
        Set the warm start parameter of the device.

        The temperature compensation algorithm is optimized for a cold start
        by default, i.e. it is assumed that the "Start Measurement" command
        is called on a device not already warmed up by previous measurements.
        If the measurement is started on a device already warmed up, this
        parameter can be used to improve the accuracy of the ambient
        temperature output.

        .. note::

            This parameter can be changed in any state of the device (and the
            getter immediately returns the new value), but it is applied only
            the next time starting a measurement, i.e. when sending a "Start
            Measurement" command! So the parameter needs to be set *before* a
            warm-start measurement is started.

        .. note:: This configuration is volatile, i.e. it will be reverted to
                  the default value after a device reset.

        .. attention:: SEN50 does not support this feature.

        :param float/int warm_start:
            Warm start parameter value (0..1 or 0..65535).
        :param bool raw:
            If ``False`` (the default), a normalized value in the range from
            0.0 (cold start) to 1.0 (warm start) is expected. Otherwise
            a raw integer value is expected (0..65535).
        """
        return self.execute(Sen5xI2cCmdSetWarmStartParameter(warm_start, raw))

    def get_rht_acceleration_mode(self):
        """
        Get the RH/T acceleration mode of the device.

        .. attention:: SEN50 does not support this feature.

        :return:
            The current RH/T acceleration mode. See
            :py:meth:`~sensirion_i2c_sen5x.device.Sen5xI2cDevice.set_rht_acceleration_mode()`
            for the list of available modes.
        :rtype:
            int
        """
        return self.execute(Sen5xI2cCmdGetRhtAccelerationMode())

    def set_rht_acceleration_mode(self, mode):
        """
        Set the RH/T acceleration mode of the device.

        By default, the RH/T acceleration algorithm is optimized for a sensor
        which is positioned in free air. If the sensor is integrated into
        another device, the ambient RH/T output values might not be optimal
        due to different thermal behavior. This parameter can be used to
        adapt the RH/T acceleration behavior for the actual use-case, leading
        in an improvement of the ambient RH/T output accuracy. There is a
        limited set of different modes available, each identified by a number:

        - ``0``: Default / Air Purifier / IAQ (slow)
        - ``1``: IAQ (fast)
        - ``2``: IAQ (medium)

        .. note::

            This parameter can be changed in any state of the device (and the
            getter immediately returns the new value), but it is applied only
            the next time starting a measurement, i.e. when sending a "Start
            Measurement" command. So the parameter needs to be set *before* a
            new measurement is started.

        .. note:: This configuration is volatile, i.e. it will be reverted to
                  the default value after a device reset.

        .. attention:: SEN50 does not support this feature.

        :param int mode:
            The new RH/T acceleration mode. The default is 0.
        """
        return self.execute(Sen5xI2cCmdSetRhtAccelerationMode(mode))

    def get_voc_tuning_parameters(self):
        """
        Get the currently set parameters for customizing the VOC algorithm.

        .. attention:: SEN50 does not support this feature.

        :return:
            - index_offset (int) -
              VOC index representing typical (average) conditions.
            - learning_time_offset_hours (int) -
              Time constant to estimate the VOC algorithm offset from the
              history in hours. Past events will be forgotten after about twice
              the learning time.
            - learning_time_gain_hours (int) -
              Time constant to estimate the VOC algorithm gain from the history
              in hours. Past events will be forgotten after about twice the
              learning time.
            - gating_max_duration_minutes (int) -
              Maximum duration of gating in minutes (freeze of estimator during
              high VOC index signal). Zero disables the gating.
            - std_initial (int) -
              Initial estimate for standard deviation. Lower value boosts
              events during initial learning period, but may result in larger
              device-to-device variations.
            - gain_factor (int) -
              Gain factor to amplify or to attenuate the VOC index output.
        :rtype:
            tuple
        """
        return self.execute(Sen5xI2cCmdGetVocAlgorithmTuningParameters())

    def set_voc_tuning_parameters(self, index_offset,
                                  learning_time_offset_hours,
                                  learning_time_gain_hours,
                                  gating_max_duration_minutes, std_initial,
                                  gain_factor):
        """
        Sets parameters to customize the VOC algorithm.

        .. note:: This command is available only in idle mode. In measure mode,
                  this command has no effect. In addition, it has no effect if
                  at least one parameter is outside the specified range.

        .. note:: This configuration is volatile, i.e. it will be reverted to
                  the default value after a device reset.

        .. attention:: SEN50 does not support this feature.

        :param int index_offset:
            VOC index representing typical (average) conditions. Allowed values
            are in range 1..250. The default value is 100.
        :param int learning_time_offset_hours:
            Time constant to estimate the VOC algorithm offset from the history
            in hours. Past events will be forgotten after about twice the
            learning time. Allowed values are in range 1..1000. The default
            value is 12 hours.
        :param int learning_time_gain_hours:
            Time constant to estimate the VOC algorithm gain from the history
            in hours. Past events will be forgotten after about twice the
            learning time. Allowed values are in range 1..1000. The default
            value is 12 hours.
        :param int gating_max_duration_minutes:
            Maximum duration of gating in minutes (freeze of estimator during
            high VOC index signal). Set to zero to disable the gating. Allowed
            values are in range 0..3000. The default value is 180 minutes.
        :param int std_initial:
            Initial estimate for standard deviation. Lower value boosts events
            during initial learning period, but may result in larger
            device-to-device variations. Allowed values are in range 10..5000.
            The default value is 50.
        :param int gain_factor:
            Gain factor to amplify or to attenuate the VOC index output.
            Allowed values are in range 1..1000. The default value is 230.
        """
        return self.execute(Sen5xI2cCmdSetVocAlgorithmTuningParameters(
            index_offset, learning_time_offset_hours,
            learning_time_gain_hours, gating_max_duration_minutes,
            std_initial, gain_factor))

    def get_nox_tuning_parameters(self):
        """
        Get the currently set parameters for customizing the NOx algorithm.

        .. attention:: SEN50 and SEN54 do not support this feature.

        :return:
            - index_offset (int) -
              NOx index representing typical (average) conditions.
            - learning_time_offset_hours (int) -
              Time constant to estimate the NOx algorithm offset from the
              history in hours. Past events will be forgotten after about twice
              the learning time.
            - learning_time_gain_hours (int) -
              The time constant to estimate the NOx algorithm gain from the
              history has no impact for NOx. This parameter is still in place
              for consistency reasons with the VOC tuning parameters command.
            - gating_max_duration_minutes (int) -
              Maximum duration of gating in minutes (freeze of estimator during
              high NOx index signal). Zero disables the gating.
            - std_initial (int) -
              The initial estimate for standard deviation has no impact for
              NOx. This parameter is still in place for consistency reasons
              with the VOC tuning parameters command.
            - gain_factor (int) -
              Gain factor to amplify or to attenuate the NOx index output.
        :rtype:
            tuple
        """
        return self.execute(Sen5xI2cCmdGetNoxAlgorithmTuningParameters())

    def set_nox_tuning_parameters(self, index_offset,
                                  learning_time_offset_hours,
                                  learning_time_gain_hours,
                                  gating_max_duration_minutes, std_initial,
                                  gain_factor):
        """
        Sets parameters to customize the NOx algorithm.

        .. note:: This command is available only in idle mode. In measure mode,
                  this command has no effect. In addition, it has no effect if
                  at least one parameter is outside the specified range.

        .. note:: This configuration is volatile, i.e. it will be reverted to
                  the default value after a device reset.

        .. attention:: SEN50 and SEN54 do not support this feature.

        :param int index_offset:
            NOx index representing typical (average) conditions. Allowed values
            are in range 1..250. The default value is 1.
        :param int learning_time_offset_hours:
            Time constant to estimate the NOx algorithm offset from the history
            in hours. Past events will be forgotten after about twice the
            learning time. Allowed values are in range 1..1000. The default
            value is 12 hours.
        :param int learning_time_gain_hours:
            The time constant to estimate the NOx algorithm gain from the
            history has no impact for NOx. This parameter is still in place for
            consistency reasons with the VOC tuning parameters command. This
            parameter must always be set to 12 hours.
        :param int gating_max_duration_minutes:
            Maximum duration of gating in minutes (freeze of estimator during
            high NOx index signal). Set to zero to disable the gating. Allowed
            values are in range 0..3000. The default value is 720 minutes.
        :param int std_initial:
            The initial estimate for standard deviation parameter has no impact
            for NOx. This parameter is still in place for consistency reasons
            with the VOC tuning parameters command. This parameter must always
            be set to 50.
        :param int gain_factor:
            Gain factor to amplify or to attenuate the NOx index output.
            Allowed values are in range 1..1000. The default value is 230.
        """
        return self.execute(Sen5xI2cCmdSetNoxAlgorithmTuningParameters(
            index_offset, learning_time_offset_hours,
            learning_time_gain_hours, gating_max_duration_minutes,
            std_initial, gain_factor))

    def get_voc_state(self):
        """
        Get the current VOC algorithm state.

        The returned data can be used to restore the state with the method
        :py:meth:`~sensirion_i2c_sen5x.device.Sen5xI2cDevice.set_voc_state()`
        to resume operation after a short power cycle or device reset,
        skipping the initial learning phase of the VOC algorithm.

        .. note::

            This command can be used either in measure mode or in idle mode
            (which will then return the state at the time when the measurement
            was stopped). In measure mode, the state can be read each measure
            interval to always have the latest state available, even in case of
            a sudden power loss.

        .. note:: This feature should only be used after at least 3 hours of
                  continuous operation.

        .. attention:: SEN50 does not support this feature.

        :return:
            Current VOC algorithm state.
        :rtype:
            bytes
        """
        return self.execute(Sen5xI2cCmdGetVocAlgorithmState())

    def set_voc_state(self, state):
        """
        Set/restore the VOC algorithm state.

        By default, the VOC algorithm resets its state to inital values
        each time a measurement is started, even if the measurement was stopped
        only for a short time. So the VOC index output value needs a long time
        until it is stable again. This can be avoided by restoring the
        algorithm state previously retrieved by
        :py:meth:`~sensirion_i2c_sen5x.device.Sen5xI2cDevice.get_voc_state()`
        before starting the measure mode.

        .. note::

            This command is only available in idle mode and the state
            will be applied only once when starting the next measurement. Any
            further measurements (i.e. when stopping and restarting the measure
            mode) will reset the state to initial values. In measure mode, this
            command has no effect.

        .. note:: This feature should not be used after interruptions of more
                  than 10 minutes.

        .. attention:: SEN50 does not support this feature.

        :param bytes state:
            VOC algorithm state to restore.
        """
        return self.execute(Sen5xI2cCmdSetVocAlgorithmState(state))

    def start_fan_cleaning(self):
        """
        Start fan cleaning.

        Starts the fan cleaning manually by applying the maximum fan speed
        for a few seconds. The "data ready"-flag will be cleared immediately
        and during the next few seconds, no new measurement results will be
        available (old values will be returned). Once the cleaning is finished,
        the "data ready"-flag will be set and new measurement results will be
        available.

        If you stop the measurement while fan cleaning is active, the cleaning
        will be aborted immediately.

        .. note:: This command is only available in measure mode with PM
                  measurement enabled, i.e. only if the fan is already running.
                  In any other state, this command does nothing. In addition,
                  when executing this command while cleaning is already active,
                  the command does nothing.
        """
        return self.execute(Sen5xI2cCmdStartFanCleaning())

    def get_fan_auto_cleaning_interval(self):
        """
        Get the fan auto cleaning interval of the device.

        The device will automatically start the fan cleaning when the fan was
        running for this number of seconds.

        :return:
            Fan auto cleaning interval [s]. Zero means auto cleaning is
            disabled.
        :rtype:
            int
        """
        return self.execute(Sen5xI2cCmdGetFanAutoCleaningInterval())

    def set_fan_auto_cleaning_interval(self, interval_s):
        """
        Set the fan auto cleaning interval of the device.

        The device will automatically start the fan cleaning when the fan was
        running for this number of seconds.

        .. note:: This configuration is volatile, i.e. it will be reverted to
                  the default value after a device reset.

        :param int interval_s:
            Fan auto cleaning interval [s]. Set to zero to disable auto
            cleaning. The default value is 604800 (1 week).
        """
        return self.execute(Sen5xI2cCmdSetFanAutoCleaningInterval(interval_s))
