import streamlit as st
import numpy as np

def main():
    st.title("Adjoint Matrix")
    st.write("Enter the values for a 2x2 matrix to calculate its adjoint matrix.")
    
    # Input matrix
    st.subheader("Matrix")
    matrix = get_matrix_input()
    
    # Calculate adjoint matrix
    adjoint_matrix = calculate_adjoint(matrix)
    
    # Display the result
    st.subheader("Adjoint Matrix")
    st.write(adjoint_matrix)
    
def get_matrix_input():
    matrix_str = st.text_area("Enter values for the matrix", value="", height=100)
    matrix_list = [row.split() for row in matrix_str.strip().split('\n')]
    matrix = np.array(matrix_list, dtype=float)
    
    if matrix.shape != (2, 2):
        st.warning("The matrix should be 2x2. Please enter the correct number of values.")
        matrix = np.zeros((2, 2))
        
    return matrix

def calculate_adjoint(matrix):
    adjoint_matrix = np.zeros_like(matrix)
    adjoint_matrix[0, 0] = matrix[1, 1]
    adjoint_matrix[0, 1] = -matrix[0, 1]
    adjoint_matrix[1, 0] = -matrix[1, 0]
    adjoint_matrix[1, 1] = matrix[0, 0]
    
    return adjoint_matrix

if __name__ == '__main__':
    main()
