import streamlit as st
import numpy as np

def main():
    st.title("Matrix Diagonalization")
    st.write("Enter the values for a 2x2 matrix.")

    # Matrix input
    matrix = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            matrix[i, j] = st.number_input(f"M[{i+1}, {j+1}]", value=0.0)

    # Diagonalize matrix
    eigenvalues, eigenvectors = diagonalize_matrix(matrix)

    # Display eigenvalues
    st.subheader("Eigenvalues")
    st.write(eigenvalues)

    # Display eigenvectors
    st.subheader("Eigenvectors")
    st.write(eigenvectors)

def diagonalize_matrix(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

if __name__ == '__main__':
    main()
