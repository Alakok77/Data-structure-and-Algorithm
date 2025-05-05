def substring():
    word_a = input()
    word_b = input()
    cell = []
    result = ""
    most = 0
    end = (0, 0)

    for i in range(len(word_a)):
        cell.append([])
        for _ in range(len(word_b)):
            cell[i].append(0)

    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                cell[i][j] =  cell[i-1][j-1] + 1
            else:
                cell[i][j] = 0
                
            if cell[i][j] > most:
                most = cell[i][j]
                end = (i, j)

    if not most:
        print("No common substring.")
        return

    i, j = end
    while cell[i][j] > 0:
        result = word_a[i] + result
        i -= 1
        j -= 1
        if i < 0 or j < 0:
            break

    print(result)
    print(most)

substring()
                            