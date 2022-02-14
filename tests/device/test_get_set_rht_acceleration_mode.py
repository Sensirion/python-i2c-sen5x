# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_rht_acceleration_mode() and set_rht_acceleration_mode() work
    as expected.
    """
    result = device.set_rht_acceleration_mode(1)
    assert result is None

    mode = device.get_rht_acceleration_mode()
    assert type(mode) is int
    assert mode == 1
