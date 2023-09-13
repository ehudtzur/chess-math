
import bord_class as br


class ChessGame:

    def __init__(self):
        self.blackCounter = 0
        self.whiteCounter = 0
        self.lost_soldierList = []

    def destin_cordinat(self):

        DastinationCordinats = input("enter Dastination Cordinats ")
        check_dest_input = br.check_valid(DastinationCordinats)
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
            pione = chess_bord._bord[oldx][oldy]
            while flag:
                if pione != 0:
                    if pione.color == "b":
                        choose_coordinates = input("enter coordinates")
                        choose_coordinates = choose_coordinates.split(",")
                        oldx = choose_coordinates[0]
                        oldy = choose_coordinates[1]
                        pione = chess_bord._bord[int(oldx)][int(oldy)]
                        if pione.color == "white":
                            flag = False
                            return choose_coordinates

                    else:
                        flag = False
                    self.whiteCounter += 1
                    choose_coordinates = [oldx, oldy]
                    return choose_coordinates
                else:
                    print("enter a legale posietion in this position dont have any pione")
                    self.player_tourn()
        else:
            pione = chess_bord._bord[oldx][oldy]
            while flag:
                if pione != 0:
                    if pione.color == "white":
                        choose_coordinates = input("enter coordinates")
                        choose_coordinates = choose_coordinates.split(",")
                        oldx = choose_coordinates[0]
                        oldy = choose_coordinates[1]
                        pione = chess_bord._bord[int(oldx)][int(oldy)]
                        if pione.color == "b":
                            flag = False
                            return choose_coordinates

                    else:
                        flag = False
                    self.blackCounter += 1
                    choose_coordinates = [oldx, oldy]
                    return choose_coordinates
                else:
                    print("enter a legale posietion in this position dont have any pione")
                    self.player_tourn()

    def player_tourn(self):

        choose_coordinates = input("enter exit again coordinates")
        chack_position = br.check_valid(choose_coordinates)
        if chack_position:
            chack_position = choose_coordinates.split(",")
        else:
            self.player_tourn()
        choose_coordinates = chess_game.valid_exit_point_by_turn_and_position(int(chack_position[0]), int(chack_position[1]))

        X, Y = choose_coordinates[0], choose_coordinates[1]
        current_square = chess_bord._bord[X][Y]
        # print(current_square,76)
        potision = chess_game.destin_cordinat()
        # print(potision)
        destX = int(potision[0])
        desty = int(potision[1])
        curent_soldier = chess_bord._bord[X][Y]
        # print(curent_soldier, 9999)
        # destX, desty = int(potision[0]), int(potision[1])
        print(chess_bord.movment_on_the_bord(X, Y, destX, desty))
        # cordinats = br.destin_Cordinat()

        # print(curent_soldier.movment_on_the_bord(X, Y, destX, desty))
        # print(type(curent_soldier))
        # print(chase_bordFinal[2][0], 22)


chess_game = ChessGame()
chess_bord = br.BOARD()

while "king" not in chess_game.lost_soldierList:
    print(chess_game.whiteCounter, chess_game.blackCounter)
    print(chess_bord.chess_bord_print())
    chess_game.player_tourn()
