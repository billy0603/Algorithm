import random

def showdata(data):
    for i in range(len(data)):
        print('%3d' %data[i],end='')
    print()
    
def quick_sort(d,size,lf,rg):
    #第一筆鍵值為d[lf]
    if lf<rg: #排序資料的左右邊
        lf_index=lf+1
        while d[lf_index]<d[lf]:
            if lf_index+1>size:
                break
            lf_index+=1
        rg_index=rg
        
        while d[rg_index]>d[lf]:
            rg_index-=1
        while lf_index<rg_index:
            d[lf_index],d[rg_index]=d[rg_index],d[lf_index]
            lf_index+=1
            while d[lf_index]<d[lf]:
                lf_index+=1
            rg_index-=1
            while d[rg_index]>d[lf]:
                rg_index-=1
        
        d[lf],d[rg_index]=d[rg_index],d[lf]
        
        for i in range(size):
            print('%3d' %d[i],end='')
        print()
        
        quick_sort(d,size,lf,rg_index-1)  #以rg_index為基準分成左右二瓣以遞迴方式
        quick_sort(d,size,rg_index+1,rg)  #分別為左右二邊進行排序直到完成排序

def main():
    arr_len=int(input('設定 list 的長度:'))
    list=[random.randint(1,100) for i in range(arr_len)]
    print('初始資料:')
    showdata(list)
    print('排序過程如下:')
    quick_sort(list,len(list),0,len(list)-1)
    print('最終結果:')
    showdata(list)
    
main()
