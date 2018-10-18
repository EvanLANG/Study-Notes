
###################################################################################################################

from math import log2
## Question No. 0:
def add(a, b): # do not change the heading of the function
    return a + b




###################################################################################################################
## Question No. 1:

def gallop_to(a, val):# do not change the heading of the function
    interval = 2
    index = 1
    pos = a.cur
    mid = 0
    if a.peek(pos) == val:
        return
    if a.peek(pos+index) == val:
        a.cur = pos + index
    else:
        a.next()
        pos = a.cur
        while True:
            if a.peek(pos) == val:
                a.cur = pos
                break
            if a.peek(pos+interval) == None:
                break
            #print(a.cur)
            if a.peek(pos+interval) == val:
                a.cur = pos + interval
                break
            elif a.peek(pos+interval) > val:
                mid = BinarySearch(pos, pos+interval, val, a)
                if mid == -1:
                    break
                else:
                    if a.data[mid] ==val:
                        a.cur = mid
                        break
                    else:
                        break
            elif a.peek(pos+interval) < val and not a.eol():
                pos = pos + interval
                interval = 2 * interval
                if (pos+interval) >= len(a.data)-1:
                    interval = len(a.data) - pos - 1
    return
     
def BinarySearch(low, height, t, array):
    #print(low, height, t, array.get_list())
    while low <= height:
        mid = int((low+height)/2)
        if array.data[mid] < t:
            low = mid + 1

        elif array.data[mid] > t:
            height = mid - 1

        elif array.data[mid] == t:
            return mid
        
    return -1  
        

###################################################################################################################
## Question No. 2:

def Logarithmic_merge(index, cut_off, buffer_size): # do not change the heading of the function
    c = cut_off
    b = buffer_size
    indt = index[0:c]
    n = 0
    while 2**n*b <= c:
        n+=1
    r = []
    for p in range(0,n):
        r.append([])
    z = []
    for _ in range(0,n):
        z.append([])
    for i in indt:
        z[0].append(i)
        if len(z[0]) == b:
            for j in range(0,100):
                if len(r[j]) == 2**j*b:
                    z[j+1] = sorted(r[j]) + sorted(z[j])
                    r[j] = []
                    z[j] = []
                else:
                    r[j] = sorted(z[j])
                    z[j] = []
                    break
    r.insert(0,z[0])
    return r


###################################################################################################################
## Question No. 3:
def unary(inputs):
    Num = len(inputs)-1
    return 2**Num

def binary(inputs):
    tem = 0
    for i in range(0,len(inputs)):
        if inputs[i] == '1':
            tem += 2**(len(inputs)-1-i)
    return tem

def decode_gamma(inputs):# do not change the heading of the function
    tem = []
    data = inputs
    count = 0
    while len(data)!=0:
        count +=1
        if data[0] == '0':
            break
        if data[0] != '0':
            step = 0 
            for i in data:
                if i == '1':
                    step+=1
                elif i == '0':
                    break
            count = 0
            num = unary(data[0:step+1])+binary(data[step+1:2*step+1])
            tem.append(num)
            data = data[2*step+1:]
    return tem

            
    

def decode_delta(inputs):# do not change the heading of the function
    tem = []
    data = inputs
    count = 0
    while len(data) != 0:
        count += 1
        #print(data)
        if data[0] == '0':
            return tem
        elif data[0] != '0':
            step = 0
            for i in data:
                if i == '1':
                    step +=1
                elif i == '0':
                    break
            #print(count)
            count = 0
            num = unary(data[0:step+1])+binary(data[step+1:2*step+1]) - 1
            num1 = binary(data[2*step+1:2*step+1+num])
            num2 = 2**num + num1
            tem.append(num2)
            data = data[2*step+1+num:]
        #print(count)
    return tem      
            
   
            

def decode_rice(inputs, b):# do not change the heading of the function
    tem = []
    step = log2(b)
    tem_step = step
    cur = 0
    count = 0
    length = len(inputs)
    start_flag = True
    flag1 = True
    while cur <= length:
        if start_flag and inputs[cur] == "1":
            
            count += 1
            data = ""
            #print(count)
        elif count > 0 and flag1:
            start_flag = False
            flag2 = True
            flag1 = False
        elif tem_step > 0 and flag2:
            data = data + inputs[cur]
            tem_step -= 1
            #print(data)
            if tem_step == 0:
                data1 = int(data, 2)
                num = count * b + data1
                tem.append(num)
                start_flag = True
                flag1 = True
                count = 0
                tem_step = step
                #print('cur', cur)
        cur += 1
        if cur >= length:
            break
    return tem