# function to extract a matrix from a file


def getMatrix(data):
    matrix = []
    for i in range(0, len(data)):
        a = data[i].split(" ")
        for j in range(0, len(a)):
            a[j] = int(a[j])
        matrix.append(a)
    return matrix


# geting the first matrix
handle = open("1/source1.txt")
data = handle.read().split("\n")
mx1 = getMatrix(data)
handle.close

# geting the second matrix
handle = open("1/source2.txt")
data = handle.read().split("\n")
mx2 = getMatrix(data)
handle.close


# checking the size
if not (len(mx1[0]) == len(mx2)):
    print("The number of columns in the first matrix must match the number of rows in the second matrix.")

m = len(mx2[0])
n = len(mx1)

# multiplication
c = []
for i in range(n):
    inc = []
    for j in range(m):
        inc.append(0)
    c.append(inc)

for ci in range(0, int(n)):
    for cj in range(0, int(m)):
        c[ci][cj] = 0
        for i in range(0, len(mx2)):
            c[ci][cj] += mx1[ci][i]*mx2[i][cj]

def up_to_3_det(matrix):
    if (len(matrix) != len(matrix[0])):
        return "The number of rows should match the number of coloumns"
    elif (len(matrix) == 1):
        return "Undefined value of determinant"
    elif (len(matrix) == 2):
        return matrix[1][1] * matrix[0][0] - matrix[1][0] * matrix[0][1]
    else:
        return ((matrix[0][0] *((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))) -
      (matrix[0][1] *((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))) +
      (matrix[0][2] *((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))))

print(up_to_3_det(c))
