from typing import Any


class Queue(list):

    def add(self, value) -> None:
        self.append(value)

    def size(self) -> int:
        return len(self)

    def get_first(self) -> Any:
        try:
            return self[0]
        except IndexError:
            raise IndexError('Queue index out of range')

    def get_last(self) -> Any:
        try:
            return self[-1]
        except IndexError:
            raise IndexError('Queue index out of range')

    def take(self) -> Any:
        first = self.get_first()
        del self[0]
        return first

    def head(self) -> Any:
        return self.get_first()

    def tail(self) -> Any:
        return self.get_last()


if __name__ == '__main__':
    pass
