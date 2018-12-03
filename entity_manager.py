import entity
class EntityManager:

    def __init__(self):
        self.process_queue = []

    def add_to_queue(self, ent):
        if isinstance(ent, entity.Entity):
            self.process_queue.append(ent)

    def remove_from_queue(self, ent_id):
        for e in self.process_queue:
            if e.id == ent_id:
                self.process_queue.remove(e)

    def process(self):
        for e in self.process_queue:
            if 'renderable' in e.flags:
                ent = entity.Entity(0, 'test',[],['renderable'])
                # ent.add_component()
            if 'possessable' in e.flags:
                print("possessable")

    def instantiate(self, e):
        pass