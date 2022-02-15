# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xMeasuredValues, Sen5xMassConcentration, \
    Sen5xHumidity, Sen5xTemperature, Sen5xAirQualityIndex


def test_members():
    values = (11, 22, 33, 44, 55, 66, 77, 88)
    obj = Sen5xMeasuredValues(values)

    assert type(obj.values) is tuple
    assert obj.values == values

    assert type(obj.mass_concentration_1p0) is Sen5xMassConcentration
    assert obj.mass_concentration_1p0.ticks == 11

    assert type(obj.mass_concentration_2p5) is Sen5xMassConcentration
    assert obj.mass_concentration_2p5.ticks == 22

    assert type(obj.mass_concentration_4p0) is Sen5xMassConcentration
    assert obj.mass_concentration_4p0.ticks == 33

    assert type(obj.mass_concentration_10p0) is Sen5xMassConcentration
    assert obj.mass_concentration_10p0.ticks == 44

    assert type(obj.ambient_humidity) is Sen5xHumidity
    assert obj.ambient_humidity.ticks == 55

    assert type(obj.ambient_temperature) is Sen5xTemperature
    assert obj.ambient_temperature.ticks == 66

    assert type(obj.voc_index) is Sen5xAirQualityIndex
    assert obj.voc_index.ticks == 77

    assert type(obj.nox_index) is Sen5xAirQualityIndex
    assert obj.nox_index.ticks == 88


def test_to_str_explicit_default_separator():
    values = (11, 22, 33, 44, 55, 66, 77, 88)
    obj = Sen5xMeasuredValues(values)
    s = obj.to_str()
    assert type(s) is str


def test_to_str_explicit():
    values = (11, 22, 33, 44, 55, 66, 77, 88)
    obj = Sen5xMeasuredValues(values)
    s = obj.to_str(", ")
    assert type(s) is str


def test_to_str_implicit():
    values = (11, 22, 33, 44, 55, 66, 77, 88)
    obj = Sen5xMeasuredValues(values)
    assert str(obj) == obj.to_str()
