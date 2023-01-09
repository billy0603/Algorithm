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
    print('-----------------------------------------')
    print('排序後結果為:')
    showdata(data)     


data=[16,25,39,27,12,8,45,63]
insert_sort(data)