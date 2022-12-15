use std::fs;
use std::io::{BufReader, BufRead};
use std::error::Error;
use std::iter::zip;
use std::cmp::{min, max};
use std::time::Instant;

use bitvec::bitbox;

fn main() -> Result<(), Box<dyn Error>> {
    let mut sensors: Vec<(i32, i32)> = Vec::new();
    let mut beacons: Vec<(i32, i32)> = Vec::new();

    let file = fs::File::open("day15.in")?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line_ = line?;
        let words = line_.split(" ").collect::<Vec<&str>>();
        let x1 = words[2][2..words[2].len()-1].parse::<i32>()?;
        let y1 = words[3][2..words[3].len()-1].parse::<i32>()?;
        let x2 = words[8][2..words[8].len()-1].parse::<i32>()?;
        let y2 = words[9][2..].parse::<i32>()?;

        sensors.push((x1, y1));
        beacons.push((x2, y2));
    }

    let mut x_arr = bitbox![0; 4000000];
    let search_space_max = 4000000;
    for y in 0..(search_space_max + 1) {
        //let start_time = Instant::now();
        x_arr.fill(true);
        for ((sx, sy), (bx, by)) in zip(sensors.iter(), beacons.iter()) {
            let max_distance = (by - sy).abs() + (bx - sx).abs();
            let min_y = max(0, sy - max_distance);
            let max_y = min(search_space_max, sy + max_distance);
            if y < min_y || y > max_y {
                continue;
            }

            let min_x = max(0, sx - (max_distance - (sy - y).abs()).abs());
            let max_x = min(search_space_max, sx + (max_distance - (sy - y).abs()).abs() + 1);

            x_arr[min_x as usize..max_x as usize].fill(false);
        }
        if x_arr.any() {
            let x = x_arr.first_one().unwrap() as i32;
            println!("(x, y) = ({}, {})", x, y);
            println!("tuning frequency = {}", x * 4000000 + y);
        }
        //println!("Iteration took {:?}", start_time.elapsed());
    }

    Ok(())
}
