class Entity:
    """
    a base class for any object that is represented in this game
    """

    def __init__(self, p_id, p_name, p_components=[], p_flags=[]):
        self.id = p_id
        self.name = p_name
        self.components = p_components
        self.flags = p_flags


    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.components == other.components and self.flags == other.flags


    def __str__(self):
        return 'Entity, Id: {}, Name: {}, Components: {}, Flags: {}'.format(self.id,self.name,self.components,self.flags)
    
    def add_component(self, component):
        self.components.append(component)

    def get_component(self, comp_id):
        for comp in self.components:
            if comp.comp_id == comp_id:
                return comp
            else:
                return None