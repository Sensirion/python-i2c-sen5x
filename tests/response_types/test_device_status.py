# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x.response_types import Sen5xDeviceStatus


def test_zero():
    obj = Sen5xDeviceStatus(0x00000000)
    assert type(obj.value) is int
    assert obj.value == 0
    assert obj.flags == []
    assert obj.fan_error is False
    assert obj.laser_error is False
    assert obj.sht_error is False
    assert obj.sgp_error is False
    assert obj.fan_cleaning is False
    assert obj.fan_speed_out_of_specs is False
    assert str(obj) == "0x00000000 [OK]"


def test_fan_error():
    obj = Sen5xDeviceStatus(0x00000010)
    assert obj.value == 0x00000010
    assert obj.flags == ['fan_error']
    assert obj.fan_error is True
    assert obj.laser_error is False
    assert obj.sht_error is False
    assert obj.sgp_error is False
    assert obj.fan_cleaning is False
    assert obj.fan_speed_out_of_specs is False


def test_laser_error():
    obj = Sen5xDeviceStatus(0x00000020)
    assert obj.value == 0x00000020
    assert obj.flags == ['laser_error']
    assert obj.fan_error is False
    assert obj.laser_error is True
    assert obj.sht_error is False
    assert obj.sgp_error is False
    assert obj.fan_cleaning is False
    assert obj.fan_speed_out_of_specs is False


def test_sht_error():
    obj = Sen5xDeviceStatus(0x00000040)
    assert obj.value == 0x00000040
    assert obj.flags == ['sht_error']
    assert obj.fan_error is False
    assert obj.laser_error is False
    assert obj.sht_error is True
    assert obj.sgp_error is False
    assert obj.fan_cleaning is False
    assert obj.fan_speed_out_of_specs is False


def test_sgp_error():
    obj = Sen5xDeviceStatus(0x00000080)
    assert obj.value == 0x00000080
    assert obj.flags == ['sgp_error']
    assert obj.fan_error is False
    assert obj.laser_error is False
    assert obj.sht_error is False
    assert obj.sgp_error is True
    assert obj.fan_cleaning is False
    assert obj.fan_speed_out_of_specs is False


def test_fan_cleaning():
    obj = Sen5xDeviceStatus(0x00080000)
    assert obj.value == 0x00080000
    assert obj.flags == ['fan_cleaning']
    assert obj.fan_error is False
    assert obj.laser_error is False
    assert obj.sht_error is False
    assert obj.sgp_error is False
    assert obj.fan_cleaning is True
    assert obj.fan_speed_out_of_specs is False


def test_fan_speed_out_of_specs():
    obj = Sen5xDeviceStatus(0x00200000)
    assert obj.value == 0x00200000
    assert obj.flags == ['fan_speed_out_of_specs']
    assert obj.fan_error is False
    assert obj.laser_error is False
    assert obj.sht_error is False
    assert obj.sgp_error is False
    assert obj.fan_cleaning is False
    assert obj.fan_speed_out_of_specs is True


def test_multiple_flags():
    obj = Sen5xDeviceStatus(0x00080011)
    assert obj.value == 0x00080011
    assert obj.flags == ['fan_error', 'fan_cleaning']
    assert obj.fan_error is True
    assert obj.laser_error is False
    assert obj.sht_error is False
    assert obj.sgp_error is False
    assert obj.fan_cleaning is True
    assert obj.fan_speed_out_of_specs is False


def test_to_str():
    obj = Sen5xDeviceStatus(0x00080010)
    assert str(obj) == "0x00080010 [fan_error, fan_cleaning]"
