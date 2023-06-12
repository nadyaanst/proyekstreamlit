import streamlit as st
import numpy as np

def main():
    st.title("Homepage")

    st.header("Matrix Normalization")
    st.write("Enter the values for a 2x2 matrix.")

    # Matrix
    st.subheader("Matrix")
    m11 = st.number_input("M[1, 1]", value=0.0)
    m12 = st.number_input("M[1, 2]", value=0.0)
    m21 = st.number_input("M[2, 1]", value=0.0)
    m22 = st.number_input("M[2, 2]", value=0.0)

    # Calculate matrix normalization
    matrix = np.array([[m11, m12], [m21, m22]])
    norm_matrix = np.linalg.norm(matrix)

    if norm_matrix != 0:
        normalized_matrix = matrix / norm_matrix
    else:
        normalized_matrix = matrix

    # Display normalized matrix
    st.subheader("Normalized Matrix")
    st.write(normalized_matrix)

if __name__ == '__main__':
    main()
