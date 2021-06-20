class Node :
    def __init__(self, data) :
        self.data=data
        self.next=None


class LinkedList :
    def __init__(self) :
        self.head=None

    # LinkedList Traversal
    def printlist(self) :
        temp=self.head
        while (temp) :
            print(temp.data)
            temp=temp.next

    # Add the node at the beginning of the linkedlist
    def push(self, data) :
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    # Deleting a node in between the linkedlist
    def DeleteNode(self, key) :
        temp=self.head

        if (temp is not None) :
            if (temp.data==key) :
                self.head=temp.next
                temp=None
                return

        while (temp is not None) :
            if temp.data==key :
                break
            prev=temp
            temp=temp.next

        if (temp==None) :
            return

        prev.next=temp.next

        temp=None

    # Deleting a node at a given position
    def DeleteNodePos(self, pos) :

        if self.head is None :
            return
        temp=self.head

        if pos==0 :
            self.head=temp.next
            temp=None
            return

        for i in range(pos-1) :
            temp=temp.next
            if temp is None :
                break

        if temp is None :
            return

        if temp.next is None :
            return

        next=temp.next.next
        temp.next=None
        temp.next=next

    # Delete a linkedlist
    def DeleteList(self) :

        current=self.head
        while current :
            prev=current.next
            del current.data
            current=prev

    # Count the total number of nodes in the linked list
    def CountNode(self) :
        temp=self.head
        count=0
        while (temp) :
            count+=1
            temp=temp.next
        return count

        # Insert a node in between the linked list

    def insertAfter(self, prev_node, data) :
        if prev_node is None :
            print("Please insert the nodes")
            return

        new_node=Node(data)

        new_node.next=prev_node.next
        prev_node.next=new_node

# search an element in the linkedlist
    def search(self, x) :
        temp=self.head
        while temp!= None :
            if temp.data==x :
                return True

            temp=temp.next
        return False

    # Add node at the end of the linked list
    def append(self, data) :
        new_node=Node(data)
        if self.head is None :
            self.head=new_node
            return
        last=self.head
        while (last.next) :
            last=last.next

        last.next=new_node


if __name__=='__main__' :
    Llist=LinkedList()
    Llist.push(7)
    Llist.push(1)
    Llist.push(3)
    Llist.push(2)
    Llist.push(8)

    if Llist.search(2) :
        print("Yes")
    else :
        print("No")

    print("Created Linked List: ")
    Llist.printlist()
    Llist.DeleteNodePos(4)
    print("print list after deletion of node at position 4")
    print("Created linkedlist is: ")
    Llist.printlist()
    print("Total number of nodes are:", Llist.CountNode())
    print("Deleting the linkedlist")
    Llist.DeleteList()
    print("Linked list deleted")
