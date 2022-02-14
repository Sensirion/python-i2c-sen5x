# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x import Sen5xDeviceStatus
import pytest


@pytest.mark.needs_device
def test_no_args(device):
    """
    Test if read_device_status() without argument returns the expected value
    and does not clear the status.
    """
    status = device.read_device_status()
    assert type(status) is Sen5xDeviceStatus
    assert status.value == 0

    device.start_measurement()
    device.start_fan_cleaning()
    assert device.read_device_status().fan_cleaning is True
    assert device.read_device_status().fan_cleaning is True  # Not cleared.


@pytest.mark.needs_device
def test_without_clear(device):
    """
    Test if read_device_status() with clear=False returns the expected value
    and does not clear the status.
    """
    device.start_measurement()
    device.start_fan_cleaning()
    assert device.read_device_status(False).fan_cleaning is True
    assert device.read_device_status().fan_cleaning is True  # Not cleared.


@pytest.mark.needs_device
def test_with_clear(device):
    """
    Test if read_device_status() with clear=True returns the expected value
    and clears the status.
    """
    device.start_measurement()
    device.start_fan_cleaning()
    assert device.read_device_status(True).fan_cleaning is True
    assert device.read_device_status().fan_cleaning is False  # Cleared.
