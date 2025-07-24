from collections import Counter

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    count = Counter(opponent_history)
    if count:
        most_common_move = count.most_common(1)[0][0]
    else:
        most_common_move = "R"  # Default guess for first move
    winning_move = {
        "R": "P",  # Paper beats Rock
        "P": "S",  # Scissors beats Paper
        "S": "R"   # Rock beats Scissors
    }
    return winning_move[most_common_move]
