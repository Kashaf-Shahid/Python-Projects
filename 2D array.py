class Node:
    def __init__(self, data=None):
        self.data = data  
        self.right = None  
        self.down = None   


class LinkedList2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.front_array_head = None
        self.back_array_head = None
        self.create_2d_front_array()
        self.create_2d_back_array()

    def create_2d_front_array(self):
        if self.rows <=  0 or self.cols <= 0:
            return
        
        self.front_array_head = Node(0)  
        current_row = self.front_array_head
        
        for i in range(self.rows):
            current = current_row
            for j in range(1, self.cols):
                new_node = Node(i * self.cols + j)  
                current.right = new_node
                current = current.right
            
            if i < self.rows - 1:
                new_row_head = Node((i + 1) * self.cols)  
                current_row.down = new_row_head
                current_row = new_row_head

    def create_2d_back_array(self):
        if self.rows <= 0 or self.cols <= 0:
            return
        
        self.back_array_head = Node(0)  
        current_row = self.back_array_head
        
        for i in range(self.rows):
            current = current_row
            for j in range(1, self.cols):
                new_node = Node(i * self.cols + j)  
                current.right = new_node
                current = current.right
            
            if i < self.rows - 1:
                new_row_head = Node((i + 1) * self.cols)  
                current_row.down = new_row_head
                current_row = new_row_head