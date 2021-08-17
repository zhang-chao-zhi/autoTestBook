import unittest

from unittest import mock


def do_login_directly():
    url = "http://127.0.0.1:5000/doLogin"
    data = {"account": "freePHP", "password": "2323243"}
    return ''


class LoginTest(unittest.TestCase):

    @mock.patch('test_login.do_login_directly')
    def test_do_login(self, mock_opt):
        json_data = [
            {'token': "dsdfsdcsdfsdfaadsfa", 'user_id': 101}
        ];

        json_result = {'data': json_data, 'result': True, 'errorMsg': ''}
        mock_opt.return_value = json_result
        self.assertEqual(do_login_directly(), json_result)


if __name__ == '__main__':
    unittest.main()
