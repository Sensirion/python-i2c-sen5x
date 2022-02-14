# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xMeasuredValues
import pytest
import time


@pytest.mark.needs_device
def test_idle_mode(device):
    """
    Test if read_measured_values() work as expected in idle mode.
    """
    values = device.read_measured_values()
    assert type(values) is Sen5xMeasuredValues
    assert values.mass_concentration_1p0.available is False
    assert values.mass_concentration_2p5.available is False
    assert values.mass_concentration_4p0.available is False
    assert values.mass_concentration_10p0.available is False
    assert values.ambient_humidity.available is False
    assert values.ambient_temperature.available is False
    assert values.voc_index.available is False
    assert values.nox_index.available is False


@pytest.mark.needs_device
def test_measure_mode(device):
    """
    Test if read_measured_values() work as expected in measure mode.
    """
    device.start_measurement()
    time.sleep(1.1)
    values = device.read_measured_values()
    assert type(values) is Sen5xMeasuredValues
    assert 0.0 <= values.mass_concentration_1p0.physical <= 500.0
    assert 0.0 <= values.mass_concentration_2p5.physical <= 500.0
    assert 0.0 <= values.mass_concentration_4p0.physical <= 500.0
    assert 0.0 <= values.mass_concentration_10p0.physical <= 500.0
    assert 10.0 <= values.ambient_humidity.percent_rh <= 90.0
    assert 10.0 <= values.ambient_temperature.degrees_celsius <= 40.0
    if values.voc_index.available:
        assert 0.0 <= values.voc_index.scaled <= 500.0
    if values.nox_index.available:
        assert 0.0 <= values.nox_index.scaled <= 500.0
