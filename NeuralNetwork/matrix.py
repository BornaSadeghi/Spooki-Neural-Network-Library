import random

class Matrix:
	def __init__(self, matrix: list):
		"""
		Initialize a new 2D matrix from a list of rows.
		So, columns are represented by the inner list, while rows are represented by the outer list.

		Parameters
		----------
		matrix: list of lists containing numbers
			The list of rows to initialize the matrix with.
			e.g. [[1,2,3], [4,5]]
		
		TODO Handle matrices with rows/columns of different sizes (don't allow them)
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

	def shape(self):
		return len(self.matrix), len(self.matrix[0])

	def get2dArray(self):
		return self.matrix

	def getRow(self, rowIndex):
		"""
		Return a specific row of values in the matrix.

		Parameters
		----------
		rowIndex: The index of the row to retrieve.
		"""
		return self.matrix[rowIndex]

	def getCol(self, colIndex):
		"""
		Return a specific column of values in the matrix.

		Parameters
		----------
		colIndex: The index of the column to retrieve.
		"""
		return [ row[colIndex] for row in self.matrix ]

	def get(self, row, col):
		"""
		Retrieve the value at (row, col) inside the matrix.

		Parameters
		----------
		row: int
			The row to get the value from
		col: int
			The column to get the value from
		"""
		try:
			return self.mat[row][col]
		except:
			raise Exception("row or col is not inside the matrix boundaries.")

	def set(self, row, col, value):
		"""
		Set the value at (row, col) inside the matrix.

		Parameters
		----------
		row: int
			The row to set the value at
		col: int
			The column to set the value at
		"""
		try:
			self.mat[row][col] = value
		except:
			raise Exception("row or col is not inside the matrix boundaries.")

	def __str__(self):
		"""
		Return the matrix in string form.
		"""
		s = "Matrix:\n"
		for row in self.matrix:
			for value in row:
				s += "%8.4f" %value
			s += "\n"
		return s

def dot (list1, list2):
	"""
	The dot product (sum of the products) of two lists.
	"""
	if len(list1) != len(list2):
		raise Exception("Tried to find the dot product of two lists of different lengths")
	return sum([list1[i]*list2[i] for i in range (len(list1))])

def matrix_product (matrix1, matrix2):
	"""
	The matrix product of two matrices.
	"""
	if matrix1.numCols == matrix2.numRows:
		matrix_product = Matrix.zeros(matrix1.numRows, matrix2.numCols)
		for r in range (matrix1.numRows):
			for c in range (matrix2.numCols):
				matrix_product.matrix[r][c] = dot(matrix1.getRow(r), matrix2.getCol(c))
	else:
		raise Exception("Dimensional error")
	return matrix_product

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