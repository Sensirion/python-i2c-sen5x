# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if set_voc_tuning_parameters() and get_voc_tuning_parameters() work
    as expected.
    """
    result = device.set_voc_tuning_parameters(110, 16, 12, 90, 40, 200)
    assert result is None

    parameters = device.get_voc_tuning_parameters()
    assert type(parameters) is tuple
    assert all([type(x) is int for x in parameters])
    assert parameters == (110, 16, 12, 90, 40, 200)
