def matrix_bin_search(matrix: list, target: int) -> tuple:
    r_lo = 0
    r_hi = len(matrix)-1

    c_lo = 0
    c_hi = len(matrix[0])-1
    r_mid = 0

    while (r_lo <= r_hi):
        r_mid = r_lo + (r_hi - r_lo)//2
        if target > matrix[r_mid][c_hi]:
            r_lo = r_mid + 1
        elif target < matrix[r_mid][c_lo]:
            r_hi = r_mid - 1
        else:
            break
    
    while (c_lo <= c_hi):
        c_mid = c_lo + (c_hi - c_lo)//2
        if target < matrix[r_mid][c_mid]:
            c_hi = c_mid - 1
        elif target > matrix[r_mid][c_mid]:
            c_lo = c_mid + 1
        else:
            return (r_mid, c_mid)
            
    return -1


A = \
[
    [1, 2, 4, 6, 8],
    [12, 14, 18, 22, 25],
    [29, 30, 31, 35, 36],
    [39, 40, 42, 44, 49]
]

print("Where is 44 in matrix?:", matrix_bin_search(A, 44))
print("Where is 38 in matrix?:", matrix_bin_search(A, 38))
