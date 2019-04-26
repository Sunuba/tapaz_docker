CREATE DATABASE IF NOT EXISTS tapaz;
-- The system will work without the line below as well
GRANT ALL PRIVILEGES ON tapaz.* TO 'root'@'localhost';
GRANT ALL PRIVILEGES ON tapaz.* TO 'tapaz'@'localhost';
ALTER USER root IDENTIFIED WITH mysql_native_password BY 'password';
ALTER USER tapaz IDENTIFIED WITH mysql_native_password BY 'password';