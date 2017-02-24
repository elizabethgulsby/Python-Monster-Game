import pygame;
from pygame.sprite import Sprite;
import math;

class Enemy(Sprite):
	def __init__(self, screen, game_settings):
		super(Enemy, self).__init__(); #passes our stuff up to parent
		# load the image
		self.image = pygame.image.load('monster1.png');
		# set the speed
		self.speed = 2;
		# Find the location and size of the image just loaded
		self.rect = self.image.get_rect();
		# Find the location and size of the screen
		self.screen_rect = screen.get_rect();
		# set up the screen
		self.screen = screen;
		# set the center of the image...
		self.rect.centery = self.screen_rect.centery;
		self.rect.right = self.screen_rect.right;

	def update_me(self, hero):
		dx = self.rect.x - hero.rect.x;  #where the monster is (x) - where hero is (x)
		dy = self.rect.y - hero.rect.y;  #where the monster is (y) - where hero is (y)
		dist = math.hypot(dx, dy);
		dx = dx / dist;
		dy = dy / dist;

		self.rect.x -= dx * self.speed;
		self.rect.y -= dy * self.speed;

	def draw_me(self):
		self.screen.blit(self.image, self.rect);


