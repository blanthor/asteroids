import pygame
from asteroidfield import AsteroidField
from constants import  *
from player import Player
from asteroid import Asteroid


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)

    AsteroidField.containers = (updateable)
    asteroidfield = AsteroidField()
    print (asteroidfield)
    #updateable.add(asteroidfield)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        updateable.update(dt)

        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                exit(0)
                # Handle collision (e.g., remove asteroid, reduce player health, etc.)
                # asteroid.kill()  # Uncomment to remove the asteroid on collision
                # player.kill()    # Uncomment to remove the player on collision
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        
if __name__ == "__main__":
    main()