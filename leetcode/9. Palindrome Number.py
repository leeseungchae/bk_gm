"""
                Given an integer x, return true if x is a
                palindrome
                , and false otherwise.



                Example 1:

                Input: x = 121
                Output: true
                Explanation: 121 reads as 121 from left to right and from right to left.

"""


def isPalindrome(self, x: int) -> bool:
    x_str = str(x)
    x_list = list(x_str)
    x_list.reverse()
    x_rev = ''.join(x_list)
    count = len(x_list)
    for i in range(0, count):
        if x_rev != x_str:
            print('false')
            break
        else:
            if i == count - 1:
                return 'true'