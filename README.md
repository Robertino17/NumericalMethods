# Solving a system of linear equations with Gauss Elimination
numer_met.solve_linear_system(A, B) <br />
That function solves a system of linear equations ***AX = B*** by reducing the matrix A to a triangular view. In that process, the rows are moving to reduce the error. Then the reverse way perfoms and we find the solution of the system. <br />
**Parameters:**  A: np.array <br />
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;The coefficient matrix. <br />
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;B: np.array <br />
&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;Vector, containing the right part. <br />
**Returns:**  X: np.array <br />
&emsp;&emsp;&emsp;Vector, containing the solution. <br />
