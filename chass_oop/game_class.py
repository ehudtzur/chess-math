import bord_class as br


class ChessGame:

    def __init__(self):
        self.blackCounter = 0
        self.whiteCounter = 0
        self.chess_bord = br.BOARD()

    def destin_cordinat(self):

        DastinationCordinats = input("enter Dastination Cordinats ")
        check_dest_input = chess_game.chess_bord.check_valid(DastinationCordinats)
        if check_dest_input:
            return DastinationCordinats.split(",")
        else:
            self.begine_or_change()

    def begine_or_change(self):
        answer = input("did ypu want to choos  just a new dest point ? y/o")
        if answer == "n":
            self.player_tourn()
        else:
            self.destin_cordinat()

    def valid_exit_point_by_turn_and_position(self, oldx, oldy):

        # global choose_a_game_tool
        # global choose_coordinates
        flag = True
        if self.whiteCounter == self.blackCounter:
            pione = self.chess_bord.white_black_space(oldx, oldy)
            while flag:
                if pione != 0:
                    if self.chess_bord.get_color(oldx, oldy) == "b":
                        choose_coordinates = input("enter exit coordinates again  remember its the white tourn")
                        choose_coordinates = choose_coordinates.split(",")
                        oldx = choose_coordinates[0]
                        oldy = choose_coordinates[1]
                        # pione = self.chess_bord._bord[int(oldx)][int(oldy)]

                        pione = self.chess_bord.get_position(int(oldx), int(oldy))
                        if pione.color == "white":
                            flag = False
                            return choose_coordinates

                    else:
                        flag = False
                    choose_coordinates = [oldx, oldy]
                    return choose_coordinates
                else:
                    print("enter a legale posietion in this position dont have any pione")
                    self.player_tourn()
        else:
            pione = self.chess_bord.white_black_space(oldx, oldy)
            while flag:
                if pione != 0:
                    if self.chess_bord.get_color(oldx, oldy) == "white":
                        choose_coordinates = input("enter coordinates")
                        choose_coordinates = choose_coordinates.split(",")
                        oldx = choose_coordinates[0]
                        oldy = choose_coordinates[1]
                        # pione = self.chess_bord._bord[int(oldx)][int(oldy)]
                        if self.chess_bord.get_color(int(oldx), int(oldy)) == "b":
                            flag = False
                            return choose_coordinates

                    else:
                        flag = False
                    # self.blackCounter += 1
                    choose_coordinates = [oldx, oldy]
                    return choose_coordinates
                else:
                    print("enter a legale posietion in this position dont have any pione")
                    self.player_tourn()

    def player_tourn(self):
        # br.check_valid(choose_coordinates)
        choose_coordinates = input("enter exit again coordinates")
        chack_position = chess_game.chess_bord.check_valid(choose_coordinates)
        if chack_position:
            chack_position = choose_coordinates.split(",")
        else:
            self.player_tourn()
        # choose_coordinates = chess_game.valid_exit_point_by_turn_and_position(self.chess_bord, int(chack_position[0]), int(chack_position[1]))

        choose_coordinates = chess_game.valid_exit_point_by_turn_and_position(int(chack_position[0]), int(chack_position[1]))
        X, Y = choose_coordinates[0], choose_coordinates[1]
        potision = chess_game.destin_cordinat()
        destX = int(potision[0])
        desty = int(potision[1])
        res = self.chess_bord.movment_on_the_bord(X, Y, destX, desty)
        if res:
            if self.whiteCounter == self.blackCounter:
                self.whiteCounter += 1
            else:
                self.blackCounter += 1
        else:
            self.player_tourn()


if __name__ == "__main__":
    chess_game = ChessGame()
    while "king" not in chess_game.chess_bord.lost_soldierList:
        print(chess_game.whiteCounter, chess_game.blackCounter, "white and black counters")
        print(chess_game.chess_bord.chess_bord_print())
        chess_game.player_tourn()
    print("finis")

