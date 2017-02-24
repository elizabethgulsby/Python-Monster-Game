# DUH
import pygame; #see docs!  www.pygame.org/docs
# import sys;
# import settings from settings modules
from settings import Settings;
# get our hero class
from hero import Hero;
from game_functions import check_events;
# from pygame, get the sprite stuff and groupcollide to handle collisions on them
from pygame.sprite import Group, groupcollide;
# get our enemy class 
from enemy import Enemy;

# initialize all of the pygame modules
pygame.init();
# screen_size = (1000, 800); - now in settings
# make a background color! (The color of grass)
# bg_color = (82, 111, 53) - now in settings


# Put a message on the status bar so the player knows the name of the game
pygame.display.set_caption("Monster Attack!");
# Create an object out of our settings class
game_settings = Settings();
# set_mode() expects a tuple that sets the size of the screen (screen_size) - in settings
screen = pygame.display.set_mode(game_settings.screen_size);
hero = Hero(screen, game_settings);

enemies = Group();
enemies.add(Enemy(screen, game_settings));

# This loop will run forever...
while 1:  #1 pretty much always means true

	# run our check_events here!
	check_events(hero)

	# put our bg_color as the fill of our game
	screen.fill(game_settings.bg_color);
	# Update the hero moving booleans
	hero.update_me();
	# draw the hero!
	hero.draw_me();

	for enemy in enemies.sprites():
		enemy.update_me(hero);
		enemy.draw_me();

	# flip the screen = wipe it out
	pygame.display.flip();
