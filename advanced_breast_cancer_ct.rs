use rand::Rng;

fn initialize_matrix(size: usize) -> Vec<Vec<char>> {
    vec![vec!['O'; size]; size]
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

fn detect_regions(matrix: &Vec<Vec<char>>) -> Vec<(usize, usize)> {
    let mut regions = Vec::new();
    for (i, row) in matrix.iter().enumerate() {
        for (j, &cell) in row.iter().enumerate() {
            if cell == 'X' {
                regions.push((i, j));
            }
        }
    }
    regions
}

fn simulate_multiple_xray_paths(matrix: &mut Vec<Vec<char>>, num_paths: usize) {
    let size = matrix.len();
    let mut rng = rand::thread_rng();

    for _ in 0..num_paths {
        let start_x = rng.gen_range(0..size);
        let start_y = rng.gen_range(0..size);
        let end_x = rng.gen_range(0..size);
        let end_y = rng.gen_range(0..size);
        simulate_xray(matrix, start_x, start_y, end_x, end_y);
    }
}

fn main() {
    let size = 10;
    let mut matrix = initialize_matrix(size);
    print_matrix(&matrix);

    // Simulate multiple x-ray paths
    simulate_multiple_xray_paths(&mut matrix, 5);
    println!("\nAfter X-ray simulation:");
    print_matrix(&matrix);

    // Detect regions of interest
    let regions = detect_regions(&matrix);
    println!("\nRegions of interest:");
    for region in regions {
        println!("({}, {})", region.0, region.1);
    }
}

