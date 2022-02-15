# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if device_reset() works as expected by changing a volatile setting,
    perform the reset, and then verifying that the setting was reset to its
    default value.
    """
    # Change fan auto cleaning interval.
    init_value = device.get_fan_auto_cleaning_interval()
    device.set_fan_auto_cleaning_interval(init_value + 1)
    assert device.get_fan_auto_cleaning_interval() == init_value + 1

    # Reset device -> should restore the default fan auto cleaning interval.
    result = device.device_reset()
    assert result is None

    # Check if the fan auto cleaning interval was reset.
    assert device.get_fan_auto_cleaning_interval() == init_value
