API Reference
=============


Sen5xI2cDevice
--------------

.. automodule:: sensirion_i2c_sen5x.device


Sen5xMeasuredValues
-------------------

.. autoclass:: sensirion_i2c_sen5x.measured_values.Sen5xMeasuredValues


Response Data Types
-------------------

Sen5xMassConcentration
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xMassConcentration

Sen5xHumidity
^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xHumidity

Sen5xTemperature
^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xTemperature

Sen5xAirQualityIndex
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xAirQualityIndex

Sen5xDeviceStatus
^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xDeviceStatus

Sen5xVersion
^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xVersion
.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xFirmwareVersion
.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xHardwareVersion
.. autoclass:: sensirion_i2c_sen5x.response_types.Sen5xProtocolVersion


Commands
--------

CmdStartMeasurement
^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStartMeasurement

CmdStartMeasurementWithoutPm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStartMeasurementWithoutPm

CmdStopMeasurement
^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStopMeasurement

CmdReadDataReady
^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadDataReady

CmdReadMeasuredValues
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadMeasuredValues

CmdGetTemperatureOffsetParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdGetTemperatureOffsetParameters

CmdSetTemperatureOffsetParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdSetTemperatureOffsetParameters

CmdGetWarmStartParameter
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdGetWarmStartParameter

CmdSetWarmStartParameter
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdSetWarmStartParameter

CmdGetRhtAccelerationMode
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetRhtAccelerationMode

CmdSetRhtAccelerationMode
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetRhtAccelerationMode

CmdGetVocAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetVocAlgorithmTuningParameters

CmdSetVocAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetVocAlgorithmTuningParameters

CmdGetNoxAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetNoxAlgorithmTuningParameters

CmdSetNoxAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetNoxAlgorithmTuningParameters

CmdGetVocAlgorithmState
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetVocAlgorithmState

CmdSetVocAlgorithmState
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetVocAlgorithmState

CmdStartFanCleaning
^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStartFanCleaning

CmdGetFanAutoCleaningInterval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetFanAutoCleaningInterval

CmdSetFanAutoCleaningInterval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetFanAutoCleaningInterval

CmdGetProductName
^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetProductName

CmdGetSerialNumber
^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetSerialNumber

CmdGetVersion
^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdGetVersion

CmdReadDeviceStatus
^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadDeviceStatus

CmdReadAndClearDeviceStatus
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadAndClearDeviceStatus

CmdDeviceReset
^^^^^^^^^^^^^^

.. autoclass:: sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdDeviceReset
