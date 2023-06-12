import streamlit as st
import numpy as np

def main():
    st.title("Matrix Normalization")
    st.write("Enter the values for a 3x3 matrix.")

    # Matrix input
    matrix = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            matrix[i, j] = st.number_input(f"M[{i+1}, {j+1}]", value=0.0)

    # Normalize matrix
    normalized_matrix = normalize_matrix(matrix)

    # Display normalized matrix
    st.subheader("Normalized Matrix")
    st.write(normalized_matrix)

def normalize_matrix(matrix):
    norm_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
    return norm_matrix

if __name__ == '__main__':
    main()
