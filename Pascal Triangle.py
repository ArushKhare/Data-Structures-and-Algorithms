def pascal_triangle(n):

    # rows
    def rows(n):
        res = []
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        previous = rows(n - 1)
        new = [1]
        for i in range(len(previous) - 1):
            new.append(previous[i] + previous[i + 1])
        return new + [1]

    # triangle
    triangle = []
    for i in range(1, n+1):
        triangle.append(rows(i))
    return triangle

x = int(input('Enter row for Pascal Triangle: '))
print(pascal_triangle(x))
