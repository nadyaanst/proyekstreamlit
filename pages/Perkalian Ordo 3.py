import streamlit as st
import numpy as np

def main():
    st.title("Matrix Multiplication")
    st.write("Enter the values for two 3x3 matrices to perform multiplication.")
    
    # Input matrix A
    st.subheader("Matrix A")
    matrix_a = get_matrix_input("a", 3)
    
    # Input matrix B
    st.subheader("Matrix B")
    matrix_b = get_matrix_input("b", 3)
    
    # Perform matrix multiplication
    result = np.dot(matrix_a, matrix_b)
    
    # Display the result
    st.subheader("Result")
    st.write(result)
    
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
