def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if not len(a[0]) == len(b):
        return -1
    result = []
    for row in range(len(a)):
        new_line = []
        for column in range(len(b[0])):
            new_line.append(0)
        result.append(new_line)

    for row in range(len(a)):
        for column in range(len(b[0])):
            for step in range(len(a[0])):
                result[row][column] += a[row][step] * b[step][column]
    return result








