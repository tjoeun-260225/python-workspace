CREATE TABLE IF NOT EXISTS users
(
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    email      VARCHAR(150) NOT NULL UNIQUE,
    phone      VARCHAR(30),
    job        VARCHAR(100),
    company    VARCHAR(100),
    city       VARCHAR(100),
    country    VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);