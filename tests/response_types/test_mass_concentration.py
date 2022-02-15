# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xMassConcentration
import math


def test_ticks():
    obj = Sen5xMassConcentration(42)
    assert type(obj.ticks) is int
    assert obj.ticks == 42


def test_available():
    obj = Sen5xMassConcentration(42)
    assert type(obj.available) is bool
    assert obj.available is True


def test_not_available():
    obj = Sen5xMassConcentration(0xFFFF)
    assert type(obj.available) is bool
    assert obj.available is False


def test_physical_available():
    obj = Sen5xMassConcentration(42)
    assert type(obj.physical) is float
    assert obj.physical == 4.2


def test_physical_not_available():
    obj = Sen5xMassConcentration(0xFFFF)
    assert type(obj.physical) is float
    assert math.isnan(obj.physical)


def test_to_str_available():
    obj = Sen5xMassConcentration(42)
    assert str(obj) == "4.2 µg/m^3"


def test_to_str_not_available():
    obj = Sen5xMassConcentration(0xFFFF)
    assert str(obj) == "N/A"
