class TreeType:
    """Flyweight class representing shared data between trees (intrinsic state)."""
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Drawing a tree of type '{self.name}' with color '{self.color}' and texture '{self.texture}' at ({x}, {y})")


class TreeFactory:
    """Factory for managing and reusing tree types."""
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        """Get an existing tree type or create a new one if it doesn't exist."""
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]


class Tree:
    """A tree that has its position as external state, but shares type (intrinsic state)."""
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        """Delegate the drawing to the shared tree type."""
        self.tree_type.draw(self.x, self.y)


class Forest:
    """The forest manages many trees with shared types."""
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        """Plant a tree in the forest by using the Flyweight pattern to reuse tree types."""
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw_forest(self):
        """Draw all trees in the forest."""
        for tree in self.trees:
            tree.draw()


# Example usage
if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(10, 20, "Oak", "Green", "Rough")
    forest.plant_tree(15, 25, "Pine", "Dark Green", "Smooth")
    forest.plant_tree(10, 20, "Oak", "Green", "Rough")  # Reuses the same Oak type

    forest.draw_forest()
