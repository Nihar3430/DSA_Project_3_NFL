class RedBlackTree:
    class Node:
        def __init__(self, gameID_new, offense, defense, first_down_new, yards_new, rush_attempts_new, passes_new, incomplete_new, touchdown_new, sack_new, interception_new, fumble_new, color='red'):
            self.gameID = gameID_new
            self.offense = offense
            self.defense = defense
            self.first_down = first_down_new
            self.yards = yards_new
            self.rush_attempts = rush_attempts_new
            self.passes = passes_new
            self.incomplete = incomplete_new
            self.touchdown = touchdown_new
            self.sack = sack_new
            self.interception = interception_new
            self.fumble = fumble_new
            self.color = color
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def get_grandparent(self, node):
        if node.parent is None:
            return None
        return node.parent.parent

    def get_uncle(self, node):
        grandparent = self.get_grandparent(node)
        if grandparent is None:
            return None
        if node.parent == grandparent.left:
            return grandparent.right
        return grandparent.left

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def decision(self, node):
        if node.parent is None:
            node.color = "black"
            return

        if node.parent.color == "black":
            return

        parent = node.parent
        grandparent = self.get_grandparent(node)
        uncle = self.get_uncle(node)

        if uncle and uncle.color == "red":
            parent.color = "black"
            uncle.color = "black"
            grandparent.color = "red"
            self.decision(grandparent)
            return

        if node == parent.right and parent == grandparent.left:
            self.rotate_left(parent)
            node = parent
            parent = node.parent
        elif node == parent.left and parent == grandparent.right:
            self.rotate_right(parent)
            node = parent
            parent = node.parent

        parent.color = "black"
        grandparent.color = "red"
        if node == parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def insert(self, gameID, offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble):
        new_node = self.Node(gameID, offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble)
        if not self.root:
            self.root = new_node
            self.decision(new_node)
            return

        current = self.root
        while True:
            if gameID < current.gameID:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            elif gameID > current.gameID:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
            else:
                # gameID already exists
                current.first_down += new_node.first_down
                current.yards += new_node.yards
                current.rush_attempts += new_node.rush_attempts
                current.passes += new_node.passes
                current.incomplete += new_node.incomplete
                current.touchdown += new_node.touchdown
                current.sack += new_node.sack
                current.interception += new_node.interception
                current.fumble += new_node.fumble
                return

        self.decision(new_node)

    def search(self, gameID):
        current = self.root
        while current is not None:
            if gameID == current.gameID:
                return [current.gameID, current.offense, current.defense, current.first_down, current.yards, current.rush_attempts, current.passes, current.incomplete,current.touchdown, current.sack, current.interception, current.fumble]
            elif gameID < current.gameID:
                current = current.left
            else:
                current = current.right
        return None
    
