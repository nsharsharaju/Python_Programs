def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans ='';
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans+c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

user_input = input("Enter a string: ")

if isPalindrome(user_input):
    print("The string you entered is a palindrome")
else:
    print("The string you entered is not a palindrome")