import pygame
import entity_manager
import entity
def main():
    lvl = entity_manager.EntityManager()
    lvl.add_to_queue(entity.Entity(0, "test", [], ['renderable', 'possessable']))
    lvl.process()

if __name__ == '__main__':
    pass