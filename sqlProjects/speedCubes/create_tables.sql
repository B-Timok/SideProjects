-- Create the speedcubes database if it doesn't exist
CREATE DATABASE IF NOT EXISTS speedcubes;

-- Use the speedcubes database
USE speedcubes;

-- Create a table for speedcube collection
CREATE TABLE cubes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255),
    release_year INT
);

-- Create a table for time statistics
CREATE TABLE times (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cube_id INT,
    avg100 DECIMAL(6, 2),
    avg12 DECIMAL(6, 2),
    avg5 DECIMAL(6, 2),
    best_single DECIMAL(6, 2),
    FOREIGN KEY (cube_id) REFERENCES cubes(id)
);