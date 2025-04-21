CREATE TABLE books (
    title VARCHAR(32),
    author VARCHAR(32),
    price INTEGER,
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY);

CREATE TABLE media (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    category VARCHAR(50) NOT NULL,
    title VARCHAR(200) NOT NULL,
    creator TEXT,
    publication_year VARCHAR(10),
    description_text TEXT
);

CREATE TABLE family (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(6) NOT NULL,
    age INTEGER,
    is_married BOOlEAN,
    city VARCHAR(6)
)