from class_figure import Figure
from class_board import Board


class Game:
    """
    Class Game. It presents game with text interface in terminal.
    """

    def print_b(self, board):
        """Prints new line and then gameboard"""
        print()
        print(board)

    def start_choice_print(self, board, place):
        """
        Starts game from rules or chooses version of game
        ----
        place : in the beginning (1) or after rules (0)
        """
        if place == 1:
            print("The Game of Neutron\nStart new game!")
            self.print_b(board)
        print()
        if place == 1:
            print("If you want to read short rules, enter '1'")
        print(
            "To start game between 2 people, enter '2'\
            \nTo start light game with computer, enter '3'\
            \nTo start hard game with computer, enter '4'\
            \nTo start game between hard and light computers, enter '5'"
        )
        if place == 0:
            print("If you don't want to play, enter '0'")

    def rules_print(self):
        """
        Presents rules with new lines before and after
        """
        print(
            "RULES\
        \nWinning the game is simple.\
        \nJust maneuver the neutron onto your own back row."
        )
        print()
        print(
            "Every",
            "piece, even the neutron, moves in excactly the",
            "same way:\nalong a straight line horizontally,",
            "vertically, or diagonally.\nA piece stops moving",
            "just before it runs into another piece or the side",
            "wall.\nThere is no jumping or capturing. But there",
            "is one unusual feature.\nWhen a piece moves, it must",
            " go as far as possible in the direction chosen.",
        )
        print()

    def choose_correctly(self, place):
        """
        Checks input element - choice
        -Is number of input elements one?
        -Is input element digit?
        -Is an element 1 or 0, 2-5?
        ----
        place : in the beginning (1) or after rules (0)
        """
        quit = True
        while quit:
            # Check: is input number correct?
            start = input("Your choice: ")
            print()
            if len(start) == 1 and start.isdigit():
                # Check number of input elements
                # Check: is input element digit?
                start = int(start)
                if (start not in range(1, 6) and place == 1) or (
                    (start not in range(2, 6) and start != 0) and place == 0
                ):
                    print("Try again")

                else:
                    quit = False
                    break
            else:
                print("Try again")
        return start

    def game_two_people_light_2_3(
        self, version, white, black, neutron, black_won, white_won
    ):
        """
        Presents text interface for game's versions 2 or 3
        ----
        version : human - human (2) or human - light random computer (3)
        white   : white pawn
        black   : black pawn
        neutron : figure neutron
        black_won : text about black pawn's victory
        white_won : text about white pawn's victory
        """
        gen_version = 23
        board = Board()
        print("Player-1 - 🟡 | Player-2 - 🟣")
        print(board)
        while True:
            print()
            print("Player-1 🟡, move a piece:")
            board.human_makes_move(white)
            self.print_b(board)
            print()
            print("Player-2 🟣, move Neutron 🐹: ")
            if version == 2:
                if board.human_makes_move(neutron) is False:
                    self.print_b(board)
                    print(white_won)
                    break
            else:
                input("Computer's move - Press enter  ")
                if board.randomly_makes_move(neutron) is False:
                    self.print_b(board)
                    print(white_won)
                    break
            self.print_b(board)
            print()
            # After moving neutron
            if board.game_over(gen_version) is True:
                break
            print("Player-2 🟣, move a piece: ")
            if version == 2:
                board.human_makes_move(black)
            else:
                input("Computer's move - press enter  ")
                board.randomly_makes_move(black)
            self.print_b(board)
            print()
            print("Player-1 🟡, move Neutron 🐹: ")
            if board.human_makes_move(neutron) is False:
                self.print_b(board)
                print(black_won)
                break
            self.print_b(board)
            # After moving neutron
            if board.game_over(gen_version) is True:
                break
        print()

    def game_with_hard_computer_4_5(
        self, version, white, black, neutron, black_won, white_won
    ):
        """
        Presents text interface for game's versions 4 or 5
        ----
        version : hard computer - human(4) or hard computer - light computer(5)
        white   : white pawn
        black   : black pawn
        neutron : figure neutron
        black_won : text about black pawn's victory
        white_won : text about white pawn's victory
        """
        gen_version = 45
        board = Board()
        print("Player-1 - 🟣 | Player-2 - 🟡")
        self.print_b(board)
        while True:
            print()
            print("Player-1 🟣, move a piece:")
            input("Computer's move - Press enter  ")
            board.hard_computer_makes_move(black)
            self.print_b(board)
            print()
            print("Player-2 🟡, move Neutron 🐹: ")
            if version == 4:
                if board.human_makes_move(neutron) is False:
                    self.print_b(board)
                    print(black_won)
                    break
            else:
                input("Computer's move - Press enter  ")
                if board.randomly_makes_move(neutron) is False:
                    self.print_b(board)
                    print(black_won)
                    break
            self.print_b(board)
            # After moving neutron
            if board.game_over(gen_version) is True:
                break
            print("Player-2 🟡, move a piece: ")
            if version == 4:
                board.human_makes_move(white)
            else:
                input("Computer's move - press enter  ")
                board.randomly_makes_move(white)
            self.print_b(board)
            print()
            print("Player-1 🟣, move Neutron 🐹: ")
            input("Computer's move - Press enter  ")
            if board.hard_computer_makes_move(neutron) is False:
                self.print_b(board)
                print(white_won)
                break
            self.print_b(board)
            # After moving neutron
            if board.game_over(gen_version) is True:
                break

    def play_all_versions(self, version):
        """
        Presents different versions of the game
        """
        white_won = "Player-2 has fallen into a trap and cannot move Neutron\
                    \n🟣 Player-2 🟣 is Looser\
                    \n🟡 Player-1 🟡 is WINNER"
        black_won = "Player-1 has fallen into a trap and cannot move Neutron\
                    \n🟡 Player-1 🟡 is Looser\
                    \n🟣 Player-2 🟣 is WINNER"
        black_won_hard = "Player-2 has fallen into a trap and cannot move Neutron\
                    \n🟡 Player-2 🟡 is Looser\
                    \n🟣 Player-1 🟣 is WINNER"
        white_won_hard = "Player-1 has fallen into a trap and cannot move Neutron\
                    \n🟣 Player-1 🟣 is Looser\
                    \n🟡 Player-2 🟡 is WINNER"
        white = Figure.WHITE
        black = Figure.BLACK
        neutron = Figure.NEUTRON
        print()
        print("Write X and Y of pawn: two numbers from 1 to 5 with", "space")
        print()
        if version == 2 or version == 3:
            self.game_two_people_light_2_3(
                version, white, black, neutron, black_won, white_won
            )
        else:
            self.game_with_hard_computer_4_5(
                version, white, black, neutron, black_won_hard, white_won_hard
            )

    def start_rules_game(self):
        """
        Starts different versions of the game
        from the beginning with rules and to the end
        """
        board = Board()
        self.start_choice_print(board, 1)
        start = self.choose_correctly(1)
        if start == 1:
            self.rules_print()
            self.start_choice_print(board, 0)
            start = self.choose_correctly(0)
        if start == 2 or start == 3 or start == 4 or start == 5:
            # 2 if start the game between two people
            # 3 if start the game between human and light computer
            # 4 if start the game between hard computer and human
            # 5 if start the game between hard and light computers
            self.play_all_versions(start)
        elif start == 0:
            print("END")
