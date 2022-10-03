#coding: UTF-8
'''
Created on 2020/01/10

@author: Akira
'''

import tkinter as tk
import tkinter.font as tkFont
import random
import pathlib
import sys
import os


class block1():

    co = [[0, 0], [0, 0], [0, 0], [0, 0]]
    color = ""
    pattern = ""

    def __init__(self, x=4, y=-3):
        self.pattern = 1
        self.color = "deep sky blue"
        self.co[0] = [x, y]
        # co[0][0]が基本のx、co[0][1]が基本のyになる
        self.co[1] = [self.co[0][0], self.co[0][1] - 2]
        self.co[2] = [self.co[0][0], self.co[0][1] - 1]
        self.co[3] = [self.co[0][0], self.co[0][1] + 1]

    def auto(self):
        for i in range(0, 4):
            self.co[i][1] += 1

    def right(self):
        for i in range(0, 4):
            self.co[i][0] += 1

    def left(self):
        for i in range(0, 4):
            self.co[i][0] -= 1

    def roundRight(self):
        for i in range(1, 4):
            self.co[i] = [self.co[0][0] + (-1) * (self.co[i][1] - self.co[0][1]),
                          self.co[0][1] + (self.co[i][0] - self.co[0][0])]

    def roundLeft(self):
        for i in range(1, 4):
            self.co[i] = [self.co[0][0] + (self.co[i][1] - self.co[0][1]),
                          self.co[0][1] + (-1) * (self.co[i][0] - self.co[0][0])]

#　以下、is-a の関係にないことを重々承知の上で継承します。blockクラスとblock1クラスをわけることに有意義さを感じなかったため。


class block2(block1):
    def __init__(self, x=5, y=-2):
        self.pattern = 2
        self.color = "red"
        self.co[0] = [x, y]
        self.co[1] = [self.co[0][0] + 1, self.co[0][1] + 1]
        self.co[2] = [self.co[0][0], self.co[0][1] - 1]
        self.co[3] = [self.co[0][0], self.co[0][1] + 1]


class block3(block1):
    def __init__(self, x=5, y=-2):
        self.pattern = 3
        self.color = "medium spring green"
        self.co[0] = [x, y]
        self.co[1] = [self.co[0][0] + 1, self.co[0][1]]
        self.co[2] = [self.co[0][0] + 1, self.co[0][1] + 1]
        self.co[3] = [self.co[0][0], self.co[0][1] + 1]


class block4(block1):
    def __init__(self, x=5, y=-2):
        self.pattern = 4
        self.color = "gold"
        self.co[0] = [x, y]
        self.co[1] = [self.co[0][0] + 1, self.co[0][1]]
        self.co[2] = [self.co[0][0], self.co[0][1] - 1]
        self.co[3] = [self.co[0][0], self.co[0][1] + 1]


class block5(block1):
    def __init__(self, x=5, y=-2):
        self.pattern = 5
        self.color = "orange"
        self.co[0] = [x, y]
        self.co[1] = [self.co[0][0] + 1, self.co[0][1]]
        self.co[2] = [self.co[0][0], self.co[0][1] - 1]
        self.co[3] = [self.co[0][0] + 1, self.co[0][1] + 1]


class block6(block1):
    def __init__(self, x=5, y=-2):
        self.pattern = 6
        self.color = "hot pink"
        self.co[0] = [x, y]
        self.co[1] = [self.co[0][0] + 1, self.co[0][1]]
        self.co[2] = [self.co[0][0] + 1, self.co[0][1] - 1]
        self.co[3] = [self.co[0][0], self.co[0][1] + 1]


class block7(block1):
    def __init__(self, x=5, y=-2):
        self.pattern = 7
        self.color = "blue violet"
        self.co[0] = [x, y]
        self.co[1] = [self.co[0][0] - 1, self.co[0][1] + 1]
        self.co[2] = [self.co[0][0], self.co[0][1] - 1]
        self.co[3] = [self.co[0][0], self.co[0][1] + 1]


class view():

    def __init__(self):
        # キャンバスの生成
        self.root = tk.Tk()
        self.root.title("INKYANOHONKI TETRIS")
        self.root.geometry("500x600")
        self.root.resizable(0, 0)
        self.canvas = tk.Canvas(self.root, width=500, height=600, bg="white")
        filename = str(__file__)
        while filename[len(filename) - 1] != '/':
            filename = filename[:-1]
        self.GAMEOVER = tk.PhotoImage(file=pathlib.Path(filename + "/iGM.png"))
        # マス目をつくっていく！
        self.CV_COLOR = "black"
        for y in range(0, 20):
            for x in range(0, 10):
                self.canvas.create_rectangle(
                    30*x, 30*y, 30*x+30, 30*y+30, fill=self.CV_COLOR, outline="white", tag="x"+str(x)+"y"+str(y))
        self.minus = [
            [self.CV_COLOR for i in range(0, 10)] for j in range(0, 10)]
        self.blockLot = []
        self.canvas.pack()
        # キー操作の表示
        self.howtotext = " RIGHT: → or d Key \nLEFT: ← or a Key\nROUNDRIGHT: ↑ or s Key\nROUNDLEFT: e Key\nDOWN: ↓ or s Key\n\n EXIT: shift+c key"
        self.howto = tk.Label(self.root, text=self.howtotext, font=tkFont.Font(
            family="Consolas", size=11)).place(x=310, y=300)
        # 得点表示板
        self.scoreNumber = 0
        self.text = tk.StringVar()
        self.text.set("SCORE:" + str(self.scoreNumber))
        self.score = tk.Label(self.root, textvariable=self.text, font=tkFont.Font(
            family="Consolas", size=25), bg="white")
        self.score.place(x=310, y=5)
        # ブロックの生成、時間によって動かす
        self.loopingcreating()
        self.root.mainloop()

    def scoreupdate(self, a=10):
        # スコアを更新するための関数
        self.scoreNumber += a
        self.text.set("SCORE:" + str(self.scoreNumber))

    def loopingcreating(self):
        # ブロックの選択と生成をする関数

        if len(self.blockLot) == 0:
            self.blockLot = [1, 2, 3, 4, 5, 6, 7]
        y = random.randrange(0, len(self.blockLot))
        x = self.blockLot[y]
        if x == 1:
            self.block = block1()
        if x == 2:
            self.block = block2()
        if x == 3:
            self.block = block3()
        if x == 4:
            self.block = block4()
        if x == 5:
            self.block = block5()
        if x == 6:
            self.block = block6()
        if x == 7:
            self.block = block7()
        self.blockLot.remove(x)
        self.looping()

    def looping(self):
        # ブロックが走っている間のふるまいをあらわす関数
        self.state = 0
        # lambdaを使ったのはきまぐれと練習です
        self.root.bind("<Key-d>", lambda event: self.right(event))
        self.root.bind("<Key-Right>", lambda event: self.right(event))
        self.root.bind("<Key-a>", lambda event: self.left(event))
        self.root.bind("<Key-w>", lambda event: self.roundRight(event))
        self.root.bind("<Key-Left>", lambda event: self.left(event))
        self.root.bind("<Key-Up>", lambda event: self.roundRight(event))
        self.root.bind("<Key-e>", lambda event: self.roundLeft(event))
        self.root.bind("<Key-s>", lambda event: self.down(event))
        self.root.bind("<Key-Down>", lambda event: self.down(event))
        self.root.bind("<Key-C>", lambda event: sys.exit(0))
        self.update()

    def update(self):
        # ブロックの生成条件、ゲームの継続条件を調べる関数

        self.fall(0)
        # 底じゃないか、次にブロックがなければ前に進み続ける
        # 前に進み続けるか？
        if self.judge("fall"):
            self.scoreupdate(3)
            self.root.after(750, self.update)
        # ブロックを生成するか？
        else:
            # 行が全部埋まってなければまたブロックを生成する
            for i in self.block.co:
                if any(self.canvas.itemcget("x"+str(i)+"y0", "fill") != self.CV_COLOR for i in range(0, 10)):
                    w = tk.Label(self.root, image=self.GAMEOVER).place(
                        x=60, y=190)
                    x = tk.Label(self.root, text="YOUR SCORE:" + str(self.scoreNumber),
                                 font=tkFont.Font(family="Consolas", size=20)).place(x=130, y=350)
                    x = tk.Label(self.root, text="RESTART: push y key \n EXIT: push shift+c key",
                                 font=tkFont.Font(family="Consolas", size=15)).place(x=120, y=390)
                    self.root.bind(
                        "<Key-y>", lambda event: os.execl(sys.executable, sys.executable, *sys.argv))
                    return 0
            for i in self.block.co:
                if i[1] < 0:
                    self.minus[9 - (-1) * i[1]][i[0]] = self.block.color
            self.deleting()
            return self.loopingcreating()

    def deleting(self, a=1):
        # ブロックが一列そろったときにその列を消す関数
        newcanvas = [[self.CV_COLOR for i in range(
            0, 10)] for j in range(0, 30)]
        # newcanvasにマイナスのブロックの情報を貼り付ける
        for i in range(0, 10):
            newcanvas[i] = self.minus[i]
        # newcanvasにブロックの情報を貼り付ける
        for i in range(10, 30):
            for j in range(0, 10):
                newcanvas[i][j] = self.canvas.itemcget(
                    "x" + str(j) + "y" + str(i - 10), "fill")
        deletingnow = True
        while deletingnow:
            newcanvasalpha = [[0 for i in range(0, 10)] for i in range(0, 30)]
            for i in range(0, 30):
                for j in range(0, 10):
                    newcanvasalpha[i][j] = newcanvas[i][j]
            for i in range(29, 0, -1):
                deleteable = True
                for j in range(0, 10):
                    if newcanvas[i][j] == (self.CV_COLOR or "green"):
                        deleteable = False
                if deleteable:
                    for k in range(i, 0, -1):
                        newcanvas[k] = newcanvas[k - 1]
            if newcanvas == newcanvasalpha:
                return 0
            for i in range(10, 30):
                for j in range(0, 10):
                    if i - 10 >= 0:
                        self.canvas.itemconfigure(
                            "x" + str(j) + "y" + str(i - 10), fill=newcanvas[i][j])
            self.scoreupdate(a * 100)
            self.deleting(a+1)

    def judge(self, direction):
        # それぞれのキー操作に対して、その操作が可能であるかを見定めるための関数
        if direction == "right":
            rights = []
            for i in self.block.co:
                rights.append(i)
                for j in rights:
                    if rights.index(j) != len(rights) - 1 and j[1] == rights[-1][1]:
                        MIN = min(j[0], rights[-1][0])
                        rights.remove([MIN, j[1]])
            rightable = all((i[1] + 11 > 0 and i[1] < 29 and self.canvas.itemcget(
                "x" + str(i[0] + 1) + "y" + str(i[1]), "fill") == self.CV_COLOR) for i in rights)
            return rightable

        if direction == "left":
            # なぜか変数名をleftにすると挙動が悪くなるので、あえてrightsのままにする
            rights = []
            for i in self.block.co:
                rights.append(i)
                for j in rights:
                    if rights.index(j) != len(rights) - 1 and j[1] == rights[-1][1]:
                        MIN = max(j[0], rights[-1][0])
                        rights.remove([MIN, j[1]])
            rightable = all((i[1] + 11 > 0 and i[1] < 29 and self.canvas.itemcget(
                "x" + str(i[0] - 1) + "y" + str(i[1]), "fill") == self.CV_COLOR) for i in rights)
            return rightable

        if direction == "roundRight":
            judge = [[self.block.co[i][0], self.block.co[i][1]]
                     for i in range(0, 4)]
            for i in range(1, 4):
                judge[i] = [judge[0][0] + (-1) * (judge[i][1] - judge[0][1]),
                            judge[0][1] + (judge[i][0] - judge[0][0])]
            roundRightable = True
            for i in range(1, 4):
                if judge[i][0] >= 0 and judge[i][1] >= 0 and judge[i] not in self.block.co:
                    if self.canvas.itemcget("x"+str(judge[i][0])+"y"+str(judge[i][1]), "fill") != self.CV_COLOR:
                        roundRightable = False
            if all(0 <= i[0] < 10 for i in judge) == False:
                roundRightable = False
            return roundRightable

        if direction == "roundLeft":
            judge = [[self.block.co[i][0], self.block.co[i][1]]
                     for i in range(0, 4)]
            for i in range(1, 4):
                judge[i] = [judge[0][0] + (judge[i][1] - judge[0][1]),
                            judge[0][1] + (-1) * (judge[i][0] - judge[0][0])]
            roundLeftable = True
            for i in range(1, 4):
                if judge[i][0] >= 0 and judge[i][1] >= 0 and judge[i] not in self.block.co:
                    if self.canvas.itemcget("x"+str(judge[i][0])+"y"+str(judge[i][1]), "fill") != self.CV_COLOR:
                        roundLeftable = False
            if all(0 <= i[0] < 10 for i in judge) == False:
                roundLeftable = False
            return roundLeftable

        if direction == "down":
            bottoms = []
            for i in self.block.co:
                """if all(i[0])"""
                bottoms.append(i)
                for j in bottoms:
                    if bottoms.index(j) != len(bottoms) - 1 and j[0] == bottoms[-1][0]:
                        MIN = min(j[1], bottoms[-1][1])
                        bottoms.remove([j[0], MIN])
            downAble = all((i[1] + 11 > 0 and i[1] < 29 and self.canvas.itemcget("x" + str(
                i[0]) + "y" + str(i[1] + 1), "fill") == self.CV_COLOR) for i in bottoms)
            return downAble

        if direction == "fall":
            bottoms = []
            for i in self.block.co:
                """if all(i[0])"""
                if i[1] >= 0:
                    bottoms.append(i)
                for j in bottoms:
                    if bottoms.index(j) != len(bottoms) - 1 and j[0] == bottoms[-1][0]:
                        MIN = min(j[1], bottoms[-1][1])
                        bottoms.remove([j[0], MIN])
            downAble = all((i[1] < 29 and self.canvas.itemcget(
                "x" + str(i[0]) + "y" + str(i[1] + 1), "fill") == self.CV_COLOR) for i in bottoms)
            return downAble

    def right(self, event):
        # 実際に右に進ませる関数
        if self.state == 0:
            self.state = 1
            if self.judge("right"):
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.CV_COLOR)
                self.block.right()
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.block.color)
            self.state = 0
            return 0
        else:
            return 0

    def left(self, event):
        if self.state == 0:
            self.state = 1
            if self.judge("left"):
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.CV_COLOR)
                self.block.left()
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.block.color)
            self.state = 0
            return 0
        else:
            return 0

    def roundRight(self, event):
        if self.state == 0:
            self.state = 1
            if self.judge("roundRight"):
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.CV_COLOR)
                self.block.roundRight()
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.block.color)
            self.state = 0
            return 0
        else:
            return 0

    def roundLeft(self, event):
        if self.state == 0:
            self.state = 1
            if self.judge("roundLeft"):
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.CV_COLOR)
                self.block.roundLeft()
                for i in self.block.co:
                    self.canvas.itemconfigure(
                        "x"+str(i[0])+"y"+str(i[1]), fill=self.block.color)
            self.state = 0
            return 0
        else:
            return 0

    def down(self, event):
        if self.judge("down"):
            for i in self.block.co:
                self.canvas.itemconfigure(
                    "x"+str(i[0])+"y"+str(i[1]), fill=self.CV_COLOR)
            self.block.auto()
            for i in self.block.co:
                self.canvas.itemconfigure(
                    "x"+str(i[0])+"y"+str(i[1]), fill=self.block.color)
        self.state = 0
        return 0

    def fall(self, event):
        if self.judge("fall"):
            for i in self.block.co:
                self.canvas.itemconfigure(
                    "x"+str(i[0])+"y"+str(i[1]), fill=self.CV_COLOR)
            self.block.auto()
            for i in self.block.co:
                self.canvas.itemconfigure(
                    "x"+str(i[0])+"y"+str(i[1]), fill=self.block.color)
        return 0


app = view()
