class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self,childnode):
        childnode.parent = self
        self.children.append(childnode)

    def get_level_no(self):
        level = 0
        parent_node = self.parent
        while parent_node :
            level = level + 1
            parent_node = parent_node.parent

        return level

    def display_tree(self,level):
        if self.get_level_no() <= level:
            suffix = self.get_level_no() * " "*3 + "|__" if self.parent else ""
            print( suffix +self.data)

            for i in self.children:
                res1 = i.display_tree(level)



global_node = TreeNode('Global')
india_node = TreeNode('India')
usa_node = TreeNode('USA')
global_node.add_child(india_node)
global_node.add_child(usa_node)

gujarat_node = TreeNode('Gujarat')
karnataka_node = TreeNode('Karnataka')
india_node.add_child(gujarat_node)
india_node.add_child(karnataka_node)

newjersey_node = TreeNode('New Jersey')
california_node = TreeNode('California')
usa_node.add_child(newjersey_node)
usa_node.add_child(california_node)

gujarat_node.add_child(TreeNode('Ahmedabad'))
gujarat_node.add_child(TreeNode('Baroda'))

karnataka_node.add_child(TreeNode('Bengaluru'))
karnataka_node.add_child(TreeNode('Mysore'))

newjersey_node.add_child(TreeNode('Princeton'))
newjersey_node.add_child(TreeNode('Trenton'))

california_node.add_child(TreeNode('San Fransisco'))
california_node.add_child(TreeNode('Mountain View'))
california_node.add_child(TreeNode('Palo Alto'))

print('Upto level 1')
global_node.display_tree(1)
print('Upto level 2')
global_node.display_tree(2)
print('Upto level 3')
global_node.display_tree(3)
