from constants import *
from functions import *
from classes import *

def main():

    snake_a = Snake(
        Coord(272, 320),
        [Coord(272, 320), Coord(256, 320)],
        RIGHT,
        (32, 32),
        (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    )

    snake_b = Snake(
        Coord(864, 320),
        [Coord(864, 320), Coord(880, 320)],
        LEFT,
        (DISPLAY_WIDTH - 32, 32),
        (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    )

    berry_ls = [Berry(idx, Coord(-1, -1)) for idx in range(BERRY_NUM)]
    color_idx = 0
    berry_init = True
    fps = 7
    running = True

    while running:
        # Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                snake_a.change_dir(event.key)
                snake_b.change_dir(event.key)

        # Update       
        snake_a.move()
        snake_b.move()

        snake_a.collide_execute(snake_b)
        snake_b.collide_execute(snake_a)

        snake_a.get_berry(berry_ls)
        snake_b.get_berry(berry_ls)
    
        if snake_a.berry_idx != -1:
            berry_ls[snake_a.berry_idx].exist = False
            snake_a.berry_idx = -1
        if snake_b.berry_idx != -1:
            berry_ls[snake_b.berry_idx].exist = False
            snake_b.berry_idx = -1

        for idx in range(BERRY_NUM):
            if not berry_ls[idx].exist:
                berry_ls = spawn_berry(
                    idx,
                    berry_ls,
                    snake_a.body_coord_ls,
                    snake_b.body_coord_ls,
                    berry_init
                )
        berry_init = False

        # Render
        SCREEN.fill(BLACK)
        snake_a.show_score()
        snake_b.show_score()

        for body in snake_a.body_ls:
            draw_square(WHITE, body.x, body.y, SNAKE_SIZE)
        for body in snake_b.body_ls:
            draw_square(WHITE, body.x, body.y, SNAKE_SIZE)
        
        if gameover_execute(snake_a.alive, snake_b.alive):
            time.sleep(3)
            break

        for berry in berry_ls:
            if berry.score == 1:
                draw_square(RED, berry.pos.x, berry.pos.y, SNAKE_SIZE)
            elif berry.score == 3:
                draw_square(BLUE, berry.pos.x, berry.pos.y, SNAKE_SIZE)
            else:
                draw_square(
                    SUPER_COLOR_LS[color_idx], berry.pos.x, berry.pos.y, SNAKE_SIZE
                )
                color_idx = (color_idx + 1) % 3

        pygame.display.update()
        CLOCK.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
