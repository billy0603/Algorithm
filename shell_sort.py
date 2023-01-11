def showdata(data):
    for i in range(len(data)):
        print('%3d' %data[i],end='')
    print()

def shell_sort(data):
    k=1
    jmp=len(data)//2

    while jmp!=0:
        for i in range(jmp,len(data)): #i為掃描次數jmp為設定間距位移量
            tmp=data[i] #tmp暫存資料
            j=i-jmp #以j來定位比較的元素
            while tmp < data[j] and j>=0: #排序插入法
                data[j+jmp]=data[j]
                j=j-jmp
            data[jmp+j]=tmp
        print('第%d次排序過程:' %k,end='')
        k+=1
        showdata(data)
        print('-------------------------------')
        jmp=jmp//2

def main():
    data=[16,25,39,27,12,8,45,63]
    print('原始陣列:')
    showdata(data)
    print('-------------------------------')
    shell_sort(data)

main()
        