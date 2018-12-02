class Component:
    """
    base class for a component in this game
    """

    def __init__(self, p_id):
        self.comp_id == p_id

    def __eq__(self, other):
        return self.comp_id == other.comp_id

    def tick():
        pass
