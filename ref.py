import time

# get the start time
print("REF Simplifier")
print("By Steven Schonlau")
print("Enter rows:")
rows = int(input())

print("Enter columns:")
columns = int(input())

print("Do you want steps? (1/0)")
steps = int(input())


matrix = []
for i in range(rows):
    print(f"Enter row {i+1}, elements separated by ' '")
    matrix.append([float(x) for x in input().split()])

st = time.time()
print("Original Matrix:")
for row in matrix:
    for elem in row:
        print(f"{elem:.3f} ", end="")
    print()
print("\nSolution:")


#REF
placeholder = 0
for i in range(columns):
    for j in range(placeholder, rows):
        if matrix[j][i] != 0:
            matrix[placeholder], matrix[j] = matrix[j], matrix[placeholder]
            row_reducer = matrix[placeholder][i]
            matrix[placeholder] = [elem / row_reducer for elem in matrix[placeholder]]
            for k in range(placeholder + 1, rows):
                multiple = matrix[k][i] / matrix[placeholder][i]
                matrix[k] = [elem - multiple * matrix[placeholder][m] for m, elem in enumerate(matrix[k])]
            placeholder += 1

            if steps == 1:
                for q in range(rows):
                    for b in range(columns):
                        print(f"{matrix[q][b]:.3f} ", end="")
                    print()
                print()

        elif j == rows - 1:
            break

#RREF
for i in range(rows-1, -1, -1):
    for j in range(columns):
        if matrix[i][j] == 1:
            placeholder = i
            for k in range(placeholder-1, -1, -1):
                multiple = matrix[k][j] / matrix[placeholder][j]
                matrix[k] = [elem - multiple * matrix[placeholder][m] for m, elem in enumerate(matrix[k])]

        if steps == 1:
            for q in range(rows):
                for b in range(columns):
                    print(f"{matrix[q][b]:.3f} ", end="")
                print()
            print()

print("Final Matrix:")
for row in matrix:
    for elem in row:
        print(f"{elem:.3f} ", end="")
    print()

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
