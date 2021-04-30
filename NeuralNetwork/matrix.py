import random

class Matrix:
	def __init__(self, rows: list):
		"""
		Initialize a new matrix from a list of rows.

		Parameters
		----------

		rows: list of lists containing numbers
			The list of rows to initialize the matrix with.

		"""
		try:
			self.nRows, self.nCols = len(rows), len(rows[0])
		except:
			raise Exception("Matrix must have at least one row and one column.")

		self.mat = rows

	@classmethod
	def zeros (cls, nRows, nCols):
		"""
		Initialize a new matrix full of zeros.

		Parameters
		----------

		nRows: int
			number of rows in the matrix
		nCols: int
			number of columns in the matrix

		"""
		return cls([[0 for _ in range(nCols)] for _ in range (nRows)])

	@classmethod
	def rand (cls, nRows, nCols, min=0, max=1):
		"""
		Similar to .zeros, but initialize each value with a random floating-point number.
		"""
		return cls([[random.uniform(min,max) for _ in range (nCols)] for _ in range(nRows)])

	def get(self, row, col):
		return self.mat[row][col]

	def set(self, row, col, value):
		self.mat[row][col] = value

	def __str__(self):
		s = "Matrix:\n"
		for row in self.mat:
			for value in row:
				s += "%8.4f" %value
			s += "\n"
		return s

def activation(mat, func):
	for i in range (mat.nRows):
		for j in range (mat.nCols):
			mat.set(i,j, func(mat.get(i,j)))
	return mat

def product (mat1, mat2):
	"""
	The matrix product of two matrices.
	"""
	mat_product = Matrix.zeros(mat1.nRows, mat2.nCols)
	if mat1.nCols == mat2.nRows:
		for r in range (mat1.nRows):
			for c in range (mat2.nCols):
				mat_product.mat[r][c] = sum([mat1.get(r,i)*mat2.get(i,c) for i in range (mat1.nCols)])
	else:
		raise Exception("Dimensional error")
	return mat_product

def diagonal_product (mat1, mat2):
	"""
	Matrix multiplication but instead of multiplying all rows with all columns, multiply 
	the nth row with the nth column. This gives us a one-dimensional result.
	"""
	diag_product = []
	if mat1.nCols == mat2.nRows:
		for r in range (mat1.nRows):
			diag_product.append(sum([mat1.get(r,i)*mat2.get(i,r) for i in range (mat1.nCols)]))
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
