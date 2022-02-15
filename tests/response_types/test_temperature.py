# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xTemperature
import math
import pytest


def test_ticks():
    obj = Sen5xTemperature(-4242)
    assert type(obj.ticks) is int
    assert obj.ticks == -4242


def test_available():
    obj = Sen5xTemperature(-4242)
    assert type(obj.available) is bool
    assert obj.available is True


def test_not_available():
    obj = Sen5xTemperature(0x7FFF)
    assert type(obj.available) is bool
    assert obj.available is False


def test_degrees_celsius_available():
    obj = Sen5xTemperature(-4242)
    assert type(obj.degrees_celsius) is float
    assert obj.degrees_celsius == -21.21


def test_degrees_celsius_not_available():
    obj = Sen5xTemperature(0x7FFF)
    assert type(obj.degrees_celsius) is float
    assert math.isnan(obj.degrees_celsius)


def test_degrees_fahrenheit_available():
    obj = Sen5xTemperature(-4242)
    assert type(obj.degrees_fahrenheit) is float
    assert obj.degrees_fahrenheit == pytest.approx(-6.178)


def test_degrees_fahrenheit_not_available():
    obj = Sen5xTemperature(0x7FFF)
    assert type(obj.degrees_fahrenheit) is float
    assert math.isnan(obj.degrees_fahrenheit)


def test_to_str_available():
    obj = Sen5xTemperature(-4242)
    assert str(obj) == "-21.21 °C"


def test_to_str_not_available():
    obj = Sen5xTemperature(0x7FFF)
    assert str(obj) == "N/A"
