import click
from constants import PLAYER_X, PLAYER_Y
from game.map_generator import generate
from game.core import Game
from utils import get_bot


@click.command()
@click.option('--max-turns', default=10, help='Max number of game turns.')
@click.option('--player-x', default='random', help='First player.')
@click.option('--player-y', default='random', help='Second player.')
@click.option('--visualizer', default=True, help='Use visualization or not.')
@click.option('--map', default=None, help='Map to play the game in.')
def main(player_x, player_y, max_turns, visualizer, map_):
    if not map_:
        map_ = generate()

    game = Game(
        players={
            PLAYER_X: get_bot(player_x, PLAYER_X, player_y, map_),
            PLAYER_Y: get_bot(player_y, PLAYER_Y, player_x, map_),
        },
        max_turns=max_turns,
        map_=map_,
        visualizer=None,
    )
    game.play()


if __name__ == '__main__':
    main()
