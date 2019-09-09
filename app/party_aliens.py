import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Kill the Part Aliens!")

    # Make play button.
    play_button = Button(ai_settings, screen, "Let's  go!")

    # Create an instance to store game statistics and create scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set background color.
    bg_color = (230, 230, 230)

    # Set background music.
    pygame.mixer.music.load('music/song.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
         
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()