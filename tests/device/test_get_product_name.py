# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_product_name() returns the expected value.
    """
    product_name = device.get_product_name()
    assert type(product_name) is str
    assert 0 < len(product_name) < 32
