# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "madam"
ans = isPalindrome(s)
 
if (ans):
    print("True")
else:
    print("False")