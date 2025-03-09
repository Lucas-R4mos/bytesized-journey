import unittest
from utils.encrypt import encrypt
from tests.dotdict import DotDict

MOCK_APP = DotDict(
    config={
        "PASSWORD_SALT": "MOCKED_SALT"
    }
)


class TestEncrypt(unittest.TestCase):
    def test_encrypt(self):
        hashed = encrypt("password", MOCK_APP)
        self.assertEqual(
            hashed[31:],
            "TU9DS0VEX1NBTFQ$4NNVS8dXJ51FZ6Vh89xBZkXzz8eNCdz8f1jd6bMPm3Q"  # noqa
        )
