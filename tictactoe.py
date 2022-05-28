#!/usr/var/python3
#win checking is bugged - see if you can spot it ;)
import random
import sys
import os

class TicTacToe:
    def __init__(self):
        self.board=[]
        self.DEBUG=True

    def create_board(self):
        for i in range(3):
            row=[]
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0,1)

    def fix_spot(self, row, col, player):
        if self.board[row][col] == '-':
            self.board[row][col] = player
            return True
        else:
            return False

    def win_check(self, player):
        win = None

        n = len(self.board)

        #run through checking rows
        for i in range(n):
            win = True
            for j in range (n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                if self.DEBUG:
                    print("row win")
                return win

        #run through checking cols
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                if self.DEBUG:
                    print("col win")
                return win

        #run through checking diagonals
        for i in range (n):
            win = True
            if self.board[i][i] != player:
                win = False
        if win:
            if self.DEBUG:
                print("diag1 win")
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            if self.DEBUG:
                print("diag2 win")
            return win
        return False
        
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    #check if the board is full
    def board_full(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    #change which player has the current turn
    def swap_turn(self, player):
        if self.DEBUG:
            print(player)
            player2 = 'X' if player == 'O' else 'O'
            print(player2)
        return 'X' if player == 'O' else 'O'
    
    #print board to stdout
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        #setup initial (blank) board state
        self.create_board()

        #randomly choose first player
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        
        #tracker for valid piece placement
        placed = True
        #tracker for new game in same launch
        play_again = 0

        while(True):

            #wipe terminal screen each pass
            os.system('cls' if os.name == 'nt' else 'clear')
            
            #check if last placed piece was valid and notify if error encountered
            if placed != True:
                print("The last placement was taken by another player, please try again")
            
            if play_again == 1:
                self.board = []
                self.create_board()
                player = 'X' if self.get_random_first_player() == 1 else 'O'
                play_again = 0
            #notify which player is taking the current turn
            print(f"Player {player}\'s turn")
            
            #print the current board state
            self.show_board()

            #get desired row and col for placement from player
            row, col = list(map(int, input("Enter the row and column numbers to place your piece <xy>: ")))
            print()
            
            #attempt placement of piece
            placed = self.fix_spot(row-1,col-1,player)

            #check if player has won and prompt for another game if wanted, if placement is invalid continue without swapping turns
            if (placed == True and self.win_check(player)) or (placed == True and self.board_full()):
                #notify who won the game - this is inefficient however still quick enough for my taste
                os.system('cls' if os.name == 'nt' else 'clear')
                self.show_board()
                if self.win_check(player):
                    print(f"{player} wins the game!")
                #notify if the game was a tie
                elif self.board_full():
                    print("The game is a tie!")

                play_again = 0
                
                #see if players want to go again, quit script if they do not
                while(play_again == 0):                    
                    player_input = input("Would you like to play again? (y/n): ")
                    #input validation
                    if (player_input == 'n' or player_input == 'N'):
                        sys.exit(0)
                    elif (player_input == 'y' or player_input == 'Y'):
                        #continue game
                        play_again = 1
                    else:
                        #input failed to validate
                        print("Please answer with 'y' or 'n'")
            
            elif (placed and self.board_full() != True):
                player = self.swap_turn(player)

TTT = TicTacToe()
TTT.start()

