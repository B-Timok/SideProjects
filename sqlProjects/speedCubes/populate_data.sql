USE speedcubes;

-- Populate speedcube collection
INSERT INTO cubes (name, brand, release_year)
VALUES
    ('GAN 11', 'GAN', 2020),
    ('GAN 13', 'GAN', 2022),
    ('GAN Mini', 'GAN', 2020),
    ('GTS2M', 'MOYU', 2017),
    ('GTS3M', 'MOYU', 2018),
    ('GUHONG PRO', 'DAYAN', 2023),
    ('MGC EVO', 'YJ', 2022),
    ('SUPER RS3M', 'MOYU', 2023),
    ('TENGYUN V1', 'DAYAN', 2019),
    ('TENGYUN V2', 'DAYAN', 2020),
    ('TORNADO V2', 'X-MAN', 2021),
    ('TORNADO V3', 'X-MAN', 2022),
    ('VALK 3M', 'QIYI', 2017),
    ('WRM 2021', 'MOYU', 2021),
    ('WEILONG V9', 'MOYU', 2023),
    ('YS3M', 'MOYU', 2023),
    ('GAN 356 XS', 'GAN', 2019);

INSERT INTO times (cube_id, avg100, avg12, avg5, best_single)
VALUES
    (1, 19.970, 19.132, 17.516, 15.171),
    (2, 19.605, 18.304, 17.606, 15.772),
    (3, 19.312, 17.787, 16.485, 13.888),
    (4, 18.972, 17.810, 17.139, 14.222),
    (5, 19.599, 18.005, 17.167, 15.160),
    (6, 18.612, 17.855, 17.144, 14.003),
    (7, 20.000, 18.446, 17.305, 14.871),
    (8, 18.697, 17.368, 16.177, 14.572),
    (9, 19.993, 17.936, 17.687, 14.207),
    (10, 21.750, 20.339, 19.239, 16.006),
    (11, 19.810, 18.474, 17.639, 13.221),
    (12, 19.304, 18.043, 17.372, 13.227),
    (13, 19.707, 18.038, 17.778, 15.740),
    (14, 20.534, 19.861, 18.811, 14.622),
    (15, 19.055, 18.278, 16.965, 13.810),
    (16, 18.792, 17.873, 16.809, 15.338),
    (17, 20.913, 19.363, 18.653, 14.138);