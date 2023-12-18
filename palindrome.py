def isPalindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[-1]:
        return isPalindrome(str[1:-1])
    else:
        return False


print(isPalindrome("awesome"))  # false
print(isPalindrome("foobar"))  # false
print(isPalindrome("tacocat"))  # true
print(isPalindrome("amanaplanacanalpanama"))  # true
print(isPalindrome("amanaplanacanalpandemonium"))  # false
