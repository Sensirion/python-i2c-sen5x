# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if start_fan_cleaning() works as expected.
    """
    device.start_measurement()
    result = device.start_fan_cleaning()
    assert result is None
    assert device.read_device_status().fan_cleaning is True
