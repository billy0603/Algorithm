import random

#設定arr長度
while True:
    arr_len=int(input('設定array的長度<10倍數>:'))
    if ( arr_len % 10 )!=0:
        print('%d非10倍數，請重新輸入，' %arr_len,end='')
    else:
        break

data=sorted([random.randint(1,100) for i in range(arr_len)])  #需先排序


def bin_search(data,val):
    low=0
    high=len(data)-1
    
    while low <= high and val!=-1:
        #內插法公式
        mid=low+int((val-data[low])*(high-low)/(data[high]-data[low]))
        if val<data[mid]:
            print('%d 介於位置 %d[%3d]及中間值 %d[%3d]，找左半邊' \
                %(val,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif val>data[mid]:
            print('%d 介於中間值位置 %d[%3d] 及 %d[%3d]，找右半邊' \
                %(val,mid+1,data[mid],high+1,data[high]))
            low=mid+1
        else:
            return mid
    return -1
            
while True:
    num=0
    val=int(input('請輸入搜尋鍵值(1-%3d)，輸入0結束：' %max(data)))
    if val ==0:
        break
    num=bin_search(data,val)
    if num==-1:
        print('##### 沒有找到[%3d] #####' %val)
    else:
        print('在第 %2d個位置找到 [%3d]' %(num+1,data[num]))

print('資料內容:')
for i in range(10):
    for j in range(arr_len//10):
        print('%2d[%3d]  ' %(i*(arr_len//10)+j+1,data[i*(arr_len//10)+j]),end='')
    print('')