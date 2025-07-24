def play(player1, player2, num_games=1000, verbose=False):
    # player1 and player2 are functions that take (prev_opponent_play) and return a move
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0

    for i in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if verbose:
            print(f"Game {i+1}: Player1={p1_move} Player2={p2_move}")

        winner = determine_winner(p1_move, p2_move)

        if winner == 1:
            p1_score += 1
        elif winner == 2:
            p2_score += 1

        p1_prev = p1_move
        p2_prev = p2_move

    print(f"Final score after {num_games} games: Player1={p1_score}, Player2={p2_score}")
    print(f"Player1 win rate: {p1_score/num_games*100:.2f}%")
    print(f"Player2 win rate: {p2_score/num_games*100:.2f}%")

def determine_winner(move1, move2):
    # Returns 1 if player1 wins, 2 if player2 wins, 0 if tie
    if move1 == move2:
        return 0
    if (move1 == "R" and move2 == "S") or (move1 == "S" and move2 == "P") or (move1 == "P" and move2 == "R"):
        return 1
    else:
        return 2

