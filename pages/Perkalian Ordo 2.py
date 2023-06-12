import streamlit as st
import numpy as np

def main():
    st.title("Homepage")

    st.header("Matrix Multiplication")
    st.write("Enter the values for two 2x2 matrices.")

    # Matrix A
    st.subheader("Matrix A")
    a11 = st.number_input("A[1, 1]", value=0.0)
    a12 = st.number_input("A[1, 2]", value=0.0)
    a21 = st.number_input("A[2, 1]", value=0.0)
    a22 = st.number_input("A[2, 2]", value=0.0)

    # Matrix B
    st.subheader("Matrix B")
    b11 = st.number_input("B[1, 1]", value=0.0)
    b12 = st.number_input("B[1, 2]", value=0.0)
    b21 = st.number_input("B[2, 1]", value=0.0)
    b22 = st.number_input("B[2, 2]", value=0.0)

    # Calculate matrix multiplication
    a = np.array([[a11, a12], [a21, a22]])
    b = np.array([[b11, b12], [b21, b22]])

    try:
        result = np.matmul(a, b)
        st.subheader("Result (A * B)")
        st.write(result)
    except ValueError as e:
        st.error("Error: Matrix dimensions are incompatible for multiplication.")
        st.error(str(e))

if __name__ == '__main__':
    main()
