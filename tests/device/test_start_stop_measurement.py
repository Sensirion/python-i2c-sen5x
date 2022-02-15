# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest
import time


@pytest.mark.needs_device
def test_normal_mode(device):
    """
    Test if start_measurement() and stop_measurement() work as expected.
    """
    result = device.start_measurement()
    assert result is None
    time.sleep(1.1)
    assert device.read_data_ready() is True

    result = device.stop_measurement()
    assert result is None
    assert device.read_data_ready() is False


@pytest.mark.needs_device
def test_without_pm(device):
    """
    Test if start_measurement_without_pm() and stop_measurement() work as
    expected.
    """
    result = device.start_measurement_without_pm()
    assert result is None
    time.sleep(1.1)
    assert device.read_data_ready() is True

    result = device.stop_measurement()
    assert result is None
    assert device.read_data_ready() is False
