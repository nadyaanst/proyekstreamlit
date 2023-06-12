import streamlit as st
import numpy as np

def main():
    st.title("Matrix Diagonalization")
    st.write("Enter the values for a 3x3 matrix.")

    # Matrix input
    matrix = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            matrix[i, j] = st.number_input(f"M[{i+1}, {j+1}]", value=0.0)

    # Diagonalize matrix
    diagonal_matrix, eigenvectors = diagonalize_matrix(matrix)

    # Display diagonalized matrix and eigenvectors
    st.subheader("Diagonalized Matrix")
    st.write(diagonal_matrix)

    st.subheader("Eigenvectors")
    st.write(eigenvectors)

def diagonalize_matrix(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    diagonal_matrix = np.diag(eigenvalues)
    return diagonal_matrix, eigenvectors

if __name__ == '__main__':
    main()
