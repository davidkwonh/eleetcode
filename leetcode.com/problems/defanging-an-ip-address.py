class Solution(object):
    def defangIPaddr(self, address):
        # ADD EACH CHARACTER INTO A stack and then for each . perpend and append a close and open bracket
        # address is saved as a string
        queue = []
        new_address = ""  # memory alocation for output
        for char in address:  # Taking the address and putting into a queue
            queue.append(char)

        while queue:
            current = queue.pop(0)  # Changes LIFO to FIFO
            if current == '.':
                new_address += '['
                new_address += current
                new_address += ']'
            else:
                new_address += current
        return new_address
