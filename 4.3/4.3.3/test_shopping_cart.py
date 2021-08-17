import unittest
from unittest import mock
from shopping_cart import ShoppingCart
'''
购物车测试类

@author freePHP
@version 1.0.0
'''
class ShoppingCartTest(unittest.TestCase):

    @mock.patch('shopping_cart.ShoppingCart.addProduct')
    def test_add_product(self, mock_opt):
        mock_opt.return_value = "add successfully"

        self.assertEqual(ShoppingCart.addProduct("earring"), "add successfully")

    @mock.patch('shopping_cart.ShoppingCart.editProduct')
    def test_edit_product(self, mock_opt):
        # 先添加，再修改数量
        shopping_cart = ShoppingCart.addProduct('plush_bear', 2)
        mock_opt.return_value = "edit successfully"

        self.assertEqual(ShoppingCart.editProduct('plush_bear', 3))

    @mock.patch('shopping_cart.ShoppingCart.deleteProduct')
    def test_delete_product(self, mock_opt):
        mock_opt.return_value = "delete successfully"

        self.assertEqual(ShoppingCart.deleteProduct("funny"), "delete successfully")

    @mock.patch('shopping_cart.ShoppingCart.payOrder')
    def test_pay_order(self, mock_opt):
        mock_opt.return_value = "payed"

        self.assertEqual(ShoppingCart.payOrder(), "payed")

    @mock.patch('shopping_cart.ShoppingCart.refund')
    def test_refund(self, mock_opt):
        mock_opt.return_value = "refund"

        self.assertEqual(ShoppingCart.refund(), "refund")

if __name__ == '__main__':
    unittest.main()
