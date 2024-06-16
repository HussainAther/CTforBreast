fn initialize_matrix(size: usize) -> Vec<Vec<char>> {
    let mut matrix = vec![vec!['O'; size]; size];
    matrix
}

fn print_matrix(matrix: &Vec<Vec<char>>) {
    for row in matrix {
        for cell in row {
            print!("{} ", cell);
        }
        println!();
    }
}

fn simulate_xray(matrix: &mut Vec<Vec<char>>, start_x: usize, start_y: usize, end_x: usize, end_y: usize) {
    let mut x = start_x;
    let mut y = start_y;
    let step_x = if end_x >= start_x { 1 } else { -1 } as isize;
    let step_y = if end_y >= start_y { 1 } else { -1 } as isize;
    
    while x != end_x || y != end_y {
        if matrix[x][y] == 'O' {
            matrix[x][y] = 'X';  // Mark x-ray path
        }
        if x != end_x {
            x = (x as isize + step_x) as usize;
        }
        if y != end_y {
            y = (y as isize + step_y) as usize;
        }
    }
}

fn main() {
    let size = 10;
    let mut matrix = initialize_matrix(size);
    print_matrix(&matrix);

    // Simulate x-ray interaction
    simulate_xray(&mut matrix, 0, 0, 9, 9);
    println!("\nAfter X-ray simulation:");
    print_matrix(&matrix);
}

