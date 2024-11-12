world = [[] for _ in range(4)]
collision_pairs = {} # 충돌 검사를 수행할 빈 딕셔너리

def add_collision_pair(group,a,b):
    if group not in collision_pairs:
        collision_pairs[group] = [[], []]
    if a: collision_pairs[group][0].append(a)
    if b: collision_pairs[group][1].append(b)

def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o#메모리에서 객체를 삭제
            return
    raise ValueError('Cannot delete non existing object')

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def clear():
    for layer in world:
        layer.clear()



# fill here
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    # 충돌 판정
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    #모두 아니면 충돌
    return True

def handle_collision():
    #실제 검사를 진행 어떤 객체의 충돌도 사용 가능
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:#a리스트에서 하나
            for b in pairs[1]:#b리스트에서 하나
                if collide(a,b):#충돌 검사
                    print(f"{group} collide")
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

