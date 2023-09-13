class Sioldier:
    # "\033[1;32;40m\u265F"
    def __init__(self, color="white", kinde="soldier", unicode="\u265F"):


        self.unie = unicode
        self.color = color
        self.kinde = kinde
        self.eml_index = 0

    def upadate_index(self):
        self.eml_index += 1

    def get_unie(self):
        return self.unie

    def movment(self, oldx, oldy, newx, newy):
        # self.eml_index += 1
        absY = (oldy - newy)
        absX = (newx - oldx)
        if absX == 1 and abs(absY) == 1:
            # print((newx - oldx), (oldy - newy), 3434443)
            return 2
        if self.eml_index >= 1:
            if absY == 0 and absX == 1:
                return 1
            else:
                return False
        else:
            if absY == 0 and ((absX == 1) or (absX == 2)):
                return 1
            else:
                return False

    # def movment_on_the_bord(self, oldx: int, oldy: int, newx, newy):
    #     global whiteCounter, blackCounter
    #     oldy = int(oldy)
    #     allow_ro_not_to_move = self.movment(oldx, oldy, newx, newy)
    #     if allow_ro_not_to_move:
    #         if br.chess_bord._bord[newx][newy] != 0:
    #             if br.chess_bord._bord[newx][newy].color != self.color:
    #                 # gm.lostsoldierList.append(br.chess_bord._bord[newx][newy].kinde)
    #                 print(5555555)
    #         br.chess_bord._bord[newx][newy] = br.chess_bord._bord[oldx][oldy]
    #         br.chess_bord._bord[oldx][oldy] = 0
    #         print(1)
    #         return True
    #     else:
    #         if whiteCounter > blackCounter:
    #             whiteCounter -= 1
    #         else:
    #             print('the move is not valid!')
    #             blackCounter -= 1
    #         # gm.player_tourn()


class BlackSoldier(Sioldier):
    # import game_class as gm

    def __init__(self, color="b", kinde="soldier", unicode="\u2659"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        absY = (oldy - newy)
        absX = (newx - oldx)
        # self.eml_index += 1
        if absX == -1 and abs(absY) == 1:
            # print((newx - oldx), (oldy - newy), 3434443)
            return 2
        elif self.eml_index >= 1:
            if absY == 0 and absX == -1:
                return 1
            else:
                return False
        else:
            if absY == 0 and ((absX == -1) or (absX == -2)):
                return 1
            else:
                return False


class KNIGHT(Sioldier):

    def __init__(self, color="white", kinde="knight", unicode="\u265e"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        absX = abs(oldx - newx)
        absY = abs(oldy - newy)
        if (absX == 2 or absY == 2) and (absX == 1 or absY == 1):
            return True
        else:
            return False


class King(Sioldier):

    def __init__(self, color="white", kinde="king", unicode="\u265a"):
        Sioldier.__init__(self, color, kinde, unicode)
        self.eml_index = 0

    def upadate_index(self):
        self.eml_index += 1
    def movment(self, oldx, oldy, newx, newy):
        absX = abs(oldx - newx)
        absY = abs(oldy - newy)
        if ((absX == 0 or absY == 0) and (absX == 1 or absY == 1)) or (absY == 1 and absX == 1):
            # if gm.chase_bordFinal[newx][newy] == 0 or gm.chase_bordFinal[newx][newy].color != self.color:
            return True
        else:
            return False


class Rook(Sioldier):

    def __init__(self, color="white", kinde="rook", unicode="\u265c"):
        Sioldier.__init__(self, color, kinde, unicode)
        self.eml_index = 0

    def upadate_index(self):
        self.eml_index += 1

    def movment(self, oldx, oldy, newx, newy):
        if oldx == newx or oldy == newy:
            print("can move")
            return True
        else:
            print("cant move")
            return False


class Queen(Sioldier):

    def __init__(self, color="white", kinde="queen", unicode="\u265b"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        absX = abs(oldx - newx)
        absY = abs(oldy - newy)
        if absX == absY or (oldx == newx or oldy == newy):
            return True
        else:
            return False


class Bishop(Sioldier):

    def __init__(self, color="white", kinde="bishop", unicode="\u265d"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        absX = abs(oldx - newx)
        absY = abs(oldy - newy)
        if absX == absY:
            return True
        else:
            return False
