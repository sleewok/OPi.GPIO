# -*- coding: utf-8 -*-
# Copyright (c) 2022 sillo01
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 3b
https://pinout.ai/orange-pi-3b
http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_3B
Usage:
.. code:: python
   import orangepi.3b
   from OPi import GPIO
   GPIO.setmode(orangepi.3b.BOARD)

 +------+-----+----------+--------+---+   PI3B   +---+--------+----------+-----+------+
 | GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
 +------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
 |      |     |     3.3V |        |   |  1 || 2  |   |        | 5V       |     |      |
 |  140 |   0 |    SDA.2 |     IN | 1 |  3 || 4  |   |        | 5V       |     |      |
 |  141 |   1 |    SCL.2 |     IN | 1 |  5 || 6  |   |        | GND      |     |      |
 |  147 |   2 |    PWM15 |     IN | 0 |  7 || 8  | 1 | ALT1   | RXD.2    | 3   | 25   |
 |      |     |      GND |        |   |  9 || 10 | 1 | ALT1   | TXD.2    | 4   | 24   |
 |  118 |   5 | GPIO3_C6 |     IN | 0 | 11 || 12 | 0 | IN     | GPIO3_C7 | 6   | 119  |
 |  128 |   7 | GPIO4_A0 |     IN | 0 | 13 || 14 |   |        | GND      |     |      |
 |  130 |   8 |    TXD.7 |     IN | 0 | 15 || 16 | 0 | IN     | RXD.7    | 9   | 131  |
 |      |     |     3.3V |        |   | 17 || 18 | 0 | IN     | GPIO4_A1 | 10  | 129  |
 |  138 |  11 | SPI3_TXD |     IN | 0 | 19 || 20 |   |        | GND      |     |      |
 |  136 |  12 | SPI3_RXD |     IN | 0 | 21 || 22 | 0 | IN     | TXD.9    | 13  | 132  |
 |  139 |  14 | SPI3_CLK |     IN | 0 | 23 || 24 | 0 | IN     | SPI3_CS1 | 15  | 134  |
 |      |     |      GND |        |   | 25 || 26 | 0 | IN     | GPIO4_A7 | 16  | 135  |
 |   32 |  17 |    SDA.3 |   ALT1 | 1 | 27 || 28 | 1 | ALT1   | SCL.3    | 18  | 33   |
 |  133 |  19 |    RXD.9 |     IN | 0 | 29 || 30 |   |        | GND      |     |      |
 |  124 |  20 | GPIO3_D4 |     IN | 0 | 31 || 32 | 0 | IN     | PWM11    | 21  | 144  |
 |  127 |  22 | GPIO3_D7 |     IN | 0 | 33 || 34 |   |        | GND      |     |      |
 |  120 |  23 | GPIO3_D0 |     IN | 0 | 35 || 36 | 0 | IN     | GPIO3_D5 | 24  | 125  |
 |  123 |  25 | GPIO3_D3 |     IN | 0 | 37 || 38 | 0 | IN     | GPIO3_D2 | 26  | 122  |
 |      |     |      GND |        |   | 39 || 40 | 0 | IN     | GPIO3_D1 | 27  | 121  |
 +------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
 | GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
 +------+-----+----------+--------+---+   PI3B   +---+--------+----------+-----+------+
"""

# Orange Pi 3b physical board pin to GPIO pin
# PH1(10) & PH2(11) for debug console default
BOARD = {
    3: 140,  # PD26 / TWI0-SDA / I2C2_SDA_M1
    5: 141,  # PD25 / TWI0-SCK / I2C2_SCL_M1
    7: 147,  # PD22 / PWM0 / PWM15_IR_M1
    8: 25,  # PL02 / 	S-UART-TX	 / UART2_TX_M0
    10: 24,  # PL03 / S-UART-RX	 / UART2_RX_M0
    11: 118,  # PD24 / UART3-RX	/ I2S1_MCLK_M1
    12: 119,  # PD18 / I2S1_SCLK_M1
    13: 128,  # PD23 / UART3-TX
    15: 130,  # PL10 / UART7_TX_M2
    16: 131,  # PD15 / UART7_RX_M2
    18: 129,  # PD16
    19: 138,  # PH05 / SPI1_MOSI / SPI3_MOSI_M0 / I2C4_SDA_M0
    21: 136,  # PH06 / SPI1_MISO / SPI3_MISO_M0
    22: 132,  # PD21 / UART9_TX_M2
    23: 139,  # PH04 / SPI1_CLK / SPI3_CLK_M0 / I2C4_SCL_M0
    24: 134,  # PH03 / SPI1_CS / SPI3_CS0_M0
    26: 135,  # PL08 / SPI3_CS1_M0
    27: 32,  # PI10 / TWI2_SDA / UART3_RX / UART3_RX_M0 / I2C3_SDA_M0
    28: 33,  # PI9 / TWI2_SCL / UART3_TX / UART3_TX_M0 / I2C3_SCL_M0
    29: 133,  # PI0 / UART9_RX_M2
    31: 124,  # PI15
    32: 144,  # PI11 / PWM1 / PWM11_IR_M1
    33: 127,  # PI12 / PWM2
    35: 120,  # PI2
    36: 125,  # PC12
    37: 123,  # PI16
    38: 122,  # PI4
    40: 121,  # PI3
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD
