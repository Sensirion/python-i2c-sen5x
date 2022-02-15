# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_voc_state() and set_voc_state() work as expected.
    """
    device.start_measurement()
    state = device.get_voc_state()
    assert type(state) is bytes
    assert len(state) == 8

    device.stop_measurement()
    result = device.set_voc_state(state)
    assert result is None
    assert device.get_voc_state() == state
