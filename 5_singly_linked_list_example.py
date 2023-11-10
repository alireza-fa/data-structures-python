from typing import Any, Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'data: {self.data}'


class SinglyLinkedList:

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def __update_size(self) -> None:
        self.__size += 1

    def insure_index(self, index: int) -> None:
        if index > self.size() - 1:
            raise IndexError

    def head(self) -> Node:
        return self.__head

    def tail(self) -> Node:
        return self.__tail

    def __set_head(self, node: Node) -> None:
        self.__head = node

    def __set_tail(self, node: Node) -> None:
        self.__tail = node

    def append(self, data: Any) -> None:
        new_node = Node(data=data)

        if self.head() is None:
            self.__set_head(node=new_node)

        if self.tail() is None:
            self.__set_tail(node=new_node)
        else:
            self.tail().next = new_node
            self.__set_tail(node=new_node)

        self.__update_size()

    def get_node(self, index: int) -> Node:
        self.insure_index(index=index)

        count = 0
        current = self.head()

        while index != count:
            current = current.next
            count += 1

        return current

    def get(self, index: int) -> Any:
        node = self.get_node(index=index)
        return node.data

    def set(self, index: int, data: Any) -> None:
        self.insure_index(index=index)

        count = 0
        current = self.head()

        while index != count:
            current = current.next
            count += 1

        current.data = data

    def remove(self, index: int) -> None:
        self.insure_index(index=index)

        count = 0
        previous = None
        current = self.head()

        while index != count:
            previous = current
            current = current.next
            count += 1

        if previous:
            previous.next = current.next
        else:
            self.__set_head(current.next)
        del current

    def pop(self, index: int = 0) -> Any:
        self.insure_index(index=index)

        count = 0
        previous = None
        current = self.head()

        while index != count:
            previous = current
            current = current.next
            count += 1

        if previous:
            previous.next = current.next
        else:
            self.__set_head(node=current.next)

        data = current.data
        del current
        return data

    def __str__(self) -> str:
        my_list = []

        current = self.head()

        while current:
            my_list.append(current.data)
            current = current.next

        return str(my_list)


if __name__ == '__main__':
    singly_list = SinglyLinkedList()
    singly_list.append(data='eggs')
    singly_list.append(data='bread')
    singly_list.append(data='cereal')
    singly_list.set(index=0, data='boobs')
    # singly_list.remove(3)
    singly_list.pop()
    singly_list.pop()
    print(singly_list)

