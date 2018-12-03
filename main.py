import pygame
import level
import entity_manager
import entity


player = entity.Entity(0, 'player', [], ['renderable'])#FIXME: have to make this come from a precompiled load file
enemy = entity.Entity(1, 'enemy', [], ['renderable'])#FIXME: have to make this come from a precompiled load file
enemy2 = entity.Entity(2, 'enemy2', [], ['renderable'])#FIXME: have to make this come from a precompiled load file

def main():
    first = level.Level()
    first.add_entity(player)
    first.add_entity(enemy)
    first.add_entity(enemy2)
    first.tick()

    for e in first.entites:
        print(e.name)

if __name__ == '__main__':
    main()
