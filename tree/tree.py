
class TreeNode:
    def __init__(self,data):
        self.root = None
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child_node):
        child_node.parent = self
        self.children.append(child_node)

    def level_of_node(self):
        level = 0
        parent_node = self.parent
        while parent_node:
            parent_node = parent_node.parent
            level = level+1
        return level

    def display_tree(self):
        level = self.level_of_node()
        print(level*' '*5 + self.data)
        for i in self.children:
            i.display_tree()

    def search(self,value):

        if self.data == value:
            return True

        for i in self.children:
            res1 = i.search(value)
            if res1 :
                return True


if __name__ == "__main__":
    electronics = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    electronics.add_child(laptop)
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('LG'))
    laptop.add_child(TreeNode('Asus'))
    tv = TreeNode('tv')
    electronics.add_child(tv)
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Sony'))
    cellphone = TreeNode('cell phone')
    electronics.add_child(cellphone)
    cellphone.add_child(TreeNode('Nokia'))
    cellphone.add_child(TreeNode('Motorola'))
    electronics.display_tree()
    print('searching for Samsung1',electronics.search('Samsung1'))
    print('searching for Samsung', electronics.search('Samsung'))
