from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 0):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity  = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())#tuple을 풀어헤친다
    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time
        # 시야를 벗어나면 사라짐
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):

        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):

        if group == 'boy:ball' or group == 'ball:zombie':
            game_world.remove_object(self)#게임 월드에서 제거


            
