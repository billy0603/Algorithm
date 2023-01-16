import random
def showdata(data):
    for i in range(len(data)):
        print('%3d' %data[i],end='')
    print()


def insert_sort(data):
    print('選擇排序:原始資料為:')
    showdata(data)
    print('-----------------------------------------')
    for x in range(1,len(data)):
        tmp=data[x] #tmp站存資料
        no=x-1
        while no>=0 and tmp<data[no]: #當數字大於tmp則換位
            data[no+1]=data[no] # 
            no-=1
        data[no+1]=tmp #最小元素放到第一位
        print('第%d次排序後的結果是:' %x,end='')
        showdata(data)   
    print('-----------------------------------------')
    print('排序後結果為:')
    showdata(data)     


#設定arr長度
arr_len=int(input('設定 list 的長度:'))

data=[random.randint(1,100) for i in range(arr_len)]  #需先排序
insert_sort(data)