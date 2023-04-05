# -*- coding: utf-8 -*-
from __future__ import unicode_literals

print("Voici ou commence PolyKoz")


import qrcode

img = qrcode.make('BINATE')

img.save("QrCode.jpg")