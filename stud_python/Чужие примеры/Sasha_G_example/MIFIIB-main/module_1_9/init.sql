CREATE DATABASE IF NOT EXISTS instruments;
CREATE USER IF NOT EXISTS 'user'@'%' 
IDENTIFIED BY 'password';
GRANT SELECT,UPDATE,INSERT ON instruments.* TO 'user'@'%';
FLUSH PRIVILEGES;

USE instruments;

CREATE TABLE IF NOT EXISTS guitars (
    id INT(10) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    model VARCHAR(40) NOT NULL,
    PRIMARY KEY (ID)
  );
  
INSERT INTO guitars (id, brand, model) VALUES
('1', 'ADMIRA', 'ARTISTA'),
('2', 'TAYLOR', 'CE110'), 
('3', 'MARTIN', 'D28'),
('4', 'OVATION', 'ADAMAS');

