from __future__ import annotations
import asyncio
import websockets
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

#from ss_player1.block_type_dict.create_block_dict import create_block_type_dict
from collections import defaultdict
import random
d = defaultdict(list)
d["A"] = [[1]]
d["B"] = [[1],[1]]
d["C"] = [[1],[1],[1]]
d["D"] = [[1, 0], [1, 1]]
d["E"] = [[1], [1], [1], [1]]
d["F"] = [[0, 1], [0, 1], [1, 1]]
d["G"] = [[1, 0], [1, 1], [1, 0]]
d["H"] = [[1, 1], [1, 1]]
d["I"] = [[1, 1, 0], [0, 1, 1]]
d["J"] = [[1], [1], [1], [1], [1]]
d["K"] = [[0, 1], [0, 1], [0, 1], [1, 1]]
d["L"] = [[0, 1], [0, 1], [1, 1], [1, 0]]
d["M"] = [[0, 1], [0, 1], [1, 1], [1, 0]]
d["S"] = [[1,0,0],[1,1,1],[0,0,1]]

def boad_str_to_list(board,pnum):
    my_stone = "o"
    opp_stone = "x"
    if pnum == 2:
        my_stone = "x"
        opp_stone = "o"
    s = board.splitlines()
    l = [3]*256
    for i in range(1,15):
        for j in range(0, 15):
            if s[i][j] == ".":
                l[i*16+j]=0
            elif s[i][j] == my_stone:
                l[i*16+j]=1
            elif s[i][j] == opp_stone:
                l[i*16+j]=2
    return l
def get_corner(l):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for i in range(15):
        for j in range(15):
            if l[(i<<4)+j] == 0:
                if (2<=i) and (i<=15):
                    if (2<=j) and(j<=15):
                        if l[((i - 1)<<4) + j - 1]==1:# -1. -1
                            l1.append((i,j))
                if (2<=i) and (i<=15):
                    if (1<=j) and(j<=14):
                        if l[((i - 1)<<4) + j + 1]==1:# -1. +1
                            l2.append((i,j))
                if (1<=i) and (i<=14):
                    if (2<=j) and(j<=15):
                        if l[((i + 1)<<4) + j - 1]==1:
                            l3.append((i,j))
                if (1<=i) and (i<=14):
                    if (1<=j) and(j<=14):
                        if l[((i + 1)<<4) + j + 1]==1:
                            l4.append((i,j))
    return l1,l2,l3,l4

def get_ans(l,block_list):
    l1,l2,l3,l4 = get_corner(l)
    for i,j in l1:
        random.shuffle(block_list)
        for block in block_list:
            if((i+len(d[block]))<=15)and((j+len(d[block]))<=15):
                cnt = 0
                y1 = 0
                x1 = 0
                for y in range(len(d[block])):
                    for x in range(len(d[block])):
                        if (d[block][y]==1)and(d[block][x]==1):
                            y1 = -y
                            x1 = -x
                for y in range(len(d[block])):
                    for x in range(len(d[block])):
                        cnt += l[((i+y+y1)<<4)+j+x+x1]
                        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                            if l[((i+y+y1+a)<<4)+j+x+b+x1]==1:
                                cnt+=1
                if cnt==0:#衝突判定
                    J = hex(j)[2:].upper()
                    I = hex(i)[2:].upper()
                    ret = block+'0'+J+I
                    return ret, block
    for i,j in l2:
        random.shuffle(block_list)
        for block in block_list:
            if((i+len(d[block]))<=15)and(1<=(j-len(d[block]))):
                cnt = 0
                y1 = 0
                x1 = 0
                for y in range(len(d[block])):
                    for x in range(len(d[block])):
                        if (d[block][y]==1)and(d[block][x]==1):
                            y1 = -y
                            x1 = +x
                for y in range(len(d[block])):
                    for x in range(len(d[block])):
                        cnt += l[((i+y+y1)<<4)+j+x+x1]
                        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                            if l[((i+y+y1+a)<<4)+j+x+b+x1]==1:
                                cnt+=1
                if cnt==0:#衝突判定
                    J = hex(j)[2:].upper()
                    I = hex(i)[2:].upper()
                    ret = block+'0'+J+I
                    return ret, block
    
    print("Nothing")
    return 'X000', 'AA'

def random_choice(board,pnum,bl):
    l = boad_str_to_list(board,pnum)
    ret = 'X000'
    use_block = 'AA'
    ret, use_block = get_ans(l,bl)
    return ret, use_block

class PlayerClient:
    def __init__(self, player_number: int, socket: websockets.WebSocketClientProtocol, loop: asyncio.AbstractEventLoop):
        self._loop = loop
        self._socket = socket
        self._player_number = player_number
        #self.p1Actions = ['U034', 'B037', 'J266', 'M149', 'O763', 'R0A3', 'F0C6', 'K113', 'T021', 'L5D2', 'G251', 'E291', 'D057', 'A053']
        #self.p2Actions = ['A0AA', 'B098', 'N0A5', 'L659', 'K33B', 'J027', 'E2B9', 'C267', 'U07C', 'M3AD', 'O2BB', 'R41C']
        self.p1turn = 0
        self.p2turn = 0
        self.block_list = ['A','B','C','D','E','F','G','S']


    @property
    def player_number(self) -> int:
        return self._player_number

    async def close(self):
        await self._socket.close()

    async def play(self):
        while True:
            board = await self._socket.recv()
            action = self.create_action(board)
            await self._socket.send(action)
            if action == 'X000':
                raise SystemExit

    def create_action(self, board):
        actions: list[str]
        s = board.splitlines()
        pnum = self.player_number
        ret = 'X000'
        if pnum==1 and self.p1turn==0:
            self.p1turn = 1
            ret = 'T055'
            
        elif pnum==2 and self.p2turn==0:
            self.p2turn = 1
            ret = 'T0AA'
        else:
            bl= self.block_list
            ret, block = random_choice(board,pnum,bl)
            if block in bl:
                self.block_list.remove(block)
        print("player_num",pnum)
        print("ret",ret)
        return ret
    
    @staticmethod
    async def create(url: str, loop: asyncio.AbstractEventLoop) -> PlayerClient:
        socket = await websockets.connect(url)
        print('PlayerClient: connected')
        player_number = await socket.recv()
        print(f'player_number: {player_number}')
        return PlayerClient(int(player_number), socket, loop)