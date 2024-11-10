# define the heap class

class BinaryHeap:
    """An object class that creates a minimum-sorted heap object.
    
    Attributes:
        insert_key: Adds a new node to the heap.
        delete_min: Deletes the minimum-valued node from the heap.
        increase_key: Increase the value of a node at a specific position.
        decrease_key: Decrease the value of a node at a specific position.
        sift_up: Implements the sift-up procedure to restore the heap properties.
        sift_down: Implements the sift-down procedure to restore the heap properties.
        print_heap: Prints out the heap elements in order.
    """
    def __init__(self, l: list = []):  # noqa: E741
        #todo add initialization "heapify" given list?
        self.heap = l
    
    def insert_key(self, value: int):
        """Adds a new node to the heap.

        Args:
            value (int or float): the value to assign to the new node.
        """
        # add key to the end of the heap
        self.heap.append(value)
        
        # use sift up to place the key in the right place
        position = len(self.heap) - 1
        self.sift_up(position)
            
    def delete_min(self):
        """Deletes the minimum-valued node from the heap.
        """
        if not self.heap:
            raise IndexError("Unable to delete the minimum value. The heap is empty.")
        # use pop() to remove the last item and store the value
        new_value = self.heap.pop()
        # end function if the heap has only 1 node
        if not self.heap:
            pass
        else:
            # set the 0 index value to the removed value above
            self.heap[0] = new_value
            #perform sift down to restore heap properties
            self.sift_down(0)
    
    def increase_key(self, position: int, new_value: int):
        """Increase the value of a node at a specific position.

        Args:
            position (int): position of the node within the heap structure.
            new_value (int or float): the new value to assign to the node.
        """
        if new_value < self.heap[position]:
            raise ValueError("The new value must be greater than the current value of the node.")

        # assign the new value to the node at the given position
        self.heap[position] = new_value
        # perform sift down to adjust the position of the node based on the new value
        self.sift_down(position)
    
    def decrease_key(self, position: int, new_value: int):
        """Decrease the value of a node at a specific position.

        Args:
            position (int): position of the node within the heap structure.
            new_value (int or float): the new value to assign to the node.
        """
        if new_value > self.heap[position]:
            raise ValueError("The new value must be less than the current value of the node.")

        # assign the new value to the node at the given position
        self.heap[position] = new_value
        # perform sift up to adjust the position of the node based on the new value
        self.sift_up(position)
    
    def sift_up(self, position: int):
        """Implements the sift-up procedure to restore the heap properties.

        Args:
            position (int): position of the node to be sifted up.
        """
        # if there is 1 or fewer nodes then sifting is complete.
        if len(self.heap) <= 1:
            pass
        
        while position != 0:
            
            # get the index of the parent node
            parent = self.find_parent(position)
            
            # find the values of the current node and parent node
            current_value = self.heap[position]
            parent_value = self.heap[parent]
            
            if parent_value > current_value:
                self.heap[parent] = current_value
                self.heap[position] = parent_value
                position = parent
            else:
                break
    
    def sift_down(self, position: int):
        """Implements the sift-down procedure to restore the heap properties.

        Args:
            position (int): position of the node to be sifted down.
        """
        # if there is 1 or fewer nodes then sifting is complete.
        if len(self.heap) <= 1:
            pass
        
        # loop to compare the value of the current node to the children and swap as needed
        while position != len(self.heap) - 1:
        
            # get the indices of the children.
            left_child, right_child = self.find_children(position)
            # get the value of the current position
            current_value = self.heap[position]
            
            # if there are no children then sifting is complete.
            if left_child == -1 & right_child == -1:
                break
            
            # if there is no right child then only compare left child
            elif right_child == -1:
                left_child_value = self.heap[left_child]
                
                if left_child_value < current_value:
                    self.heap[left_child] = current_value
                    self.heap[position] = left_child_value
                    position = left_child
                    
                else:
                    # if current value is less than left child then end
                    break
            
            # if left and right children exist then compare both to the current value
            else:
                left_child_value = self.heap[left_child]
                right_child_value = self.heap[right_child]
                
                # one of the child values must be less than the current value to continue
                if current_value > left_child_value or current_value > right_child_value:
                    # find which child is smallest
                    if left_child_value < right_child_value:
                        # swap current position with the left child
                        self.heap[left_child] = current_value
                        self.heap[position] = left_child_value
                        position = left_child
                        
                    else:
                        # if not left then it must be right
                        self.heap[right_child] = current_value
                        self.heap[position] = right_child_value
                        position = right_child
                        
                else:
                    # if current value is less than both children then end
                    break
                
    def find_parent(self, position: int):
        """Finds the index of the parent node of the given index.

        Args:
            position (int): the index of the target node.

        Returns:
            parent_index (int): the integer value for the index of the parent node. If there is no parent, returns -1.
        """
        if position >= len(self.heap):
            raise IndexError("Position is outside the index range of the heap.")
        if position == 0:
            return -1
        else:
            parent_index = (position - 1) // 2
            return parent_index
        
    def find_children(self, position: int):
        """Find the indices of the children of the given index.

        Args:
            position (int): the index of the target node.

        Returns:
            children_index (tuple): a tuple containing the indices of the children. If no child exists returns -1 instead.
        """
        if position >= len(self.heap):
            raise IndexError("Position is outside the index range of the heap.")
        if position == len(self.heap) - 1:
            return -1, -1
        else:
            left_child_index = 2 * position + 1
            right_child_index = 2 * position + 2
            if right_child_index <= len(self.heap) - 1:
                return left_child_index, right_child_index
            elif left_child_index <= len(self.heap) - 1:
                return left_child_index, -1
            else:
                return -1, -1
    
    def print_heap(self):
        """Prints out the heap elements in order.
        """
        #todo: print out the heap list/array visually
        print(self.heap)