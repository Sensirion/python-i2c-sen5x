# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xAirQualityIndex
import math


def test_ticks():
    obj = Sen5xAirQualityIndex(42)
    assert type(obj.ticks) is int
    assert obj.ticks == 42


def test_available():
    obj = Sen5xAirQualityIndex(42)
    assert type(obj.available) is bool
    assert obj.available is True


def test_not_available():
    obj = Sen5xAirQualityIndex(0x7FFF)
    assert type(obj.available) is bool
    assert obj.available is False


def test_scaled_available():
    obj = Sen5xAirQualityIndex(42)
    assert type(obj.scaled) is float
    assert obj.scaled == 4.2


def test_scaled_not_available():
    obj = Sen5xAirQualityIndex(0x7FFF)
    assert type(obj.scaled) is float
    assert math.isnan(obj.scaled)


def test_to_str_available():
    obj = Sen5xAirQualityIndex(42)
    assert str(obj) == "4.2"


def test_to_str_not_available():
    obj = Sen5xAirQualityIndex(0x7FFF)
    assert str(obj) == "N/A"
