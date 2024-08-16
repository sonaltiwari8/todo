CREATE DATABASE todoapp;
USE todoapp;

CREATE TABLE todos(
    id INT PRIMARY KEY AUTO_INCREMENT,  
    todo_name VARCHAR(255) NOT NULL UNIQUE,
    priority_level ENUM('high','medium', 'low') DEFAULT 'low',
    deadline_date DATE NOT NULL,
    deadline_time TIME NOT NULL,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);