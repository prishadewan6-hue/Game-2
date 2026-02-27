import chess
import random

def roll_dice():
    # Maps dice roll to chess piece types
    mapping = {1: chess.PAWN, 2: chess.KNIGHT, 3: chess.BISHOP, 
               4: chess.ROOK, 5: chess.QUEEN, 6: chess.KING}
    roll = random.randint(1, 6)
    return mapping[roll]

def play_dice_chess():
    board = chess.Board()
    piece_names = {1: 'Pawn', 2: 'Knight', 3: 'Bishop', 4: 'Rook', 5: 'Queen', 6: 'King'}

    while not board.is_game_over():
        print("\n", board)
        input(f"\n{'White' if board.turn else 'Black'}'s turn. Press Enter to roll...")
        
        roll = random.randint(1, 6)
        piece_type = {1: chess.PAWN, 2: chess.KNIGHT, 3: chess.BISHOP, 
                      4: chess.ROOK, 5: chess.QUEEN, 6: chess.KING}[roll]
        
        print(f"You rolled a {roll} ({piece_names[roll]})!")

        # Filter legal moves for the rolled piece type
        legal_moves = [m for m in board.legal_moves if board.piece_at(m.from_square).piece_type == piece_type]

        if not legal_moves:
            print("No legal moves for that piece. Turn skipped!")
            # Manually push a null move to switch turns
            board.push(chess.Move.null())
            continue

        print(f"Legal moves: {', '.join([board.san(m) for m in legal_moves])}")
        move_san = input("Enter your move (e.g., e4, Nf3): ")

        try:
            move = board.parse_san(move_san)
            if move in legal_moves:
                board.push(move)
            else:
                print("That piece doesn't match your roll!")
        except ValueError:
            print("Invalid move format.")

    print("Game Over!", board.result())

if __name__ == "__main__":
    play_dice_chess()
