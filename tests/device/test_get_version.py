# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xVersion
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_version() returns the expected value.
    """
    version = device.get_version()
    assert type(version) is Sen5xVersion
    assert version.firmware.major >= 0
    assert version.firmware.minor >= 0
    assert version.firmware.debug in [True, False]
    assert version.hardware.major >= 1
    assert version.hardware.minor >= 0
    assert version.protocol.major == 1
    assert version.protocol.minor == 0
