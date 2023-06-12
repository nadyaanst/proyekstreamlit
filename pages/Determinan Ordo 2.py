import streamlit as st
import numpy as np

def main():
    st.title("Matrix Determinant")
    st.write("Enter the values for a 2x2 matrix to calculate its determinant.")
    
    # Input matrix
    st.subheader("Matrix")
    matrix = get_matrix_input("a", 2)
    
    # Calculate determinant
    determinant = np.linalg.det(matrix)
    
    # Display the result
    st.subheader("Determinant")
    st.write(determinant)
    
def get_matrix_input(label, size):
    matrix_str = st.text_area(f"Enter values for matrix {label}", value="", height=100)
    matrix_list = [row.split() for row in matrix_str.strip().split('\n')]
    matrix = np.array(matrix_list, dtype=float)
    
    if matrix.shape != (size, size):
        st.warning(f"The matrix {label} should be {size}x{size}. Please enter the correct number of values.")
        matrix = np.zeros((size, size))
        
    return matrix

if __name__ == '__main__':
    main()
