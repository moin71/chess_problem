from django.shortcuts import render
from django.http import HttpResponse
import json

def findValidMoves(request):
    data = json.loads(request.body)
    path = request.path
    query = path.split('/')[-1]
    positions = data['postions']

    print('query is :', query)

    bishop = positions['Bishop']
    queen = positions['Queen']
    knight = positions['Knight']
    rook = positions['Rook']


    knight_moves = knightMoves(knight)
    print('knight moves are: ', knight_moves)


    bishop_moves = bishopMoves(bishop)
    print('bishop moves are: ', bishop_moves)


    queen_moves = queenMoves(queen)
    print('queen moves are: ', queen_moves)


    rook_moves = rookMoves(rook)
    print('rook moves are: ', rook_moves)

    if query == 'knight':
        valid_moves = list(set(knight_moves)- set(bishop_moves+queen_moves+rook_moves))
        print('safe moves for knight are: ', valid_moves)

    if query == 'queen':
        valid_moves = list(set(queen_moves)- set(bishop_moves+knight_moves+rook_moves))
        print('safe moves for queen are: ', valid_moves)

    if query == 'bishop':
        valid_moves = list(set(bishop_moves)- set(knight_moves+queen_moves+rook_moves))
        print('safe moves for bishop are: ', valid_moves)

    if query == 'rook':
        valid_moves = list(set(rook_moves)- set(bishop_moves+queen_moves+knight_moves))
        print('safe moves for rook are: ', valid_moves)

    response = {"valid_moves":valid_moves}

    return HttpResponse(json.dumps(response))

def isValidMove(x, y):
        if ord('A') <= x <= ord('H') and 1 <= y <= 8:
            return True
        return False

def knightMoves(knight):
    knight_moves = []
    knight_steps = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
    for x, y in knight_steps:
        moved_x, moved_y = ord(knight[0]) + x, int(knight[1]) + y
        if isValidMove(moved_x, moved_y):
            knight_moves.append(chr(moved_x) + str(moved_y))
    print('knight moves are: ', knight_moves)
    return knight_moves

def bishopMoves(bishop):
    directions = [ (1, 1), (1, -1), (-1, 1), (-1, -1) ] 
    bishop_moves = []
    for dx, dy in directions:
        step = 1
        while True:
            moved_x, moved_y = ord(bishop[0]) + step * dx, int(bishop[1]) + step * dy
            if isValidMove(moved_x, moved_y):
                bishop_moves.append(chr(moved_x) + str(moved_y))
            else:
                break
            step += 1
    return bishop_moves

def queenMoves(queen):
    directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)  
        ]
    queen_moves = []
    for dx, dy in directions:
        step = 1
        while True:
            moved_x, moved_y = ord(queen[0]) + step * dx, int(queen[1]) + step * dy
            if isValidMove(moved_x, moved_y):
                queen_moves.append(chr(moved_x) + str(moved_y))
            else:
                break
            step += 1
    return queen_moves

def rookMoves(rook):
    directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1), 
        ]
    rook_moves = []
    for dx, dy in directions:
        step = 1
        while True:
            moved_x, moved_y = ord(rook[0]) + step * dx, int(rook[1]) + step * dy
            if isValidMove(moved_x, moved_y):
                rook_moves.append(chr(moved_x) + str(moved_y))
            else:
                break
            step += 1
    return rook_moves