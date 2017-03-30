class node:#creating a node
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

#node with 2 fields
#next for the adress of the nodes
class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        #new class being called so a new node will be created everytime
        #and the adress will be stored in a integer data type called
        #new_node

        new_node.data = data
        #putting data in data field of node
        new_node.next = self.cur_node
        # link the new node to the 'previous' node.
        self.cur_node = new_node
        # set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print (node.data)
            node = node.next
            #traverse of a link list 
            #in order to print all the data in field

ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.list_print()
