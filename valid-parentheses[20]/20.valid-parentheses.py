#
# [20] Valid Parentheses
#

class Solution(object):
    def isValid(self, s):

        open = []
        switch = {")": "(", "]": "[", "}": "{"}

        for char in s:

            if char in switch:
                if open and open[-1] == switch[char]:
                    open.pop()
                else:
                    return False
            else:
                open.append(char)

        return len(open) == 0
