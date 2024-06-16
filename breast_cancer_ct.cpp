#include <iostream>
#include <Eigen/Dense>
#include <vector>

using namespace Eigen;
using namespace std;

// Function to initialize a 10x10 matrix with 'O's
MatrixXd initializeMatrix(int size) {
    MatrixXd matrix = MatrixXd::Zero(size, size);
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            matrix(i, j) = 'O';
        }
    }
    return matrix;
}

// Function to print the matrix
void printMatrix(const MatrixXd& matrix) {
    for (int i = 0; i < matrix.rows(); ++i) {
        for (int j = 0; j < matrix.cols(); ++j) {
            cout << (char)matrix(i, j) << " ";
        }
        cout << endl;
    }
}

// Function to simulate x-ray interaction with Janus spheres
void simulateXRay(MatrixXd& matrix, int startX, int startY, int endX, int endY) {
    int x = startX, y = startY;
    while (x != endX || y != endY) {
        if (matrix(x, y) == 'O') {
            matrix(x, y) = 'X';  // Mark x-ray path
        }
        x += (endX - startX) / abs(endX - startX);
        y += (endY - startY) / abs(endY - startY);
    }
}

int main() {
    int size = 10;
    MatrixXd matrix = initializeMatrix(size);
    printMatrix(matrix);

    // Simulate x-ray interaction
    simulateXRay(matrix, 0, 0, 9, 9);
    cout << "\nAfter X-ray simulation:\n";
    printMatrix(matrix);

    return 0;
}

