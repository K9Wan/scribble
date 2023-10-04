#include <stdio.h>

typedef enum State {UP, DOWN, UNFOLDED, FOLDED} State;
enum {False, True};
int motors[] = {-1, 0, 0, UP, UNFOLDED, UNFOLDED, UNFOLDED, UNFOLDED, UNFOLDED};

_Bool move_motor1(int x)
{
    printf("모터1을 사용해 x%d에서부터 x방향으로 %d만큼 이동합니다\n", motors[1], x-motors[1]);
    motors[1] = x;
    return True;
}

_Bool move_motor2(int y)
{
    printf("모터2를 사용해 y%d에서부터 y방향으로 %d만큼 이동합니다\n", motors[2], y-motors[2]);
    motors[2] = y;
    return True;
}

_Bool move_motor3(State direction)
{
    if(direction == DOWN)
    {
        if(motors[3] == DOWN)
        {
            return False;
        }
        puts("모터3을 사용해 팔을 내립니다");
        motors[3] = DOWN;
    }
    else
    {
        if(motors[3] == UP)
        {
            return False;
        }
        puts("모터3을 사용해 팔을 올립니다");
        motors[3] = UP;
    }
    return True;
}

char * eul2(int);
char * eul3(int);
char * eul(int num)
{
    //return eul2(num);
    //return eul3(num);
    switch(num)
    {
        case 2:
        case 4:
        case 5:
        case 9:
        return "를";
        default:
        return "을";
    }
}

_Bool unfold(int motor)
{
    if(motors[motor] == UNFOLDED)
    {
        return False;
    }
    printf("모터%d%s 사용해 손가락을 폅니다\n", motor, eul(motor));
    motors[motor] = UNFOLDED;
    return True;
}

_Bool fold(int motor)
{
    if (motors[motor] == FOLDED)
    {
        return False;
    }
    printf("모터%d%s 사용해 손가락을 접습니다\n", motor, eul(motor));
    motors[motor] = FOLDED;
    return True;
}

_Bool grab(void)
{
    _Bool state[5] = {0};
    for (int i=0; i<5; i++)
    {
        state[i] = fold(4 + i);
    }
    _Bool is_success = False;
    if (motors[3] == DOWN)
    {
        is_success = True;
        for(int i=0; i<5; i++)
        {
            if(!state[i])
            {
                is_success = False;
            }
        }
    }
    return is_success;
}

_Bool let_go(void)
{
    _Bool state[5] = {0};
    for (int i=0; i<5; i++)
    {
        state[i] = unfold(4 + i);
    }
    _Bool is_success = False;
    if (motors[3] == DOWN)
    {
        is_success = True;
        for(int i=0; i<5; i++)
        {
            if(!state[i])
            {
                is_success = False;
            }
        }
    }
    return is_success;
}

_Bool move_motor_xy(int x, int y)
{
    return (move_motor1(x) && move_motor2(y)) ? True : False;
}

void move_item(int x, int y, int x2, int y2)
{
    move_motor_xy(x, y);
    move_motor3(DOWN);
    grab();
    move_motor3(UP);
    move_motor_xy(x2, y2);
    move_motor3(DOWN);
    let_go();
    move_motor3(UP);
}

int main(void)
{
    move_item(1, 3, 4, 5);
    move_item(1, 3, 4, 5);

    return 0;
}

char * eul2(int num)
{
    char * mr_toe = NULL;
    switch(num)
    {
        case 2:
        case 4:
        case 5:
        case 9:
        mr_toe = "를";
        break;
        default:
        mr_toe = "을";
        break;
    }
    return mr_toe;
}

inline char * eul3(int num)
{
    return (num == 2 || num == 4 || num == 5 || num == 9) ? "를" : "을";
}