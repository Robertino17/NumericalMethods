# Solving a system of linear equations with Gauss Elimination
numer_met.solve_linear_system(A, B)__
That function solves a system of linear equations ***AX = B*** by reducing the matrix A to a triangular view. In that process, the rows are moving to reduce the error. Then the reverse way perfoms and we find the solution of the system.
**Parameters:**  A: np.array
                 The coefficient matrix.
                 B: np.array
                 Vector, containing the right part.
**Returns:**  X: np.array
              Vector, containing the solution.
