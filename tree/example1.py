class HierarchyTreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.parent = None
        self.children = []
        self.designation = designation

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def display_hierarchy(self,value):
        data = ""
        if value == 'Name':
            data = self.name
        elif value == 'Designation':
            data = self.designation
        elif value == 'both':
            data = self.name + " ("+self.designation + " )"

        print(self.level_of_node()*" "*4 +str(data))
        for i in self.children:
            i.display_hierarchy(value)

    def level_of_node(self):
        level = 0
        parent_node = self.parent
        while parent_node:
            parent_node = parent_node.parent
            level = level + 1
        #print(level, self.name)
        return level



def build_tree():
    nilupul = HierarchyTreeNode("Nilupul",'CEO')
    chinmay = HierarchyTreeNode('Chinmay','CTO')
    gels = HierarchyTreeNode('Gels','HR Head')
    nilupul.add_child(chinmay)
    nilupul.add_child(gels)

    vishwa = HierarchyTreeNode('vishwa',"Infrastructure Head")
    Aamir = HierarchyTreeNode('Aamir','Application Head')
    chinmay.add_child(vishwa)
    chinmay.add_child(Aamir)

    vishwa.add_child(HierarchyTreeNode('Abhijit','App Manager'))
    vishwa.add_child(HierarchyTreeNode('Dhaval','Cloud Manager'))

    gels.add_child(HierarchyTreeNode('Peter','Recruitment Manager'))
    gels.add_child(HierarchyTreeNode('Waqas','Policy Manager'))
    return nilupul


if __name__ == "__main__" :
    root = build_tree()
    root.display_hierarchy('Name')
    root.display_hierarchy('Designation')
    root.display_hierarchy('both')