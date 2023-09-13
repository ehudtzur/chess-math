import game_class as gm

class Sioldier:


    def __init__(self, color="white", kinde="soldier", unicode="\u265F"):
        self.unie = unicode
        self.color = color
        self.kinde = kinde
        self.eml_index = 0

    def get_unie(self):
        return self.unie

    def movment(self, oldx, oldy, newx, newy):
        self.eml_index += 1
        absY = (oldy - newy)
        absX = (newx - oldx)
        if absX == 1 and absY == -1:
            print(8888888888888888889)
            return 2

        elif self.eml_index > 1:
            if absY == 0 and absX == 1:
                # if br.chess_bord._bord[newx][newy] == 0 or br.chess_bord._bord[newx][newy].color != self.color:
                return True
            else:
                return False
        else:
            absY = (oldy - newy)
            absX = (newx - oldx)
            if absY == 0 and ((absX == 1) or (absX == 2)):
                # if br.chess_bord._bord[newx][newy] == 0 or br.chess_bord._bord[newx][newy].color != self.color:
                return True
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
        self.eml_index += 1
        if absX == 1 and absY == 1:
            if gm.chess_game.chess_bord.get_color(newx, newy) != self.color:
                print(888888888888888888)
                return True
            else:
                print(111111111111111111111111111)
                return False
        if self.eml_index > 1:
            if absY == 0 and absX == -1:
                print(77777777777777777)
                return True
            else:
                print(00000000000000000000000)
                return False
        else:
            if absY == 0 and ((absX == -1) or (absX == -2)):
                print(24324324343242)
                return True

            else:
                print(55555555555555555555555555)
                return False


class KNIGHT(Sioldier):

    def __init__(self, color="white", kinde="knight", unicode="\u265e"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        absX = abs(oldx - newx)
        absY = abs(oldy - newy)
        if (absX or absY == 2) and (absX or absY == 1):
            # if gm.chase_bordFinal[newx][newy] == 0 or gm.chase_bordFinal[newx][newy].color != self.color:
            return True
        else:
            return False


class King(Sioldier):

    def __init__(self, color="white", kinde="king", unicode="\u265a"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        absX = abs(oldx - newx)
        absY = abs(oldy - newy)
        if (absX or absY == 0) and (absX or absY == 1):
            # if gm.chase_bordFinal[newx][newy] == 0 or gm.chase_bordFinal[newx][newy].color != self.color:
            return True
        else:
            return False


class Rook(Sioldier):

    def __init__(self, color="white", kinde="rook", unicode="\u265c"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        if oldx == newx or oldy == newy:
            # if gm.chase_bordFinal[newx][newy] == 0 or gm.chase_bordFinal[newx][newy].color != self.color:
            print("can move")
            return True
        else:
            print("cant move")
            return False


class Queen(Sioldier):

    def __init__(self, color="white", kinde="quine", unicode="\u265b"):
        Sioldier.__init__(self, color, kinde, unicode)

    def movment(self, oldx, oldy, newx, newy):
        absX = abs(oldx - newx)
        absY = abs(oldy - newy)
        if absX == absY or (oldx == newx or oldy == newy):
            # if gm.chase_bordFinal[newx][newy] == 0 or gm.chase_bordFinal[newx][newy].color != self.color:
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
            # if gm.chase_bordFinal[newx][newy] == 0 or gm.chase_bordFinal[newx][newy].color != self.color:
            return True
        else:
            return False
