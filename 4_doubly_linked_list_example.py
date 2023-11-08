from typing import Any


class Node:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.pre = None

    def __str__(self):
        return f'data: {self.data}'


class DoubleLinkedList:

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

        if self.head() is None and self.tail() is None:
            self.__set_head(node=new_node)
            self.__set_tail(node=new_node)
            self.__update_size()
            return

        self.tail().next = new_node
        new_node.pre = self.tail()
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

    def remove(self, index: int) -> None:
        current = self.get_node(index=index)

        if current.pre:
            current.pre.next = current.next
        else:
            self.__set_head(node=current.next)

        if current.next:
            current.next.pre = current.pre
        else:
            self.__set_tail(node=current.pre)

        del current

    def insert(self, index: int, data: Any) -> None:
        current = self.get_node(index=index)

        new_node = Node(data=data)
        new_node.next = current
        new_node.pre = current.pre

        if current.next:
            pass

        if current.pre:
            current.pre.next = new_node
        else:
            self.__set_head(node=new_node)

        self.__update_size()

    def pop(self):
        if self.tail():
            if self.tail().pre:
                self.tail().pre.next = None
                self.__set_tail(node=self.tail().pre)
                data = self.tail().data
            else:
                data = self.tail().data
                self.__head = None
                self.__tail = None

            return data

        return ValueError('Double linked list is empty.')

    def __str__(self) -> str:
        my_list = []

        current = self.head()

        while current:
            my_list.append(current.data)
            current = current.next

        return str(my_list)


if __name__ == '__main__':
    d_list = DoubleLinkedList()

    d_list.append(data='a')
    d_list.append(data='b')
    d_list.append(data='c')

    d_list.insert(index=1, data='d')
    d_list.insert(index=1, data='j')
    d_list.remove(index=1)
    d_list.remove(index=1)
    d_list.remove(index=1)

    print(d_list)

    # print(d_list.get(index=0))
    print(d_list.pop())
    print(d_list)
    print(d_list.pop())
    print(d_list.pop())
