# Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

# Cases for atoi() conversion:

# Skip any leading whitespaces.
# Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
# Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
# If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.
# Examples:

# Input: s = "-123"
# Output: -123
# Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer
def atoi(s):
    INT_MAX=2**31-1
    INT_MIN=-2**31
    i=0
    sign=1
    result=0
    if s[i]==" " and i<len(s):
        i+=1
    if i<len(s) and s[i]=="+" or s[i]=="-":
        sign=-1 if s[i]=="-" else 1
        i+=1
    while i<len(s) and '0'<=s[i]<='9':
        digit=ord(s[i])-ord('0')
        if result>INT_MAX-digit//10:
            return INT_MAX if sign==1 else INT_MIN
        result=result*10+digit
        i+=1
    return sign*result
if __name__=="__main__":
    s=input().strip()
    print(atoi(s))