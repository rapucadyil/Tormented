import pygame
import entity_manager
import entity


def main():
    lvl_lst = [] #FIXME: needs to be removed from here
    lvl = entity_manager.EntityManager()
    lvl.add_to_queue(entity.Entity(0, "test", [], ['renderable'])) #FIXME: make a parser for entity types to be passed in
    lvl.process(lvl_lst)
    print(lvl.process_queue)
    lvl_lst[0].comps[0].tick()


if __name__ == '__main__':
    main()
