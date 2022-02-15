# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test_no_arg(device):
    """
    Test if get_temperature_offset_parameters() and
    set_temperature_offset_parameters() work as expected when not passing the
    raw parameter.
    """
    result = device.set_temperature_offset_parameters(1.2, 0.34, 5.6)
    assert result is None

    offset, slope, time_constant = device.get_temperature_offset_parameters()
    assert type(offset) is float
    assert type(slope) is float
    assert type(time_constant) is int
    assert offset == 1.2
    assert slope == 0.34
    assert time_constant == 6


@pytest.mark.needs_device
def test_raw_false(device):
    """
    Test if get_temperature_offset_parameters() and
    set_temperature_offset_parameters() work as expected when passing
    raw=False.
    """
    result = device.set_temperature_offset_parameters(1.2, 0.34, 5.6,
                                                      raw=False)
    assert result is None

    offset, slope, time_constant = \
        device.get_temperature_offset_parameters(raw=False)
    assert type(offset) is float
    assert type(slope) is float
    assert type(time_constant) is int
    assert offset == 1.2
    assert slope == 0.34
    assert time_constant == 6

    # Check scaling
    offset, slope, time_constant = \
        device.get_temperature_offset_parameters(raw=True)
    assert offset == 240
    assert slope == 3400
    assert time_constant == 6


@pytest.mark.needs_device
def test_raw_true(device):
    """
    Test if get_temperature_offset_parameters() and
    set_temperature_offset_parameters() work as expected when passing
    raw=True.
    """
    result = device.set_temperature_offset_parameters(11, 22, 33, raw=True)
    assert result is None

    offset, slope, time_constant = \
        device.get_temperature_offset_parameters(raw=True)
    assert type(offset) is int
    assert type(slope) is int
    assert type(time_constant) is int
    assert offset == 11
    assert slope == 22
    assert time_constant == 33

    # Check scaling
    offset, slope, time_constant = \
        device.get_temperature_offset_parameters(raw=False)
    assert offset == pytest.approx(0.055)
    assert slope == pytest.approx(0.0022)
    assert time_constant == 33
