x = [1, 2, 3]
y = [4, 5, 6]

# RUF017
sum([x, y], start=[])
sum([x, y], [])
sum([[1, 2, 3], [4, 5, 6]], start=[])
sum([[1, 2, 3], [4, 5, 6]], [])

# OK
sum([x, y])
sum([[1, 2, 3], [4, 5, 6]])