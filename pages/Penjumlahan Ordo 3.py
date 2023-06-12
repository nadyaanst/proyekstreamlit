import streamlit as st
import numpy as np

def matrix_addition(matrix1, matrix2):
    result = np.add(matrix1, matrix2)
    return result

def main():
    st.title("Matrix Addition")
    st.write("Enter the elements of two 3x3 matrices to perform matrix addition.")

    # Create input fields for matrix 1
    st.write("Matrix 1:")
    matrix1 = []
    for i in range(3):
        row = []
        for j in range(3):
            value = st.number_input(f"Enter element at position ({i+1}, {j+1})", key=f"matrix1_{i}_{j}")
            row.append(value)
        matrix1.append(row)

    # Create input fields for matrix 2
    st.write("Matrix 2:")
    matrix2 = []
    for i in range(3):
        row = []
        for j in range(3):
            value = st.number_input(f"Enter element at position ({i+1}, {j+1})", key=f"matrix2_{i}_{j}")
            row.append(value)
        matrix2.append(row)

    # Perform matrix addition
    if st.button("Add Matrices"):
        result = matrix_addition(matrix1, matrix2)
        st.write("Result:")
        st.write(np.array(result))

if __name__ == '__main__':
    main()
