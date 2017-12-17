class node:
    value = -1

class node_list_c:

    def __init__(self):
        self.first_node = node()
        self.first_node.value = 0
        self.first_node.next_node = self.first_node

        self.current_node = self.first_node
        self.next_value = 1


    def do_insert(self, step):
        
        # advance to the node before where we want to insert a node
        for i in range(step):
            self.current_node = self.current_node.next_node


        # create the new node
        new_node = node()
        new_node.next_node = self.current_node.next_node
        new_node.value = self.next_value
        self.next_value += 1
        self.current_node.next_node = new_node
        self.current_node = new_node

    def get_value_sequence(self):
        return_list = list()
        it = self.first_node
        for i in range(self.next_value): # next_value is also the number of nodes
            return_list.append(it.value)
            it = it.next_node
        return return_list
            


if __name__ == "__main__":

    node_list = node_list_c()

    step = 371 # puzzle input

    for i in range(2017):
        node_list.do_insert(step)

    part1_value = node_list.current_node.next_node.value
    print(f"Part 1: {part1_value}")

    # part 2 requires looking for the value after node 0 after 50 million insertions 
    # to speed things up and not use as much memory, since node 0 is always the beginning of the circular
    # buffer, just note when items are inserted after zero

    # i just fiddled with this general idea of using mod and checking if the current node was 0-ish
    # until the problem sample gave the right solution
    current_node = 0
    value_after_zero = 0
    for i in range(50000000):

        if current_node == 1:
            value_after_zero = i

        length = i+1
        current_node = ((current_node + step) % length) + 1



        if i % 100000 == 0:
            print(f"len: {length}  current node: {current_node}")


    print(f"Part 2: {value_after_zero}")
