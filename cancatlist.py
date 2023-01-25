import sys

import random

class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None

def concatlist(ptr1,ptr2):
    ptr=ptr1
    while ptr.next!=None:
        ptr=ptr.next
    ptr.next=ptr2
    return ptr1

data=[[None]*2 for row in range(12)]

namedata1=['Allen','Scott','Marry','Jon', \
            'Mark','Ricky','Lisa','Jasica', \
            'Hanson','Amy','Bob','Jack']

namedata2=['May','John','Michael','Andy', \
            'Tom','Jane','Yoko','Axel', \
            'Alex','Judy','Kelly','Lucy']

for i in range(12):
    data[i][0]=i+1 #編號
    data[i][1]=random.randint(60,100) #分數

head1=employee()   #建立第一組串列首
if not head1:
    print('Error!! 記憶體配置失敗!!')
    sys.exit(0)
	
head1.num=data[0][0]
head1.name=namedata1[0]
head1.salary=data[0][1]
head1.next=None
ptr=head1

for i in range(1,12):  #建立第一組鏈結串列
    newnode=employee()
    newnode.num=data[i][0] #編號
    newnode.name=namedata1[i] #人名
    newnode.salary=data[i][1] #分數
    newnode.next=None #無下一個鏈結
    ptr.next=newnode #將剛剛的ptr與newnode連結
    ptr=ptr.next 
    
for i in range(12):
    data[i][0]=i+1 #編號
    data[i][1]=random.randint(60,100) #分數

head2=employee()   #建立第二組串列首
if not head2:
    print('Error!! 記憶體配置失敗!!')
    sys.exit(0)  
	
head2.num=data[0][0]
head2.name=namedata2[0]
head2.salary=data[0][1]
head2.next=None
ptr=head2
for i in range(1,12):  #建立第二組鏈結串列
    newnode=employee()
    newnode.num=data[i][0]
    newnode.name=namedata2[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next

i=0
ptr=concatlist(head1,head2) #將串列相連

print('兩個鏈結串列相連的結果：')
while ptr!=None: #列印串列資料
    print('[%2d %6s %3d] => ' %(ptr.num,ptr.name,ptr.salary),end='')
    i=i+1
    if i>=3:
        print()
        i=0
    ptr=ptr.next