from infra import entity
import pygame
def main():
    e = entity.Entity(0, "rapucadyil")
    print(e.__str__())

if __name__ == '__main__':
    while True:
        main()