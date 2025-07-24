from RPS import player

import RPS_game

# A simple random bot to play against
import random
def random_bot(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])

if __name__ == "__main__":
    # Play 1000 games between your player and random_bot
    RPS_game.play(player, random_bot, num_games=1000, verbose=False)

