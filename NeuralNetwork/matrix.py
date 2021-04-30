import random

class Matrix:
	def __init__(self, matrix: list):
		"""
		Initialize a new matrix from a list of rows.

		Parameters
		----------

		matrix: list of lists containing numbers
			The list of rows to initialize the matrix with.
		"""
		try:
			self.numRows, self.numCols = len(matrix), len(matrix[0])
		except:
			raise Exception("Matrix must have at least one row and one column.")

		self.matrix = matrix

	@classmethod
	def zeros (cls, numRows, numCols):
		"""
		Initialize a new matrix full of zeros.

		Parameters
		----------

		numRows: int
			number of rows in the matrix
		numCols: int
			number of columns in the matrix

		"""
		return cls([[0 for _ in range(numCols)] for _ in range (numRows)])

	@classmethod
	def rand (cls, numRows, numCols, min=0, max=1):
		"""
		Similar to .zeros, but initialize each value with a random floating-point number.

		Parameters
		----------

		numRows: int
			number of rows in the matrix
		numCols: int
			number of columns in the matrix
		min: float
			minimum value of the random number
		max: float
			maximum value of the random number
		"""
		return cls([[random.uniform(min,max) for _ in range (numCols)] for _ in range(numRows)])

	def get(self, row, col):
		return self.mat[row][col]

	def set(self, row, col, value):
		self.mat[row][col] = value

	def __str__(self):
		"""
		Show the matrix in string form.
		"""
		s = "Matrix:\n"
		for row in self.mat:
			for value in row:
				s += "%8.4f" %value
			s += "\n"
		return s

def activation(matrix, activation_function):
	"""
	Run the each element of the matrix through an activation function.

	Parameters
	----------

	matrix: list of lists
		the matrix to apply the activation function on
	activation_function: function
		the function to apply
	"""
	for i in range (matrix.numRows):
		for j in range (matrix.numCols):
			matrix.set(i,j, func(matrix.get(i,j)))
	return matrix

def matrix_product (matrix1, matrix2):
	"""
	The matrix product of two matrices.
	"""
	if matrix1.numCols == matrix2.numRows:
		matrix_product = Matrix.zeros(matrix1.numRows, matrix2.numCols)
		for r in range (matrix1.numRows):
			for c in range (matrix2.numCols):
				matrix_product.matrix[r][c] = sum([matrix1.get(r,i)*matrix2.get(i,c) for i in range (matrix1.numCols)])
	else:
		raise Exception("Dimensional error")
	return matrix_product

def diagonal_product (mat1, mat2):
	"""
	Matrix multiplication but instead of multiplying all rows with all columns, multiply 
	the nth row with the nth column. This gives us a one-dimensional result.
	"""
	diag_product = []
	if mat1.numCols == mat2.numRows:
		for r in range (mat1.numRows):
			diag_product.append(sum([mat1.get(r,i)*mat2.get(i,r) for i in range (mat1.numCols)]))
	else:
		raise Exception("Dimensional error")
	return diag_product

def sum_products (list1, list2):
	"""
	The sum of the products of two lists.
	"""
	if len(list1) != len(list2):
		raise Exception("Tried to find the sum of products of two lists of different sizes")
	return sum([list1[i]*list2[i] for i in range (len(list1))])
