import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	all_asteroids = pygame.sprite.Group()
	Asteroid.containers = (updatable, drawable, all_asteroids)

	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
	
		screen.fill("black")
		dt = clock.tick(60) / 1000
		
		for each in updatable:
			each.update(dt)

		for asteroid in all_asteroids:
			if player.collide(asteroid):
				sys.exit("Game over!")
		
		for each in drawable:
			each.draw(screen)
		
		pygame.display.flip()


if __name__ == "__main__":
	main()

