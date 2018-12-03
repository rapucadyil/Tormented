class Level:

    def __init__(self):
        self.entites = []
        self.managers = []

    def add_entity(self, e):
        self.entites.append(e)

    def remove_entity(self, e_id):
        pass