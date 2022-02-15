# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_serial_number() returns the expected value.
    """
    serial_number = device.get_serial_number()
    assert type(serial_number) is str
    assert 0 < len(serial_number) < 32
