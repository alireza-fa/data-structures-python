from typing import Any


class TreeNode:

    def __init__(self, value: Any, parent: Any | None = None) -> None:
        self.parent = parent
        self.value = value
        self.__children = []

    def add_child(self, value) -> None:
        new_child = TreeNode(value=value, parent=self)
        self.__children.append(new_child)

    def children(self) -> list:
        return self.__children

    def get_all_children(self) -> list:
        all_children = []
        depth_count = 0
        for child in self.__children:
            depth_count += 1
            all_children.append(child)
            all_children.extend(child.get_all_children())
        return all_children

    def depth(self) -> int:
        count = 0
        node = self
        while node and node.parent:
            node = node.parent
            count += 1
        return count

    def get_depth(self) -> int:
        if not self.__children:
            return 0
        else:
            child_depths = [child.get_depth() for child in self.__children]
            return max(child_depths) + 1

    def get_height(self) -> int:
        if not self.__children:
            return 0
        else:
            child_heights = [child.get_height() for child in self.__children]
            return max(child_heights) + 1

    def remove(self) -> None:
        parent = self.parent
        children = self.children()
        if parent:
            parent.__children.extend(children)
            parent.__children.remove(self)
        del self


class Tree:

    def __init__(self, value: Any) -> None: self.__root = self.__create_root(value=value)

    @staticmethod
    def __create_root(value: Any) -> TreeNode: return TreeNode(value=value)

    @property
    def root(self):
        return self.__root

    def __str__(self): return f'root name: {self.__root.value}'


if __name__ == '__main__':
    tree = Tree(value='root')
    tree.root.add_child(value='first_child')
    tree.root.add_child(value='second_child')
    print(tree.root.children())
    tree.root.children()[0].add_child(value='third_children')

    print(tree.root.get_all_children())
    print(tree.root.get_all_children()[0].children()[0].depth())
    print(tree.root.get_all_children()[0].remove())
    print(tree.root.get_all_children())
    print(tree.root.get_depth())
