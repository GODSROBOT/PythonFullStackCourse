-- 1 NF
CREATE TABLE ex (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

-- 2 NF
CREATE TABLE tx (
    id INT PRIMARY KEY,
    ex_id INT,
    amount DECIMAL(10, 2),
    FOREIGN KEY (ex_id) REFERENCES ex(id)
);

-- 3 NF
CREATE TABLE tz (
    id INT PRIMARY KEY,
    tx_id INT,
    description VARCHAR(255),
    FOREIGN KEY (tx_id) REFERENCES tx(id)
);

-- BCNF
CREATE TABLE ta (
    id INT PRIMARY KEY,
    tz_id INT,
    info VARCHAR(255),
    FOREIGN KEY (tz_id) REFERENCES tz(id)
);
