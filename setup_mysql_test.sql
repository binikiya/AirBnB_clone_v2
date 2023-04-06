-- prepares mysql database for a project
-- create project test database with the name 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user with the name 'hbnb_test' and password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant select privilege on database 'performance_schema' to user 'hbnb_test'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
-- apply changes to database
FLUSH PRIVILEGES;
-- grant all privileges on database 'hbnb_test_db' to user 'hbnb_test'
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- apply changes to database
FLUSH PRIVILEGES;
