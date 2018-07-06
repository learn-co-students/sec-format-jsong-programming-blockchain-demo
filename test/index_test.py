from unittest import TestCase
from ipynb.fs.full.index import *

class S256Test(TestCase):

        def test_sec(self):

            G = S256Point(
                0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
                0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)

            coefficient = 999**3
            uncompressed = '049d5ca49670cbe4c3bfa84c96a8c87df086c6ea6a24ba6b809c9de234496808d56fa15cc7f3d38cda98dee2419f415b7513dde1301f8643cd9245aea7f3f911f9'
            compressed = '039d5ca49670cbe4c3bfa84c96a8c87df086c6ea6a24ba6b809c9de234496808d5'
            point = coefficient*G
            self.assertEqual(point.sec(compressed=False), bytes.fromhex(uncompressed))
            self.assertEqual(point.sec(compressed=True), bytes.fromhex(compressed))
            coefficient = 123
            uncompressed = '04a598a8030da6d86c6bc7f2f5144ea549d28211ea58faa70ebf4c1e665c1fe9b5204b5d6f84822c307e4b4a7140737aec23fc63b65b35f86a10026dbd2d864e6b'
            compressed = '03a598a8030da6d86c6bc7f2f5144ea549d28211ea58faa70ebf4c1e665c1fe9b5'
            point = coefficient*G
            self.assertEqual(point.sec(compressed=False), bytes.fromhex(uncompressed))
            self.assertEqual(point.sec(compressed=True), bytes.fromhex(compressed))
            coefficient = 42424242
            uncompressed = '04aee2e7d843f7430097859e2bc603abcc3274ff8169c1a469fee0f20614066f8e21ec53f40efac47ac1c5211b2123527e0e9b57ede790c4da1e72c91fb7da54a3'
            compressed = '03aee2e7d843f7430097859e2bc603abcc3274ff8169c1a469fee0f20614066f8e'
            point = coefficient*G
            self.assertEqual(point.sec(compressed=False), bytes.fromhex(uncompressed))
            self.assertEqual(point.sec(compressed=True), bytes.fromhex(compressed))
