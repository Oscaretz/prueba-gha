A = [[1, 2, 3],
     [1, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 0, 4],
     [3, 2, 1]]

def matmul(A,B, output_file):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return matmul_res(result, output_file)

def matmul_res(x, output_file):
    with open(output_file, 'w') as file:
        file.write("Matrix Multiplication Result:\n")
        for row in x:
            file.write(' '.join(map(str, row)) + '\n')

output_file = "matrixresult.txt"
matmul(A,B, output_file)
