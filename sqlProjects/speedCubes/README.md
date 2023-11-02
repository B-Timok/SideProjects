# Speedcubes Database

This project creates a MySQL database to track my speedcube collection. It includes tables for cube information and time statistics. Here's how to set it up and use it.

## Table of Contents
- [Database Structure](#database-structure)
- [Getting Started](#getting-started)
- [Sample Queries](#sample-queries)

## Database Structure
The project contains two table: 'cubes' and 'times'.

### Cubes Table
- 'id': Unique identifier for each cube.
- 'name': Name of the cube.
- 'brand': Brand of the cube.
- 'release_year': Year the cube was released.

### Times Table
- 'id': Unique identifier for each time record.
- 'cube_id': Foreign key referencing the cube to each time record belongs.
- 'avg100': Best average of 100 solve times.
- 'avg12': Best average of 12 solve times.
- 'avg5': Best average of 5 solve times.
- 'best_single': Best single solve time.

## Getting Started
1. Create the 'speedcubes' database and tables by executing the 'create_tables.sql' script.
2. Populate the database with cube and time information using the 'populate_data.sql' script.

## Sample Queries
You can run SQL queries to retrieve, update, and manipulate data in the database.

### List all cubes
```
SELECT * FROM cubes;
```
### Rank cubes by the best average of 5 solves
```
SELECT cubes.name, times.avg5
FROM cubes
JOIN times ON cubes.id = times.cube_id
ORDER BY times.avg5
```
### List all cubes with a best single solve under 14 seconds in order
```
SELECT cubes.name, times.best_single
FROM cubes
JOIN times ON cubes.id = times.cube_id
WHERE times.best_single < 14
ORDER BY times.best_single;
```