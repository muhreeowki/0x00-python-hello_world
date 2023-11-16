-- Script that creates the MySQL server user user_0d_1.
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'NewPassword';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
