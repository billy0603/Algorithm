import sys

class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None
        
def findnode(head,num):
    ptr=head
    
    while ptr!=None:
        if ptr.num==num:
            return ptr
        ptr=ptr.next
    return ptr

def insertnode(head,ptr,num,salary,name):
    InsertNode=employee()
    if not InsertNode:
        return None
    InsertNode.num=num
    InsertNode.salary=salary
    InsertNode.name=name
    InsertNode.next=None
    if ptr==None: #插入第一個節點
        InsertNode.next=head
        return InsertNode
    else:
        if ptr.next==None: #插入最後一個節點
            ptr.next=InsertNode
        else: #插入中間節點
            InsertNode.next=ptr.next
            ptr.next=InsertNode
        return head

def del_ptr(head,ptr):  #刪除節點副程式
    top=head
    if ptr.num==head.num:  #[情形1]:刪除點在串列首
        head=head.next
        print('已刪除第 %d 號員工 姓名：%s 薪資:%d' %(ptr.num,ptr.name,ptr.salary))
    else:
        while top.next!=ptr:  #找到刪除點的前一個位置
            top=top.next
        if ptr.next==None:   #刪除在串列尾的節點
            top.next=None
            print('已刪除第 %d 號員工 姓名：%s 薪資:%d' %(ptr.num,ptr.name,ptr.salary))
        else:
            top.next=ptr.next #刪除在串列中的任一節點
            print('已刪除第 %d 號員工 姓名：%s 薪資:%d' %(ptr.num,ptr.name,ptr.salary))
    return head  #回傳串列


position=0
data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
      [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
      [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
namedata=['Allen','Scott','Marry','John','Mark','Ricky', \
          'Lisa','Jasica','Hanson','Amy','Bob','Jack']
print('員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')

print('-------------------------------------------------------')

for i in range(3):
    for j in range(4):
        print('[%4d] $%5d ' %(data[j*3+i][0],data[j*3+i][1]),end='')
    print()
    
print('------------------------------------------------------\n')

head=employee() #建立串列首
head.next=None

if not head:
    print('Error!! 記憶體配置失敗!!\n')
    sys.exit(1)
head.num=data[0][0]
head.name=namedata[0]
head.salary=data[0][1]
head.next=None

ptr=head

for i in range(1,len(data)): #建立串列
    newnode=employee()
    newnode.next=None
    newnode.num=data[i][0]
    newnode.name=namedata[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next
    
while(True):
    print('請輸入要插入其後的員工編號,如輸入的編號不在此串列中,') 
    position=int(input('新輸入的員工節點，將視為此串列的串列首,請輸入1\n要刪除的員工編號,請輸入2\n要離開程序請輸入-1\n你的選擇為==>'))
    if position ==-1:
        break
    elif position== 1:
        
        ptr=findnode(head,position)
        new_num=int(input('請輸入新插入的員工編號：'))
        new_salary=int(input('請輸入新插入的員工薪水：'))
        new_name=input('請輸入新插入的員工姓名: ')
        head=insertnode(head,ptr,new_num,new_salary,new_name)
    else:
        findword=int(input('請輸入要刪除的員工編號,要結束刪除過程,請輸入-1：'))
        ptr=head
        find=0
        while ptr!=None:
            if ptr.num==findword:
                ptr=del_ptr(head,ptr)
                find=find+1
                head=ptr
            ptr=ptr.next
        if find==0:
            print('######沒有找到######')        
    print()

ptr=head
print('\t員工編號    姓名\t薪水')         
print('\t==============================')
while ptr!=None:
    print('\t[%2d]\t[ %-7s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
    ptr=ptr.next
