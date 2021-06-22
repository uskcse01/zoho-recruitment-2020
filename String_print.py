print("Enter the input: ")
str_ = input()
i = 0
j = len(str_)//2
print("Output: ")
while i<=len(str_)//2:
    if j<len(str_):
        result  = str_[len(str_)//2:j]
        print(' '*(len(str_)-len(result))+result)
        # print()
        j+=1
    else:
        result = str_[len(str_)//2:j]+str_[0:i]
        print(' '*(len(str_)-len(result))+result)
        # print(result)
        i+=1
