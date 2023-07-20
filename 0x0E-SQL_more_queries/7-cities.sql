--  creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCEs hbtn_0d_usa.states(id)
);