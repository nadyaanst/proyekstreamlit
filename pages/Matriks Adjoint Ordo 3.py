import streamlit as st
import numpy as np

def main():
    st.title("Adjoint Matrix")
    st.write("Enter the values for a 3x3 matrix to calculate its adjoint matrix.")
    
    # Input matrix
    st.subheader("Matrix")
    matrix = get_matrix_input()
    
    try:
        # Calculate adjoint matrix
        adjoint = np.linalg.pinv(matrix)
        adjoint = np.round(adjoint, 2)
        
        # Display the result
        st.subheader("Adjoint Matrix")
        st.write(adjoint)
    except np.linalg.LinAlgError:
        st.error("The input matrix is singular and doesn't have an adjoint matrix.")
    
def get_matrix_input():
    matrix_str = st.text_area("Enter values for the matrix", value="", height=100)
    matrix_list = [row.split() for row in matrix_str.strip().split('\n')]
    matrix = np.array(matrix_list, dtype=float)
    
    if matrix.shape != (3, 3):
        st.warning("The matrix should be 3x3. Please enter the correct number of values.")
        matrix = np.zeros((3, 3))
        
    return matrix

if __name__ == '__main__':
    main()
