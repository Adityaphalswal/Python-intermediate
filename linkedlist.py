class Node:
    def _init_(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def _init_(self):
        self.head = None

    def insert_at_starting(self, data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
    
        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) +"-->"
            itr=itr.next

        print(llstr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next =Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,index):
        if index<0 or index>=self.length():
            raise Exception("invalid index")

        if index==0:
            self.head =self.head.next
            return
        
        count= 0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next  = itr.next.next
                break
            itr =itr.next
            count +=1


if __name__=="__main__":
    ll=LinkedList()
    '''ll.insert_at_starting(10)
    ll.insert_at_starting(30)
    ll.insert_at_end(79)
    ll.insert_at_end(44)
    ll.insert_values(["banana","mango","grapes","orange"])
    print("length:",ll.length())
    ll.remove_at(2)'''
    ll.insert_at(0,"figs")
    ll.print()