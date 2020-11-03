# -*- coding: utf-8 -*-
"""
This is the MiniMax search Algorithm
""" 
import numpy as np
import math

def euclid_dist(p1,p2):
    return  np.sqrt((p1[0]-p2[0])^2 + (p1[1]-p2[1])^2)
    


""" 
def closest_m(pos, peice_type, m_type):
    if m_type = win:
        win_matchups = []  
    
        return min(euclid_dist(pos,m_1),euclid_dist(pos,m_1),\ 
                   euclid_dist(pos,m_3))
    else:
        draw_matchups = [] 
        return min(euclid_dist(pos,m_1),euclid_dist(pos,m_1),\ 
                   euclid_dist(pos,m_3))


def static_eval(position,p_type): 
    
    return 0.25 * pieces_left + 0.25 * closest_m(pos,p_type,"draw") 
    + 0.50 * closest_m(pos,p_type,"win")

"""    
    

def move_set(pos): # possible move
    
    p_m= [[pos[0]-1, pos[1]], [pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0],\
           pos[1]-1], [pos[0]-1, pos[1]+1], [pos[0]+1, 
           pos[1]-1], [pos[0]-1, pos[1]-1],[pos[0]+1, pos[1]+1]]
    
    out_m = [None]*0
    for move in p_m:
        if p_m[0] > 0 and p_m[1] > 0:
            out_m.append(p_m)
            
    return out
    
    
    
def minimax(position, tree_depth, bMaxPlayer):
     if tree_depth == 0 or goal(position,p_type): 
         return static_eval(position) #static evaluation
     if bMaxPlayer:
         MaxOut = -inf
         p_moves = mov_set(position)
         for move in p_moves: # all spaces within one move of current pos
             MaxCur = minimax(move, tree_depth − 1, False)
             MaxOut = max(MaxOut,MaxCur)
         return MaxOut
     
     else: 
         MinOut = inf
         p_moves = move_set(position)
         for move in p_moves:
             MinCur = minimax(move, tree_depth − 1, True)
             MinOut = min(MinOut,MinCur)
         return MinOut
 


