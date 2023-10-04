UP, DOWN = 'up', 'down'
UNFOLDED, FOLDED = 'unfolded', 'folded'
motors = [None] + ([0, 0]+[UP]+[UNFOLDED]*5)
def move_motor1(x):
    print(f'모터1을 사용해 x{motors[1]}에서부터 x방향으로 {x-motors[1]}만큼 이동합니다')
    motors[1] = x
    return True
def move_motor2(y):
    print(f'모터2를 사용해 y{motors[2]}에서부터 y방향으로 {y-motors[2]}만큼 이동합니다')
    motors[2] = y
    return True
def move_motor3(direction):
    if direction == DOWN:
        if motors[3] == DOWN:
            return False
        print('모터3을 사용해 팔을 내립니다')
        motors[3] = DOWN
    else:
        if motors[3] == UP:
            return False
        print('모터3을 사용해 팔을 올립니다')
        motors[3] = UP
    return True

def unfold(motor):
    if motors[motor] == UNFOLDED:
        return False
    print('모터{}{} 사용해 손가락을 '
          '폅니다'.format(motor, '를' if motor in (4,5) else '을'))
    motors[motor] = UNFOLDED
    return True

def fold(motor):
    if motors[motor] == FOLDED:
        return False
    print('모터{}{} 사용해 손가락을 '
          '접습니다'.format(motor, '를' if motor in (4,5) else '을'))
    motors[motor] = FOLDED
    return True

def grab():
    state = []
    for motor in range(4, 9):
        state.append(fold(motor))
    if motors[3] == DOWN and all(state):
        return True
    return False

def let_go():
    state = []
    for motor in range(4, 9):
        state.append(unfold(motor))
    if motors[3] == DOWN and all(state):
        return True
    return False

def move_motor_xy(x, y):
    return True if move_motor1(x) and move_motor2(y) else False

def move_item(x, y, x2, y2):
    move_motor_xy(x, y)
    move_motor3(DOWN)
    grab()
    move_motor3(UP)
    move_motor_xy(x2, y2)
    move_motor3(DOWN)
    let_go()
    move_motor3(UP)

def 을(num):
    return '을' if num%10 not in [2,4,5,9] else '를'
from enum import Enum, auto
class State(Enum):
    UP = '팔을 올립니다'
    DOWN = '팔을 내립니다'
    UNFOLDED = '손가락을 폅니다'
    FOLDED = '손가락을 접습니다'
    LEG = auto()
    X = 'x'
    Y = 'y'
class Motor(object):
    motors = [None]
    def __init__(self, d_list=set(), cur=None):
        self.n = len(self.motors)
        self.d_list = d_list    #direction or destination
        self.cur = cur
        self.motors.append(self)
    def move(self, d):
        str_using = f'모터{self.n}{을(self.n)} 사용해 '
        if State.LEG in self.d_list:
            axis = (self.d_list - {State.LEG}).pop()
            action_str = str_using + (f'{axis.value}{self.cur}에서부터 '
            f'{axis.value}방향으로 {d-self.cur}만큼 이동합니다')
            print(action_str)
            self.cur = d
            return True
        else:
            if d in self.d_list:
                if self.cur == d:
                    return False
                action_str = str_using + d.value
                print(action_str)
                self.cur = d
                return True
            return False
class Finger(object):
    def __init__(self):
        self.motor = Motor({State.FOLDED,State.UNFOLDED}, State.UNFOLDED)
    def fold(self):
        return self.motor.move(State.FOLDED)
    def unfold(self):
        return self.motor.move(State.UNFOLDED)
class Hand(object):
    def __init__(self, cur=State.UP, cur_finger=State.UNFOLDED):
        self.cur = cur
        self.fingers = []
        for i in range(5):
            self.fingers.append(Finger())
    def grab(self):
        state = []
        for finger in self.fingers:
            state.append(finger.fold())
        if self.cur == State.DOWN and all(state):
            return True
        return False
    def let_go(self):
        state = []
        for finger in self.fingers:
            state.append(finger.unfold())
        if self.cur == State.DOWN and all(state):
            return True
        return False
class Arm(object):
    def __init__(self):
        self.motor = Motor({State.UP, State.DOWN}, State.UP)
        self.hand = Hand()
    def move(self, direction):
        self.motor.move(direction)
        self.hand.cur = direction

class Leg(object):
    def __init__(self):
        self.motors = []
        for axis in (State.X, State.Y):
            self.motors.append(Motor({State.LEG, axis}, 0))
    def move(self, x, y):
        self.motors[0].move(x)
        self.motors[1].move(y)
        
class Crane(object):
    def __init__(self):
        self.leg = Leg()
        self.arm = Arm()
    def move_item(self, x, y, x2, y2):
        self.leg.move(x, y)
        self.arm.move(State.DOWN)
        self.arm.hand.grab()
        self.arm.move(State.UP)
        self.leg.move(x2, y2)
        self.arm.move(State.DOWN)
        self.arm.hand.let_go()
        self.arm.move(State.UP)

move_item(1,3,4,5)
move_item(1,3,4,5)
print()
c = Crane()
c.move_item(1,3,4,5)
c.move_item(1,3,4,5)
print()
