import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy, balls, zombies
    
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)
    
    balls = [Ball(random.randint(100, 1600-100), 50, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)



    game_world.add_collision_pair('boy:ball',boy,None)
    game_world.add_collision_pair('boy:zombie',boy,None)

    for ball in balls:
        game_world.add_collision_pair('boy:ball',None,ball)
    
    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie',None,zombie)
        game_world.add_collision_pair('ball:zombie',None,zombie)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here 충돌 처리
    game_world.handle_collision()


    '''
    for ball in balls.copy:#공을 지워도 문제 없게
        if game_world.collide(ball, boy):
            print('COLLISION boy:ball')
            boy.ball_count += 1
            game_world.remove_object(ball)
            balls.remove(ball)
    '''
    


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

