count = 0

def isVisible(M, i, j, nr, nc, direction):
    global count

    lr, ud = 0, 0
    cur = M[i][j]

    # get movement (left-right) or (up-down); otherwise no movement remains as 0
    if (direction == 'LEFT'):       lr = -1
    elif (direction == 'RIGHT'):    lr = 1
    elif (direction == 'UP'):       ud = -1
    else:                           ud = 1

    # initial checking position
    ii, jj = i + ud, j + lr

    while ((0 <= ii <= nc) and (0 <= jj <= nr)):
        if cur <= M[ii][jj]: return False
        ii, jj = ii + ud, jj + lr
    
    count += 1
    return True

def main():
    M = []
    with open('data.txt', 'r') as f:
        for line in f:
            M.append([int(num) for num in list(*line[0:-1].split())])

    nr, nc = len(M)-1, len(M[0])-1

    # outer grid is always visible
    edge_case = (nr-1)*2 + (nc-1)*2 + 4

    # check if inner grid is visible
    for i in range(1, nc):
        for j in range(1, nr):
            M_dat = (M, i, j, nr, nc)
            if isVisible(*M_dat, 'LEFT') or isVisible(*M_dat, 'RIGHT') or isVisible(*M_dat, 'UP') or isVisible(*M_dat, 'DOWN'):
                continue
            
    print(f'Total visible trees = {edge_case + count}')

if __name__ == "__main__":
    main()