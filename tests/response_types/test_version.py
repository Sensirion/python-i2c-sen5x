# -*- coding: utf-8 -*-
# (c) Copyright 2022 Sensirion AG, Switzerland

from sensirion_i2c_sen5x.response_types import Sen5xVersion, \
    Sen5xFirmwareVersion, Sen5xHardwareVersion, Sen5xProtocolVersion


def test_to_str():
    obj = Sen5xVersion(
        Sen5xFirmwareVersion(1, 2, False),
        Sen5xHardwareVersion(3, 4),
        Sen5xProtocolVersion(5, 6),
    )
    assert str(obj.firmware) == "1.2"
    assert str(obj.hardware) == "3.4"
    assert str(obj.protocol) == "5.6"
    assert str(obj) == "Firmware 1.2, Hardware 3.4, Protocol 5.6"
