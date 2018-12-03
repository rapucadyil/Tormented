import entity_manager
class Level:

    def __init__(self):
        self.entites = []
        self.manager = entity_manager.EntityManager()

    def add_entity(self, e):
        self.manager.add_to_queue(e)

    def remove_entity(self, e_id):
        pass

    def tick(self):
        self.manager.tick(self.entites)