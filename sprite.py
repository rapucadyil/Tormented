import component
class SpriteComponent(component.Component):

    def __init__(self, flp):
        super(SpriteComponent, self).__init__(0,'sprite')
        self.file = flp

    def tick(self):
        print("ticking...")

    def draw(self):
        pass