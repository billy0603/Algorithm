import random

def showdata(data):
    for i in range(len(data)):
        print('%3d' %data[i],end='')
    print()

def select_sort(data):
    print('選擇排序:原始資料為:')
    showdata(data)
    print('-----------------------------------------')
    for x in range(len(data)):
        smallest=data[x]
        index=x
        for y in range(x+1,len(data)): #由x+1開始比較
            if smallest>data[y]: #找出最小元素
                smallest=data[y]
                index=y
        tmp=data[x]
        data[x]=data[index]
        data[index]=tmp
        print("第%d次排序結果:" %(x+1),end='')
        showdata(data)
        
        
    print('-----------------------------------------')
    print('排序後結果為:')
    showdata(data)     
    
#設定arr長度
arr_len=int(input('設定 list 的長度:'))

data=[random.randint(1,100) for i in range(arr_len)]

select_sort(data)