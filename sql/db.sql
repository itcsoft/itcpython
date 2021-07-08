CREATE DATABASE itc_bootcamp;

USE itc_bootcamp;

CREATE TABlE users(
    name TEXT NULL DEFAULT NULL
);

INSERT INTO users(name) VALUES('bootcamp');

SELECT * FROM users;