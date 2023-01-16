import random

def showdata(data):
    for i in range(len(data)):
        print('%3d' %data[i],end=' ')
    print()

def radix(data,size):
    n=1 #n為基數，由個位數開始排序
    while n<=100:
        tmp=[[0]*100 for row in range(10)] #設定暫存陣列，[0~9位數]
        
        for i in range(size): #比對所有資料
            m=(data[i]//n)%10 # m為n位數的值，如36取十位數(36/10)%10=3
            tmp[m][i]=data[i]
        k=0
            
        for i in range(10):
            for j in range(size):
                if tmp[i][j] !=0: # 因一開始設定tmp=[0],故不為0者即為data暫存在tmp裡的值，把tmp裡的放回data[]
                    data[k]=tmp[i][j]
                    k+=1
        print('經過%3d位數排序後  :' %n,end='')
        showdata(data)
        n=10*n

def main():
    #設定arr長度
    arr_len=int(input('設定 list 的長度:'))
    list=[random.randint(0,999) for i in range(arr_len)]
    print('-----------------------------------------')
    print('初始資料:')
    showdata(list)
    print('-----------------------------------------')
    radix(list,arr_len)
    print('-----------------------------------------')
    print('最終結果:')
    showdata(list)
main()
    