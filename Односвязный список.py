class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self, value):
        self.start = Node(value)
        self.end = self.start
        self.length = 1

    def append(self, value):
        if self.start.next is None:
            self.start.next = Node(value)
            self.length += 1
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(value)
        self.end = temp.next
        self.length += 1

    def print(self):
        if self.start.next is None:
            print(self.start)
        temp = self.start
        ans = ''
        while temp is not None:
            ans += f"{temp.value} "
            temp = temp.next
        print(ans)

    def at(self, ind):
        temp = self.start
        for i in range(ind):
            if temp.next is not None:
                temp = temp.next
            else:
                return -1
        return temp.value

    def find(self, value):
        temp = self.start
        ind = 0
        while temp is not None:
            if temp.value == value:
                return ind
            temp = temp.next
            ind += 1
        return -1

    def pop(self):
        temp = self.start
        for i in range(self.length-2):
            print(f'{i+1}/{self.length}', temp.value)
            temp = temp.next
        temp.next = None
        self.length -= 1

a = List(6)
a.append(2)
a.append(3)
a.append(4)
a.append(10000)
a.print()
a.pop()
a.print()