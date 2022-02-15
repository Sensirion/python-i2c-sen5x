# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_fan_auto_cleaning_interval() and
    set_fan_auto_cleaning_interval() work as expected.
    """
    result = device.set_fan_auto_cleaning_interval(42)
    assert result is None

    interval = device.get_fan_auto_cleaning_interval()
    assert type(interval) is int
    assert interval == 42
