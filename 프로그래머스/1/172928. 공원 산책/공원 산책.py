def solution(park, routes):
    row = 0
    for i in park:
        if 'S' in i:
            col = i.find('S')
            break
        row += 1
    # print(row, col)
    
    for i in routes:
        move = True
        isrow = 0 if i[0] == 'E' or i[0] == 'W' else 1
        iscol = 0 if i[0] == 'N' or i[0] == 'S' else 1
        sign = 1 if i[0] == 'E' or i[0] == 'S' else -1
        
        for j in range(int(i[2])):
            if not check(park, row + isrow * sign * (j + 1), col + iscol * sign * (j + 1)):
                move = False
                break
        if move:
            row += isrow * sign * int(i[2])
            col += iscol * sign * int(i[2])
        # print(row, col)
    
    return [row, col]

def check(park, row, col):
    if row < 0 or col < 0 or row >= len(park) or col >= len(park[0]):
        return False
    if park[row][col] == 'X':
        return False
    return True