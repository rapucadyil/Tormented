import entity
import sprite
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

    def process(self, manager_list):
        for e in self.process_queue:
            if 'renderable' in e.flags:
                ent = entity.Entity(0, 'renderable_test', [], ['renderable'])
                ent.add_component(sprite.SpriteComponent("test"))
                self.instantiate(ent, manager_list)
                self.remove_from_queue(0)
            if 'possessable' in e.flags:
                print("possessable")

    def instantiate(self, e, manager_list):
        print(e.__str__())
        manager_list.append(e)
