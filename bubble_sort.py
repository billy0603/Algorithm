import random

def showdata(data):
    for i in range(len(data)):
        print('%3d' %data[i],end='')
    print()


def bubble_sort(data):
    print('氣泡排序:原始資料為:')
    showdata(data)
    print('-----------------------------------------')
    for x in range(len(data)-1,-1,-1): #須執行排序次數:(n-1)次
        for y in range(x):
            if data[y]>data[y+1]: #判斷第一個與第二個大小
                data[y],data[y+1] = data[y+1],data[y]  #如果第一個大於第二個，則交換
                
        print('第%d次排序後的結果是:' %(len(data)-x),end='')
        
        for j in range(len(data)):
            print('%3d' %data[j],end='')
        print()
    print('-----------------------------------------')
    print('排序後結果為:')
    showdata(data)     

#設定arr長度
arr_len=int(input('設定 list 的長度:'))

data=[random.randint(1,100) for i in range(arr_len)]  #需先排序

bubble_sort(data)