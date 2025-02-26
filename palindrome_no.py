def getdata():
  a=int(input("Enter the number to check palindrome : "))
  return a
def checkpalindrome():
  a=str(getdata())
  if a[::]==a[::-1]:
    return "Entered number is palindrome . "
  else:
    return "not palindrome"
print(checkpalindrome())