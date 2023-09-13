import picec_class as pi

lost_soldierList = []

y = [[pi.Rook(), pi.KNIGHT(), pi.Bishop(), pi.Queen(), pi.King(), pi.Bishop(), pi.KNIGHT(), pi.Rook()],
    [pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier(), pi.Sioldier()],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b"), pi.BlackSoldier("b")],
    [pi.Rook("b", "rook"), pi.KNIGHT("b"), pi.Bishop("b"), pi.Queen("b"), pi.King("b"), pi.Bishop("b"), pi.KNIGHT("b"), pi.Rook("b")]]

class BOARD:

    def __init__(self):
        self._bord = [[pi.Rook(), pi.KNIGHT(), pi.Bishop(), pi.Queen(), pi.King(), pi.Bishop(), pi.KNIGHT(), pi.Rook()],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [pi.Rook("b", "rook"), pi.KNIGHT("b"), pi.Bishop("b"), pi.Queen("b"), pi.King("b"), pi.Bishop("b"), pi.KNIGHT("b"), pi.Rook("b")]]
        self.lost_soldierList = []
        self.list_bord = []
        self.target_location = []
        self.terrier_target_location = []
        self.chess_func_target = []
        self.white_object = pi.Sioldier()
        self.black_object = pi.BlackSoldier("b")
        self.temperri_white_saver = 0
        self.temperri_black_saver = 0


    def eat_threat(self,x,y):
        if self.get_position(x, y).color == "white":
            for i in range(8):
                for w in range(8):
                    if self.get_position(i, w) != 0 and self.get_position(i, w).color == "b":
                        res = self.movment_on_the_bord_for_king(i, w, x, y)
                        a= res
                        if not res:
                            return True
                        else:
                            return False
            return False
        else:
            for i in range(8):
                for w in range(8):
                    if self.get_position(i, w) != 0 and self.get_position(i, w).color == "white":
                        res = self.movment_on_the_bord_for_king(i, w, x, y)
                        if not res:
                            return True
                        else:
                            return False
            return False






    def castling(self,color):
        if color:
            res = input("which rook?  l for left r for right l/r")
            if self.get_position(0, 4).kinde == "king" and self.get_position(0, 4).eml_index == 0:
                if res == "l" :
                    if self.get_position(0, 0).kinde == "rook" and self.get_position(0, 0).eml_index == 0:
                        return True
                    else:
                        print("the rook all redy move")
                        return False
                else :
                    if self.get_position(0, 7).kinde == "rook" and self.get_position(0, 7).eml_index == 0:
                        return True
                    else:
                        print("the rook all redy move")
                        return False
            else:
                print("the king all redy move")
                return False
        else:
            res = input("which rook?  l for left r for right l/r")
            if self.get_position(7, 4).kinde == "king" and self.get_position(7, 4).eml_index == 0:
                if res == "l":
                    if self.get_position(7, 0).kinde == "rook" and self.get_position(7, 0).eml_index == 0:
                        return True
                    else:
                        print("the rook all redy move")
                        return False
                else:
                    if self.get_position(7, 7).kinde == "rook" and self.get_position(7, 7).eml_index == 0:
                        return True
                    else:
                        print("the rook all redy move")
                        return False
            else:
                print("the king all redy move")
                return False

    def get_color(self, x, y):
        if self._bord[x][y] != 0:
            return self._bord[x][y].color
        else:
            return 0

    def get_position(self, x, y):
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
                    self.list_bord.append("_\u202f\u202f")
            for p in range(len(self.list_bord)):
                print(self.list_bord[p], end=" ")
    print("")

    def white_black_space(self, x, y):
        if self.get_position(x, y) != 0:
            return self._bord[x][y].color
        else:
            print("nothing in this squer")
            return False


    def movment_on_the_bord(self, oldx, oldy, newx, newy):
        oldy = int(oldy)
        oldx = int(oldx)

        courent_soldier = self.get_position(oldx, oldy)
        allow_or_not_to_move = courent_soldier.movment(oldx, oldy, newx, newy)
        if allow_or_not_to_move == 1:
            if self.get_position(newx, newy) == 0:
                intarpt = self.interapt_on_the_bord(oldx, oldy, newx, newy)
                if intarpt:
                    self.change_positione(oldx, oldy, newx, newy)
                    res = self.exspose_the_king(newx, newy)
                    if res:
                        return True
                    else:
                        print("not legal move expose the king to cheese")
                        self.change_positione(newx, newy, oldx, oldy)
                else:
                    return False
            else:
                if courent_soldier.kinde == "soldier":
                    return False
                else:
                    if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                        intarpt = self.interapt_on_the_bord(oldx, oldy, newx, newy)
                        if intarpt:
                            self.change_positione(oldx, oldy, newx, newy)
                            print(44446565656565656656555555555555555555555555555)
                            # return True
                            res = self.exspose_the_king(newx, newy)
                            if res:
                                print(555880000)
                                # self.eat_piece(newx, newy)
                                return True
                            else:
                                print(787878787887878787)
                                print("not legal move expose the king to cheese")
                                self.change_positione(newx, newy, oldx, oldy)
                            self.eat_piece(newx, newy)
                            self.change_positione(oldx, oldy, newx, newy)
                            return True
                        else:
                            return False
        elif allow_or_not_to_move == 2:
            if self._bord[newx][newy] != 0:
                if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                    self.eat_piece(newx, newy)
                    self.change_positione(oldx, oldy, newx, newy)
                    return True
            else:
                return False

        else:
            if courent_soldier.eml_index == 1:
                courent_soldier.eml_index = 0
            print(21)
            return False

    def interapt_on_the_bord(self, x, y, n_x, n_y):
        self.terrier_target_location = []
        self.target_location = []
        if self.get_position(x, y).kinde == ("queen" or "rook" or "bishop"):
            if self.get_position(x, y).kinde == "queen":
                intarapt, location = self.queen_interapt(x, y, n_x, n_y)
                if intarapt:
                    print(location, 87654321987654321987654321)
                    self.target_location.append(location)
                    return True
                else:
                    return False

        else:
            if self.get_position(x, y).kinde == "rook":
                intarapt, location = self.rook_interapt(x, y, n_x, n_y)
                print(location)
                if intarapt:
                    self.target_location.append(location)
                    return True

                else:
                    return False, []
            elif self.get_position(x, y).kinde == "bishop":
                intarapt, location = self.bishop_interapt(x, y, n_x, n_y)
                self.target_location.append(location)
                print(location, 7654321987654321987654321)
                if intarapt:
                    self.target_location.append(location)
                    return True
                else:
                    return False
            print("W")
            return True

    def biger(self, x, y):
        bigger = max(x, y)
        lower = min(x, y)
        return bigger, lower

    def rook_interapt(self, o_x, o_y, n_x, n_y):
        location = []
        self.terrier_target_location = []
        self.target_location = []
        if abs(o_x-n_x) == 0:
            big, small = self.biger(o_y, n_y)
            for i in range(small + 1, big):
                location.append(self.get_position(o_x, i))
                self.terrier_target_location.append([o_x, i])
            print(location)
            if all(ele == 0 for ele in location):
                print(444)
                return True, self.terrier_target_location
            else:
                print(55550000055555)
                return False, []
        else:
            big, small = self.biger(o_x, n_x)
            for i in range(small+1, big):
                location.append(self.get_position(i, o_y))
                self.terrier_target_location.append([i, o_y])
            print(location)
            if all(ele == 0 for ele in location):
                print(444)
                return True, self.terrier_target_location
            else:
                print(55554444455555)
                return False, []

    def bishop_interapt(self, o_x, o_y, n_x, n_y):
        location = []
        self.terrier_target_location = []
        if ((o_x-n_x)/(o_y-n_y)) < 0:
            big, small = self.biger(o_y, n_y)
            big_x, small_x = self.biger(o_x, n_x)
            for i in range(small_x + 1, big_x):
                location.append(self.get_position(i, big-1))
                if (i < big_x and i > small_x):
                    self.terrier_target_location.append([i, big-1, 9999])
                big -= 1
            if all(ele == 0 for ele in location):
                print(444556677000000987675654356875565656565656565656565656565656565656565656565650)
                return True, self.terrier_target_location
            else:
                print(5555)
                return False, []
        else:
            big, small = self.biger(o_y, n_y)
            big_x, small_x = self.biger(o_x, n_x)
            for i in range(small_x + 1, big_x):
                location.append(self.get_position(i, small + 1))
                self.terrier_target_location.append([i, small + 1])
                small += 1
            if all(ele == 0 for ele in location):
                print(444556677)
                return True,  self.terrier_target_location
            else:
                print(5555)
                return False, []

    def queen_interapt(self, o_x, o_y, n_x, n_y):
        if o_x == n_x or o_y == n_y:
            res, location = self.rook_interapt(o_x, o_y, n_x, n_y)
            return res, location
        else:
            res, location = self.bishop_interapt(o_x, o_y, n_x, n_y)
            return res, location
            # big, small = self.biger(o_x, n_x)
            # for i in range(small+1, big):
            #     location.append(self.get_position(i, o_y))
            # if all(ele == 0 for ele in location):
            #     print(444)
            #     return True
            # else:
            #     print(5555)
            #     return False

    def check_valid(self, cord):

        cord1 = cord[0]
        cord2 = cord[1]
        cord3 = cord[2]
        if len(cord) == 3 and (len(cord1) == 1) and (len(cord3) == 1) and cord2 == ",":
            if cord1.isnumeric() and cord3.isnumeric() and (-1 < int(cord1) < 8) and (-1 < int(cord3) < 8):
                return True
            else:
                print(" not legal char")
                return False
        else:
            print(" not legal char")
            return False

    def exspose_the_king(self, x, y):
        trate_on_the_king_list = []
        if self.get_color(x, y) == "white":
            for i in range(8):
                for w in range(8):
                    if self.get_position(i, w) != 0:
                        if self._bord[i][w].color == "white":
                            if self.get_position(i, w).kinde == "king":
                                x_kingLOC, y_kingLOC = i, w
                                break

        else:
            if self.get_color(x, y) == "b":
                for i in range(8):
                    for w in range(8):
                        if self.get_color(i, w) == "b" and self.get_position(i, w).kinde == "king":
                            x_kingLOC, y_kingLOC = i, w
        for i in range(8):
            for w in range(8):
                if self.get_position(i, w) != 0:
                    if self.get_position(i, w).color != self.get_position(x, y).color:
                        res = self.movment_on_the_bord_for_king(i, w, x_kingLOC, y_kingLOC)
                        trate_on_the_king_list.append(res)
                # else:
                #     yield True
        if all(trate_on_the_king_list):
            return True
        else:
            return False

    def movment_on_the_bord_for_king(self, oldx, oldy, newx, newy):
        courent_soldier = self.get_position(oldx, oldy)
        allow_or_not_to_move = courent_soldier.movment(oldx, oldy, newx, newy)
        if allow_or_not_to_move == 1:
            if self.get_position(newx, newy) == 0:
                intarpt = self.interapt_on_the_bord(oldx, oldy, newx, newy)
                if intarpt:
                    return False
                else:
                    return True
            else:
                if courent_soldier.kinde == "soldier":
                    return True
                else:
                    if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                        intarpt = self.interapt_on_the_bord(oldx, oldy, newx, newy)
                        if intarpt:
                            return False
                        else:
                            return True
        elif allow_or_not_to_move == 2:
            if self._bord[newx][newy] != 0:
                if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                    return False
            else:
                return True

        else:
            return True

    def chess_check(self, x, y):
        self.terrier_target_location = []
        self.target_location = []
        trate_on_the_king_list = []
        if self.get_color(x, y) == "white":
            for i in range(8):
                for w in range(8):
                    if self.get_position(i, w) != 0:
                        if self._bord[i][w].color == "b":
                            if self.get_position(i, w).kinde == "king":
                                x_kingLOC, y_kingLOC = i, w
                                break

        else:
            if self.get_color(x, y) == "b":
                for i in range(8):
                    for w in range(8):
                        if self.get_color(i, w) == "white" and self.get_position(i, w).kinde == "king":
                            x_kingLOC, y_kingLOC = i, w
                            break
        for i in range(8):
            for w in range(8):
                if self.get_position(i, w) != 0:
                    if self.get_position(i, w).color == self.get_position(x, y).color:
                        res = self.movment_on_the_bord_for_king(i, w, x_kingLOC, y_kingLOC)
                        print(self.get_position(i, w))
                        print(res)
                        trate_on_the_king_list.append(res)
        if all(trate_on_the_king_list):
            return False, []
        else:
            return True, self.target_location
    # def mat_2_o(self, t, u):
    #     x, p = self.find_the_king(t, u)
    #     print(x, p, 77878787878787878787878)
    #     position_to_escape = []
    #     for i in range(-1, 2):
    #         for w in range(-1, 2):
    #             if (x + i > -1) and (x + i < 8) and (p + w > -1) and (p + w < 8) and (i != 0 or w != 0):
    #                 if self.get_position(x+i, p+w) != 0 and (x+i > -1) and (x+i < 8) and (p+w > -1) and (p+w < 8):
    #                     for l in range(8):
    #                         for o in range(8):
    #                             if self.get_position(l, o) != 0 and self.get_color(x, p) != self.get_color(l, o):
    #                                 if self.get_position(x+i, p+w) == 0:
    #                                     res = self.movment_on_the_bord_for_king(l, o, x+i, p+w)
    #                                     position_to_escape.append(res)
    #                                 else:
    #                                     if self.get_color(x+i, p+w) != self.get_color(l, o):
    #                                         res = self.movment_on_the_bord_for_king(l, o, x + i, p + w)
    #                                         position_to_escape.append(res)
    #                 else:
    #                     print(555555555555555555555555555555555555555555555577777777777777777777777777777)
    #     if all(position_to_escape):
    #         return True
    #     else:
    #         return False

    def mat(self, t, u):
        x, p = self.find_the_king(t, u)
        print(x, p, 77878787878787878787878)
        position_to_escape = []
        for i in range(-1, 2):
            for w in range(-1, 2):
                print(i)
                print(w, 2222)
                if (x + i > -1) and (x + i < 8) and (p + w > -1) and (p + w < 8) and (i != 0 or w != 0):
                    if self.get_position(x+i, p+w) != 0 and (x+i > -1) and (x+i < 8) and (p+w > -1) and (p+w < 8):
                        for l in range(8):
                            for o in range(8):
                                if self.get_position(l, o) != 0 and self.get_color(x, p) != self.get_color(l, o):
                                    if self.get_position(x+i, p+w) == 0:
                                        res = self.movment_on_the_bord_for_king(l, o, x+i, p+w)
                                        position_to_escape.append(res)
                                    else:
                                        if self.get_color(x+i, p+w) != self.get_color(x, p):
                                            if self.get_color(x+i, p+w) == "white":
                                                self.temperri_white_saver = self.get_position(x+i, p+w)
                                                self._bord[x+i][p+w] = self.black_object
                                                res = self.movment_on_the_bord_for_king(l, o, x + i, p + w)
                                                position_to_escape.append(res)
                                                self._bord[x + i][p + w] = self.temperri_white_saver
                                            else:
                                                self.temperri_black_saver = self.get_position(x + i, p + w)
                                                self._bord[x + i][p + w] = self.white_object
                                                res = self.movment_on_the_bord_for_king(l, o, x + i, p + w)
                                                position_to_escape.append(res)
                                                self._bord[x + i][p + w] = self.temperri_black_saver
                    else:
                        print(555555555555555555555555555555555555555555555577777777777777777777777777777)
        if all(position_to_escape):
            return True
        else:
            return False

    def find_the_king(self, x, y):
        if self.get_color(x, y) == "white":
            for i in range(8):
                for w in range(8):
                    if self.get_position(i, w) != 0:
                        if self._bord[i][w].color == "b":
                            if self.get_position(i, w).kinde == "king":
                                x_kingLOC, y_kingLOC = i, w
                                return x_kingLOC, y_kingLOC

        else:
            if self.get_color(x, y) == "b":
                for i in range(8):
                    for w in range(8):
                        if self.get_color(i, w) == "white" and self.get_position(i, w).kinde == "king":
                            x_kingLOC, y_kingLOC = i, w
                            return x_kingLOC, y_kingLOC

    def interapt_chess(self, list_target, player_color):
        way_list = []
        print(list_target, 99999999999999998888888888888888877777777777766666666)
        list_target = list_target[0]
        for i in range(len(list_target)):
            loc_1, loc_2 = list_target[i][0], list_target[i][1]
            print(loc_1, loc_2)
            for x in range(8):
                for y in range(8):
                    if self.get_position(x, y) != 0 and self.get_position(x, y).color != player_color and self.get_position(x, y).kinde != "king":
                        res = self.movment_on_the_bord_for_mat_cheak(x, y, loc_1, loc_2)
                        way_list.append(res)
        if any(way_list):
            return True
        else:
            return False

    def movment_on_the_bord_for_mat_cheak(self, oldx, oldy, newx, newy):

        print(oldx, oldy, newx, newy)
        courent_soldier = self.get_position(oldx, oldy)
        allow_or_not_to_move = courent_soldier.movment(oldx, oldy, newx, newy)
        if allow_or_not_to_move == 1:
            if self.get_position(newx, newy) == 0:
                intarpt = self.interapt_on_the_bord(oldx, oldy, newx, newy)
                if intarpt:
                    return True
                else:
                    return False
            else:
                if courent_soldier.kinde == "soldier":
                    return True
                else:
                    if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                        intarpt = self.interapt_on_the_bord(oldx, oldy, newx, newy)
                        if intarpt:
                            return True
                        else:
                            return False
        elif allow_or_not_to_move == 2:
            if self._bord[newx][newy] != 0:
                if self._bord[newx][newy].color != self.get_color(oldx, oldy):
                    return True
            else:
                return False

        else:
            return False

# def destin_Cordinat():

#     DastinationCordinats = input("enter Dastination Cordinats ")
#     check_dest_input = check_valid(DastinationCordinats)
#     if check_dest_input:
#         DastinationCordinats = DastinationCordinats.split(",")
#         return [int(DastinationCordinats[0]), int(DastinationCordinats[1])]
#     else:
#         answer = input("did ypu want to choose a just a new dest point ? y/o")
#         if answer == "y":
#             destin_Coordinate()
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
#                 uni = chess_bord._bord[i][x].get_uni()
#                 list_bord.append(uni)
#             else:
#                 list_bord.append("_")
#         for p in range(len(list_bord)):
#             print(list_bord[p], end=" ")
