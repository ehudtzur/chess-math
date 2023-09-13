import picec_class as pi
lost_soldierList = []


class BOARD:

    def __init__(self):
        self._bord = [[pi.Rook(), pi.KNIGHT(), pi.Bishop(), pi.Queen(), pi.King(), pi.Bishop(), pi.KNIGHT(), pi.Rook()],
                      [pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier()],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b")],
                      [pi.Rook("b", "rook"), pi.KNIGHT("b"), pi.Bishop("b"), pi.Queen("b"), pi.King("b"), pi.Bishop("b"), pi.KNIGHT("b"), pi.Rook("b")]]
        self.lost_soldierList = []
        self.list_bord = []

    def get_color(self, x, y):
        if self._bord[x][y] != 0:
            return self._bord[x][y].color
        else:
            return 0

    def get_position(self, x, y):
        print(x, y)
        return self._bord[x][y]

    def eat_piece(self, x, y):
        piece_to_eat = self.get_position(x, y).kinde
        # print(piece_to_eat,88)
        # piece_to_eat = self.get_position(x, y).kinde, 1)
        self.lost_soldierList.append(piece_to_eat)
        # self.lost_soldierList = self.lost_soldierList.append(self.get_position(x, y))

        print(self.lost_soldierList, 11)

    def change_positione(self, oldx, oldy, newx, newy):
        self._bord[newx][newy] = self._bord[oldx][oldy]
        self._bord[oldx][oldy] = 0

    def chess_bord_print(self):
        self.list_bord = []
        for i in range(8):
            self.list_bord = []
            print("")
            for x in range(8):
                if self._bord[i][x] != 0:
                    uni = self._bord[i][x].get_unie()
                    self.list_bord.append(uni)
                else:
                    self.list_bord.append("_")
            for p in range(len(self.list_bord)):
                print(self.list_bord[p], end=" ")
    print("")

    def white_black_space(self, x, y):
        return self._bord[x][y].color

    def movment_on_the_bord(self, oldx, oldy, newx, newy):
        oldy = int(oldy)
        courent_soldier = self.get_position(oldx, oldy)
        allow_or_not_to_move = courent_soldier.movment(oldx, oldy, newx, newy)
        if allow_or_not_to_move:
            if courent_soldier.kinde == "soldier":
                if self.get_position(newx, newy) == 0:
                    self.change_positione(oldx, oldy, newx, newy)
                    return True
                else:
                    return False
            else:
                if self._bord[newx][newy] != 0:
                    if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                        self.eat_piece(newx, newy)
                else:
                    return False

        elif allow_or_not_to_move == 2:
            if self._bord[newx][newy] != 0:
                if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                    self.eat_piece(newx, newy)
            else:
                return False

        else:
            print(21)
            return False

    def interapt_on_the_bord(self, x, y):
        if self.get_color(x, y) == ("queen" or "rook" or "bishop"):
            print("L")
            return False
        else:
            print("W")
            return True

    def bishop_interapt(self, o_x, o_y, n_x, n_y):
        if abs(o_x-n_x) == 0:
            if o_y > n_y:
                for i in range(n_y, o_y-1):
                    if self.get_position(o_x, i+1) == 0:
                        continue
                    else:
                        return False

    def check_valid(self, cord):

        cord1 = cord[0]
        cord2 = cord[1]
        cord3 = cord[2]
        if len(cord) == 3 and (len(cord1) == 1) and (len(cord3) == 1) and cord2 == ",":
            if cord1.isnumeric() and cord3.isnumeric() and (-1 < int(cord1) < 8) and (-1 < int(cord3) < 8):
                return True
            else:
                print(" not leigale char")
                return False
        else:
            print(" not leigale char")
            return False


# def destin_Cordinat():
#
#     DastinationCordinats = input("enter Dastination Cordinats ")
#     check_dest_input = check_valid(DastinationCordinats)
#     if check_dest_input:
#         DastinationCordinats = DastinationCordinats.split(",")
#         return [int(DastinationCordinats[0]), int(DastinationCordinats[1])]
#     else:
#         answer = input("did ypu want to choos a just a new dest point ? y/o")
#         if answer == "y":
#             destin_Cordinat()
#         else:
#             pass
# chess_bord = BOARD()
# def chess_bord_print():
#     list_bord = []
#     for i in range(8):
#         list_bord = []
#         print("")
#         for x in range(8):
#             if chess_bord._bord[i][x] != 0:
#                 uni = chess_bord._bord[i][x].get_unie()
#                 list_bord.append(uni)
#             else:
#                 list_bord.append("_")
#         for p in range(len(list_bord)):
#             print(list_bord[p], end=" ")
