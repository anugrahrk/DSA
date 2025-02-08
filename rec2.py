def temp_name(k):
    if k>0:
        result=k + temp_name(k-1)
        print(result)
    else:
        result=0
    return result
print("Recursion examples are:")
temp_name(6)