class Solution(object):
    def myAtoi(self, str: str) -> int:
        str=str.lstrip()
        strlen = len(str)
        if strlen == 0:
            return 0

        start = 1
        if str[0] == '+' or str[0] == '-':
            start = 2
        result = 0
        while start <= strlen:
            try:
                result = int(str[:start])
                start += 1
            except:
                break


        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result