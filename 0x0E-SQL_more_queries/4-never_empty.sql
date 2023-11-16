-- Script that creates the table id_not_null on your MySQL server.
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (id INT SET DEFAULT 1, name VARCHAR(256));
