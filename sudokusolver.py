#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sudokusolver.py

import sys
import copy

class Cell(object):
    def __init__(self, row, col, quad, possibles, answer):
        self.row = row
        self.col = col
        self.quad = quad
        self.possibles = possibles
        self.answer = answer
    
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value
    
    def decide_answer(self):
        if self.answer != 0 and len(self.possibles) > 1:
            self.possibles = []
        if len(self.possibles) == 1:
            self.answer = self.possibles[0]
    
    def eliminate_possibiles(self):
        for item in self.possibles:
            for j in range(len(board)):
                if (board[j].row == self.row and
                board[j].col == self.col):
                    pass
                elif (board[j].row == self.row or
                board[j].col == self.col or
                board[j].quad == self.quad):
                    if board[j].answer == item:
                        try:
                            self.possibles.remove(item)
                        except ValueError:
                            pass

board = []
quad_dict = {(0,0): 0, (0,1): 0, (0,2): 0,
            (1,0): 0, (1,1): 0, (1,2): 0,
            (2,0): 0, (2,1): 0, (2,2): 0,
            (0,3): 1, (0,4): 1, (0,5): 1,
            (1,3): 1, (1,4): 1, (1,5): 1,
            (2,3): 1, (2,4): 1, (2,5): 1,
            (0,6): 2, (0,7): 2, (0,8): 2,
            (1,6): 2, (1,7): 2, (1,8): 2,
            (2,6): 2, (2,7): 2, (2,8): 2,
            (3,0): 3, (3,1): 3, (3,2): 3,
            (4,0): 3, (4,1): 3, (4,2): 3,
            (5,0): 3, (5,1): 3, (5,2): 3,
            (3,3): 4, (3,4): 4, (3,5): 4,
            (4,3): 4, (4,4): 4, (4,5): 4,
            (5,3): 4, (5,4): 4, (5,5): 4,
            (3,6): 5, (3,7): 5, (3,8): 5,
            (4,6): 5, (4,7): 5, (4,8): 5,
            (5,6): 5, (5,7): 5, (5,8): 5,
            (6,0): 6, (6,1): 6, (6,2): 6,
            (7,0): 6, (7,1): 6, (7,2): 6,
            (8,0): 6, (8,1): 6, (8,2): 6,
            (6,3): 7, (6,4): 7, (6,5): 7,
            (7,3): 7, (7,4): 7, (7,5): 7,
            (8,3): 7, (8,4): 7, (8,5): 7,
            (6,6): 8, (6,7): 8, (6,8): 8,
            (7,6): 8, (7,7): 8, (7,8): 8,
            (8,6): 8, (8,7): 8, (8,8): 8}
            
with open(sys.argv[1]) as f:
    a = []
    for line in f:
        a.append(list(line.strip()))
    for i in range(9):
        for j in range(9):
            board.append(Cell(i,j,quad_dict[i,j],
            ([1,2,3,4,5,6,7,8,9]if int(a[i][j]) == 0 else []),
            int(a[i][j])))

changed = True
while changed == True:
    changed = False
    oldboard = copy.deepcopy(board)
    for each_cell in board:
        each_cell.eliminate_possibiles()
        each_cell.decide_answer()
    if False in [dict(board[i]) == dict(oldboard[i]) for i in range(len(board))]:
        changed = True
        
for i in range(9):
    for j in range(9):
        print board[i*9+j].answer,
    print
    
    
