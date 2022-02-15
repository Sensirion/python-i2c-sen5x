# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest
import time


@pytest.mark.needs_device
def test_normal_mode(device):
    """
    Test if read_data_ready() works as expected.
    """
    ready = device.read_data_ready()
    assert type(ready) is bool
    assert ready is False

    device.start_measurement()
    time.sleep(1.1)
    assert device.read_data_ready() is True
