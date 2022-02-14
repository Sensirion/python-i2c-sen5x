# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test_no_arg(device):
    """
    Test if get_warm_start_parameter() and set_warm_start_parameter() work as
    expected when not passing the raw parameter.
    """
    result = device.set_warm_start_parameter(0.7)
    assert result is None

    parameter = device.get_warm_start_parameter()
    assert type(parameter) is float
    assert parameter == pytest.approx(0.7, abs=1e-5)


@pytest.mark.needs_device
def test_raw_false(device):
    """
    Test if get_warm_start_parameter() and set_warm_start_parameter() work as
    expected when passing raw=False.
    """
    result = device.set_warm_start_parameter(0.8, raw=False)
    assert result is None

    parameter = device.get_warm_start_parameter(raw=False)
    assert type(parameter) is float
    assert parameter == pytest.approx(0.8, abs=1e-5)

    # Check scaling
    parameter = device.get_warm_start_parameter(raw=True)
    assert parameter == 52428


@pytest.mark.needs_device
def test_raw_true(device):
    """
    Test if get_warm_start_parameter() and set_warm_start_parameter() work as
    expected when passing raw=True.
    """
    result = device.set_warm_start_parameter(12345, raw=True)
    assert result is None

    parameter = device.get_warm_start_parameter(raw=True)
    assert type(parameter) is int
    assert parameter == 12345

    # Check scaling
    parameter = device.get_warm_start_parameter(raw=False)
    assert parameter == pytest.approx(0.188372625, abs=1e-5)
