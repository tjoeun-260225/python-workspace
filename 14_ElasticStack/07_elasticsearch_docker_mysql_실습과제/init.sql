USE shopdb;
CREATE TABLE IF NOT EXISTS products
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(200)   NOT NULL,
    brand       VARCHAR(100)   NOT NULL,
    category    VARCHAR(100)   NOT NULL,
    description TEXT,
    price       DECIMAL(10, 2) NOT NULL,
    stock       INT            NOT NULL DEFAULT 0,
    rating      FLOAT,
    created_at  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;