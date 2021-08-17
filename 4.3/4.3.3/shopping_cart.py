# -*- coding: utf-8 -*-
'''
购物车

@author freePHP
@version 1.0.0


包含 CURD（增删改查）商品方法，下单，支付订单，退款等功能。
'''


class ShoppingCart(object):
    __products = {}
    __pay_state = ''

    # 根据商品名看是否存在于购物车
    def has_product(self, product_name: str) -> bool:
        if product_name in self.__products:
            return True
        else:
            return False

    # 增加商品到购物车,包括商品名和数量
    def addProduct(self, product_name: str, num: int) -> str:
        if self.has_product(product_name):
            self.__products[product_name] += num
            return "add successfully"
        else:
            self.__products[product_name] = num
            return "add successfully, and init it"

    # 修改商品，主要修改数量
    def editProduct(self, product_name: str, num: int) -> str:
        if self.has_product(product_name):
            self.__products[product_name] += num
            return "update successfully"
        else:
            return "not have this kind of product!"

    # 删除商品
    def deleteProduct(self, product_name: str) -> str:
        if self.has_product(product_name):
            self.__products.pop(product_name)
            return "delete successfully"
        else:
            return "The product dosen't exist, so it can not be deleted."

    # 创建订单
    def createOrder(self) -> str:
        self.__pay_state = "waitingForPay"
        return self.__pay_state
        # other codes

    # 支付订单，改变订单状态为已支付
    def payOrder(self) -> str:
        self.__pay_state = "payed"
        return self.__pay_state
        # other codes

    # 退款
    def refund(self) -> str:
        self.__pay_state = "refund"
        return self.__pay_state
        # other codes

