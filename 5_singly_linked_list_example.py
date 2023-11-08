from typing import Any, Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __set_new_head(self, node: Node) -> None:
        self.__head = node

    def __set_new_tail(self, node: Node) -> None:
        self.__tail = node

    def head(self) -> Node:
        return self.__head

    def tail(self) -> Node:
        return self.__tail

    def __update_size(self) -> None:
        self.__size += 1

    def size(self) -> int:
        return self.__size

    def insure_index(self, index: int) -> None:
        try:
            if index > self.size():
                raise IndexError
        except ValueError:
            raise IndexError

    def append(self, data: Any) -> None:
        new_node = Node(data=data)
        if self.head() is None:
            self.__set_new_head(node=new_node)

        if self.tail() is None:
            self.__set_new_tail(node=new_node)
        else:
            self.tail().next = new_node
            self.__set_new_tail(node=new_node)

        self.__update_size()

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

        previous.next = current.next
        del current

    def pop(self, index: Optional[int] = None) -> Any:
        if index is None:
            index = self.size() - 1

        self.insure_index(index=index)

        count = 0
        previous = None
        current = self.head()

        while index != count:
            previous = current
            current = current.next
            count += 1

        if previous:
            if current.next:
                previous.next = current.next
            else:
                self.__set_new_tail(node=previous)
                previous.next = None
        else:
            self.__set_new_head(node=current)

        data = current.data
        del current

        return data

    def print_list(self) -> None:
        current = self.head()
        while current:
            print(current.data)
            current = current.next


if __name__ == '__main__':
    singly_list = SinglyLinkedList()
    singly_list.append(data='eggs')
    singly_list.append(data='bread')
    singly_list.append(data='cereal')
    print(singly_list.size())
    # singly_list.print_list()
    # singly_list.set(index=1, data='boobs')
    # singly_list.print_list()
    print('--------------------------')
    print(singly_list.pop())
    print(singly_list.pop(index=0))
    print('-----------------------')
    # singly_list.remove(index=5)
    singly_list.print_list()
