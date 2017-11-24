#!/bin/python
import sys
class Solution(object):
    def toHex(self, num):
        """
        transfor a int(positive or negtive) to hex
        :param num: 
        :return: string
        """
        asiii = 65
        if num == 0:
            return 0
        if num < 0:
            num = abs(num)
            num = ~num + 1
        n = num
        hexstr = ''
        while n > 0:
            m = n & 15
            if m < 10:
                hexstr = str(m) + hexstr
            else:
                hexstr = (chr(m-10+asiii)) + hexstr
            n = n >> 4
        print hexstr
if __name__ == "__main__":
    sol = Solution()
    num = int(sys.argv[1])
    sol.toHex(num)
