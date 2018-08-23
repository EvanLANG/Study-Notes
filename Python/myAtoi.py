def myAtoi(s):
    s=s.lstrip()
    if s[0].isalpha():
        print(0)
        return 0
    else:
        #print(1)
        neg=False
        num=0
        step=0
        for c in s:
            if c =="-":
                neg=True
            elif c.isdigit():
                step+=1
            else:
                break
        if neg:
            num=0-int(s[1:step+1])
        else:
            num=int(s[0:step])
        if num < -2**31:
            print(-2**31)
            return -2**31
        elif num > 2**31-1:
            print(2**31-1)
            return 2**31-1
        else:
            print(num)
            return num

if __name__=="__main__":
    myAtoi("24")
    myAtoi("  23")
    myAtoi("-24")
    myAtoi("word and 24")
    myAtoi("-91283472332")
