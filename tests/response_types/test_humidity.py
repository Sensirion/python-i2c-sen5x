# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xHumidity
import math


def test_ticks():
    obj = Sen5xHumidity(-1337)
    assert type(obj.ticks) is int
    assert obj.ticks == -1337


def test_available():
    obj = Sen5xHumidity(-1337)
    assert type(obj.available) is bool
    assert obj.available is True


def test_not_available():
    obj = Sen5xHumidity(0x7FFF)
    assert type(obj.available) is bool
    assert obj.available is False


def test_percent_rh_available():
    obj = Sen5xHumidity(-1337)
    assert type(obj.percent_rh) is float
    assert obj.percent_rh == -13.37


def test_percent_rh_not_available():
    obj = Sen5xHumidity(0x7FFF)
    assert type(obj.percent_rh) is float
    assert math.isnan(obj.percent_rh)


def test_to_str_available():
    obj = Sen5xHumidity(-1337)
    assert str(obj) == "-13.37 %RH"


def test_to_str_not_available():
    obj = Sen5xHumidity(0x7FFF)
    assert str(obj) == "N/A"
