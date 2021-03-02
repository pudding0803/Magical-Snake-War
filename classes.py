from constants import *


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __getattr__(self, attr):
        if attr == 'coord':
            return (self.x, self.y)


class Snake:
    def __init__(self, head, body_ls, dir, score_coord, key_tp):
        self.head = head
        self.body_ls = body_ls
        self.dir = dir
        self.score = 0
        self.score_coord = score_coord
        self.key_tp = key_tp
        self.berry_idx = -1
        self.alive = True
        self.pop_immune = 0

    def __getattr__(self, attr):
        if attr == 'head_coord':
            return self.head.coord
        if attr == 'body_coord_ls':
            return [body.coord for body in self.body_ls]

    def change_dir(self, key):
        if key in self.key_tp:
            if (key == pygame.K_UP or key == pygame.K_w) and self.dir != DOWN:
                self.dir = UP
            elif (key == pygame.K_DOWN or key == pygame.K_s) and self.dir != UP:
                self.dir = DOWN
            elif (key == pygame.K_LEFT or key == pygame.K_a) and self.dir != RIGHT:
                self.dir = LEFT
            elif (key == pygame.K_RIGHT or key == pygame.K_d) and self.dir != LEFT:
                self.dir = RIGHT

    def move(self):
        if self.dir == UP:
            self.head.y -= SNAKE_SIZE
        elif self.dir == DOWN:
            self.head.y += SNAKE_SIZE
        elif self.dir == LEFT:
            self.head.x -= SNAKE_SIZE
        elif self.dir == RIGHT:
            self.head.x += SNAKE_SIZE
        self.body_ls.insert(0, Coord(self.head.x, self.head.y))
        if self.pop_immune:
            self.pop_immune -= 1
        else:
            self.body_ls.pop()
    
    def get_berry(self, berry_ls):
        for berry in berry_ls:
            if self.head_coord == berry.coord:
                self.score += berry.score
                self.pop_immune += berry.score
                self.berry_idx = berry.index
                break

    def show_score(self):
        text = SCORE_FONT.render(str(self.score), True, WHITE)
        rect = text.get_rect()
        rect.center = self.score_coord
        SCREEN.blit(text, rect)

    def collide_execute(self, other):
        if self.head.x < 0 or self.head.x + SNAKE_SIZE > DISPLAY_WIDTH \
                    or self.head.y < 0 or self.head.y + SNAKE_SIZE > DISPLAY_HEIGHT:
            print('died from edge')
            self.alive = False
        elif self.head_coord in self.body_coord_ls[1:]:
            print('died from self body')
            print(self.head_coord, self.body_coord_ls)
            self.alive = False
        elif self.head_coord in other.body_coord_ls:
            print('died from another body')
            print(self.head_coord, other.body_coord_ls)
            self.alive = False


class Berry:
    def __init__(self, index, pos, exist=False, score = 1):
        self.index = index
        self.pos = pos
        self.exist = exist
        self.score = score
        self.color_idx = 0
        self.remote = 0
    
    def __getattr__(self, attr):
        if attr == 'coord':
            return self.pos.coord;
