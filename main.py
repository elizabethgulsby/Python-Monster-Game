# DUH
import pygame; #see docs!  www.pygame.org/docs
# we need sys to halt the program
import sys;
# import settings from settings modules
from settings import Settings;
from hero import Hero;

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

# This loop will run forever...
while 1:
	for event in pygame.event.get():
		# this means the user clicked on the red x
		if event.type == pygame.QUIT:
			# Stop the game, the user wants off
			sys.exit();

		# check for key press!
		elif event.type == pygame.KEYDOWN:
			# print event.key;
			# user pressed a key AND it's one of the following arrows
			if event.key == pygame.K_RIGHT:
				print "Pressed right";
				# set the hero boolean for right to True
				hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				print "Pressed left";
				hero.moving_left = True;
			elif event.key == pygame.K_UP:
				print "Pressed up";
				hero.moving_up = True;
			elif event.key == pygame.K_DOWN:
				print "Pressed down";
				hero.moving_down = True;

		#check for key being let go!
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				print "Not pressed right";
				hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				print "Not pressed left";
				hero.moving_left = False;
			elif event.key == pygame.K_UP:
				print "Not pressed up";
				hero.moving_up = False;
			elif event.key == pygame.K_DOWN:
				print "Not pressed down";
				hero.moving_down = False;

	# put our bg_color as the fill of our game
	screen.fill(game_settings.bg_color);
	# Update the hero moving booleans
	hero.update_me();
	# draw the hero!
	hero.draw_me();
	# flip the screen = wipe it out
	pygame.display.flip();
