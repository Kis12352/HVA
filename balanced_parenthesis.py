def checkBalance(str1):
    count= 0
    ans=False
    for i in str1:
        if i == "(" or i == "{" or i == "[":
            count += 1
        elif i == ")" or i == "}" or i == "]":
            count-= 1
        if count < 0:
            return ans
    if count==0:
        return not ans
    return ans
str1=input("Enter a string of brackets: ")
print("Given string is balanced :",checkBalance(str1))







