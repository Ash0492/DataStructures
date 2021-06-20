#def IsAnagram(a,b):
   # a= sorted(a)
    #b = sorted(b)

    #if len(a)!=len(b):
        #return "No"

    #if a==b:
        #return "YES"
    #else:
        #return "NO"


#a = "b"
#b= "d"
#print(IsAnagram(a,b))


class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # code here
        a = sorted(a)
        b = sorted(b)

        if len(a) != len(b):
            return "No"

        if a == b:
            return "YES"
        else:
            return "NO"


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        if (Solution().isAnagram(a, b)):
            print("YES")
        else:
            print("NO")
        # } Driver Code Ends

