#lata tem 2l e gasta 3l por metro

import unittest


def latas(a, b):
    rlatas = ((a * b) / 3)/2
    if rlatas - int(rlatas) > 0 :
        rlatas = int(rlatas+1)
    else:
        rlatas = int(rlatas)
    return rlatas


class PinturaTestCase(unittest.TestCase):
    def test_latas(self):
        self.assertEqual(24, latas(11,13))

if __name__ == "__main__":
unittest.main()
