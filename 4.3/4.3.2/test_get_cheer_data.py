import unittest
from unittest import mock
from get_cheer_data import create_cheers

class GetCheerDataTest(unittest.TestCase):
    @mock.patch('get_cheer_data.load_cheers')
    def test_get_cheer_data(self, mock_load):
        mock_load.return_value = "Ha Ha,CDC" # patch模拟了load_cheers函数对象，并将返回值设置了，这样就不用真正调用该函数了
        self.assertEqual(create_cheers(), "Ha Ha,CDC")


if __name__ == '__main__':
    unittest.main()
