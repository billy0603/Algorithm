list1=[20,45,88,9999]
list2=[98,10,23,15,9999]
list3=[]

def merge_sort():
    global list1
    global list2
    global list3
    
    #先用select sort將兩數列排序，在做合併
    select_sort(list1)
    select_sort(list2)

    print('\n第1組資料排序結果: ',end='')
    for i in range(len(list1)-1):
        print(list1[i],' ',end='')
        
    print('\n第2組資料排序結果: ',end='')
    for i in range(len(list2)-1):
        print(list2[i],' ',end='')
    
    print()
    
    for i in range(30):
        print('=',end='')
    print()
    
    My_Merge(len(list1)-1,len(list2)-1)
    
    for i in range(30):
        print('=',end='')
    print()
    
    print('\n合併排序法的最終結果: ',end='')
    for i in range(len(list3)-1):
        print('%d' %list3[i],' ',end='')


def select_sort(data):
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
        

def My_Merge(x,y):
    global list1
    global list2
    global list3
    
    index1=0
    index2=0
    
    for index3 in range(len(list1)+len(list2)-2):
        if list1[index1]<list2[index2]:#比較二個數列，資料小的先存放
            list3.append(list1[index1])
            index1+=1
            print('此數字%d取自第1組資料 ' %list3[index3])
        else:
            list3.append(list2[index2])
            index2+=1
            print('此數字%d取自第1組資料 ' %list3[index3])   
        print('目前的合併排序結果: ',end='')
        for i in range(index3+1):
            print(list3[i],' ',end='')
        print('\n')
merge_sort()         