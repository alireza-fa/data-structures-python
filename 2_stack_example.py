from typing import Any


class Stack(list):

    def add(self, value) -> None:
        self.append(value)

    def size(self) -> int:
        return len(self)

    def get_last(self) -> Any:
        try:
            return self[-1]
        except IndexError:
            raise IndexError('Stack index out of range')

    def pop(self) -> Any:
        try:
            return super().pop()
        except IndexError:
            raise IndexError('pop from empty stack.')

    def top(self) -> Any:
        return self.get_last()


if __name__ == '__main__':
    pass
