# def max_sequence(arr):
#     max_sum = 0
#     current_sum = 0

#     for num in arr:
#         current_sum = max(0, current_sum + num)
#         max_sum = max(max_sum, current_sum)

#     return max_sum

# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) 

# ---------------------------------------------------------------------------------------

# def sudoku(puzzle):
    
#     def find_empty(puzzle):
#         for r in range(9):
#             for c in range(9):
#                 if puzzle[r][c] == 0:
#                     return r, c
#         return None

#     def valid(puzzle, num, pos):
#         r, c = pos

#         if num in puzzle[r]:
#             return False

#         if num in [puzzle[i][c] for i in range(9)]:
#             return False

#         box_r, box_c = r // 3 * 3, c // 3 * 3
#         for i in range(box_r, box_r + 3):
#             for j in range(box_c, box_c + 3):
#                 if puzzle[i][j] == num:
#                     return False

#         return True

#     def solve(puzzle):
#         find = find_empty(puzzle)
#         if not find:
#             return True  
#         r, c = find

#         for num in range(1, 10):
#             if valid(puzzle, num, (r, c)):
#                 puzzle[r][c] = num

#                 if solve(puzzle):
#                     return True

#                 puzzle[r][c] = 0  

#         return False

#     solve(puzzle)
#     return puzzle

# puzzle = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,7,9]
# ]

# for row in sudoku(puzzle):
#     print(row)

#----------------------------------------------------------------------------------------



