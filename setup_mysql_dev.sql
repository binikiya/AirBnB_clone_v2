-- prepares a MySQL server for the project
-- creates database with the name hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates user with the name ''hbnb_dev' and password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant SELECT privilege on database 'performance_schema' to user 'hbnb_dev'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
-- grant all privileges on database 'hbnb_dev_db' to user 'hbnb_dev'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- apply changes to database
FLUSH PRIVILEGES;
