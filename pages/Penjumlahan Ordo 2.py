import streamlit as st
import numpy as np

def matrix_addition():
    st.header("Matrix Addition")
    st.write("Enter the values for two 2x2 matrices.")

    # Matrix A
    st.subheader("Matrix A")
    a11 = st.number_input("A[1, 1]", key="A11")
    a12 = st.number_input("A[1, 2]", key="A12")
    a21 = st.number_input("A[2, 1]", key="A21")
    a22 = st.number_input("A[2, 2]", key="A22")

    # Matrix B
    st.subheader("Matrix B")
    b11 = st.number_input("B[1, 1]", key="B11")
    b12 = st.number_input("B[1, 2]", key="B12")
    b21 = st.number_input("B[2, 1]", key="B21")
    b22 = st.number_input("B[2, 2]", key="B22")

    # Calculate matrix addition
    a = np.array([[a11, a12], [a21, a22]])
    b = np.array([[b11, b12], [b21, b22]])
    result = a + b

    # Display result
    st.subheader("Result (A + B)")
    st.write(result)

if __name__ == '__main__':
    matrix_addition()
