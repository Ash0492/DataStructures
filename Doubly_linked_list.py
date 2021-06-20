#Create a node class
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next=next
        self.prev=prev
        self.data=data

#Class to create a doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None
#Adding node at the front of the list
    def push(self,new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev=None

        if self.head is not None:
            self.head.prev=new_node


        self.head = new_node

#Adding node after a given node
    def InsertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The node doesn't exist in DLL")
            return

        new_node = Node(data= new_data)

        prev_node.next = new_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev=new_node

#Adding node at the end of the doubly linked list
    def append(self, new_data):

        new_node = Node(data = new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while(last.next is not None):
            last = last.next

        last.next = new_node

        new_node.prev = last

        return

    #Adding a node before a given node
    def InsertBefore(head_ref,next_node,new_data):
        if (next_node == None):
            print("The given next node cannot be Null")
            return

        new_node= Node(data =new_data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if(new_node.next!=None):
            new_node.prev.next=new_node
        else:
            head_ref=new_node
        return head_ref

#Print the list
    def PrintList(self, node):
        last = None
        print("Traversal in forward direction")
        while(node != None):
            print(node.data, end=" ")
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while (last!=None):
            print(last.data, end=" ")
            last=last.prev

#Program to test above functions
llist= DoublyLinkedList()

llist.append(6)
llist.push(7)
llist.push(1)
llist.append(4)
llist.InsertAfter(llist.head.next, 8)
llist.InsertAfter(llist.head.next, 21)
llist.InsertBefore(llist.head.next, 69)
llist.InsertBefore(llist.head.next, 89)

print("Created DLL is: ", llist.PrintList(llist.head))
