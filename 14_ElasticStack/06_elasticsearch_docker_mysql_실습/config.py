import os

MYSQL = {
    "host":     "localhost",
    "port":     3307,
    "user":     "shopuser",
    "password": "shoppassword",
    "database": "shopdb",
    "charset":  "utf8mb4",
}

ES_HOST    = "http://localhost:9200"
ES_INDEX   = "products"
TOTAL      = 500_000
BATCH_SIZE = 5_000


