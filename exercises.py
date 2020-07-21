from collections import Counter

def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """
    return Counter(s1) == Counter(s2)

def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """
    if string.count("(") == string.count(")"):
        return True
    return False

import copy

def is_valid(maze, visited, x_max, y_max, x, y):
    return (x >= 0) and (x < x_max) and (y >= 0) and (y < y_max) and (visited[x][y] != 2) and (maze[x][y] == 1)

def find_path(start, end, result, previous):
    if result[0] == start:
        return result
    for key, value in previous.items():
        if key == end:
            result.insert(0, value)
            find_path(start, value, result, previous)
    return result

def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """
    moves = [(-1, 0), (0, 1), (1, 0), (0,-1)]

    if maze and maze[0]:
        x_max = len(maze)
        y_max = len(maze[0])
    else:
        return False
    pt_start = maze[start[0]][start[1]]
    visited = copy.deepcopy(maze)
    visited[start[0]][start[1]] = 2
    queue = []
    queue.append((start[0], start[1], 0))
    previous = {}
    while queue:
        (x_cell, y_cell, dist) = queue.pop(0)
        if x_cell == end[0] and y_cell == end[1]:
            return find_path(start, end, [end], previous)
        for move in moves:
            if is_valid(maze, visited, x_max, y_max, x_cell + move[0], y_cell + move[1]):
                visited[x_cell][y_cell] = 2
                previous[(x_cell + move[0], y_cell + move[1])] = (x_cell, y_cell)
                queue.append((x_cell + move[0], y_cell + move[1], dist + 1))
    return False
