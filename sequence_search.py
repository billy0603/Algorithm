import random

#設定arr長度
while True:
    arr_len=int(input('設定array的長度<10倍數>:'))
    if ( arr_len % 10 )!=0:
        print('%d非10倍數，請重新輸入，' %arr_len,end='')
    else:
        break
data=[random.randint(1,100) for i in range(arr_len)]

val=-1
while val != 0:  #進入抽獎快樂區
    find=0
    val=int(input('請輸入搜尋見值(1~100)，輸入0則離開'))
    for i in range(arr_len):
        if data[i]==val:
            print('在第 %3d個位置找到鍵值 [%3d]' %(i+1,data[i]))
            find+=1
    if find==0 and val != 0:
        print('####  沒有找到數字 %3d ####' %val)
        
print('資料內容:')
for i in range(10):
    for j in range(arr_len//10):
        print('%2d[%3d]  ' %(i*(arr_len//10)+j+1,data[i*(arr_len//10)+j]),end='')
    print('')