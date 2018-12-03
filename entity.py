class Entity:

    def __init__(self, p_id, p_name, p_comps=[], p_flags=[]):
        self.id = p_id
        self.name = p_name
        self.comps = p_comps
        self.flags = p_flags


    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.comps == other.comps and self.flags == other.flags

    def add_component(self, component):
        self.comps.append(component)

    