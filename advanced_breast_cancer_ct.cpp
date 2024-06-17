#include <iostream>
#include <Eigen/Dense>
#include <vector>
#include <cstdlib>
#include <ctime>

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

// Function to detect regions of interest
vector<pair<int, int>> detectRegions(const MatrixXd& matrix) {
    vector<pair<int, int>> regions;
    for (int i = 0; i < matrix.rows(); ++i) {
        for (int j = 0; j < matrix.cols(); ++j) {
            if (matrix(i, j) == 'X') {
                regions.push_back(make_pair(i, j));
            }
        }
    }
    return regions;
}

// Function to simulate multiple x-ray paths
void simulateMultipleXRayPaths(MatrixXd& matrix, int numPaths) {
    srand(time(0));
    for (int i = 0; i < numPaths; ++i) {
        int startX = rand() % matrix.rows();
        int startY = rand() % matrix.cols();
        int endX = rand() % matrix.rows();
        int endY = rand() % matrix.cols();
        simulateXRay(matrix, startX, startY, endX, endY);
    }
}

int main() {
    int size = 10;
    MatrixXd matrix = initializeMatrix(size);
    printMatrix(matrix);

    // Simulate multiple x-ray paths
    simulateMultipleXRayPaths(matrix, 5);
    cout << "\nAfter X-ray simulation:\n";
    printMatrix(matrix);

    // Detect regions of interest
    vector<pair<int, int>> regions = detectRegions(matrix);
    cout << "\nRegions of interest:\n";
    for (const auto& region : regions) {
        cout << "(" << region.first << ", " << region.second << ")\n";
    }

    return 0;
}

