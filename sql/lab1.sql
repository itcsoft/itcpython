-- показать все базы данных
show databases;

-- Создание базы данных
CREATE DATABASE itc_zakidev;

-- Удаление базы данных zakidev
DROP DATABASE itc_zakidev;

-- Выбираем базу данных
USE itc_zakidev;


-- Типы данных
-- VARCHAR Текстовый тип
-- BIT 1 же 0 деген санды алат (1 или 0)
-- TEXT 16 878 Количество макс. Символов
-- MEDIUMTEXT 64 6565 кол-сво символов
-- LONGTEXT 4GB размер текста
-- FLOAT болчок сан (дробное число)
-- DOUBLE ото чон болчок чан (оочень большое дробное число)
-- INT бутун сан (целое число)
-- BIGINT ото чон бутун сан (очень большое целое число) (можно разместить кол-во звезд внебе)


-- Создание Таблицы
CREATE TABLE users(
    name VARCHAR(250) NULL,
    login VARCHAR(100) NULL,
    password VARCHAR(300) NULL,
    address TEXT NULL DEFAULT NULL
) DEFAULT CHARSET=utf8mb4;

-- Создайние Таблицы products
CREATE TABLE products(
    name VARCHAR(250) NULL
) DEFAULT CHARSET=utf8mb4;

-- Создайние Таблицы balance
CREATE TABLE balance(
    bank_name VARCHAR(250) NULL,
    user_name VARCHAR(250) NULL,
    cash FLOAT NULL
) DEFAULT CHARSET=utf8mb4;


-- Удаление таблицы
DROP TABLE products;

-- Получение данных из таблицы users
SELECT name, login, password, address FROM users;

-- Получение данных из таблицы users по всем полям
SELECT * FROM users;

-- Вставка данных в таблицу
INSERT INTO users(name, login)
    VALUES('Zalkarbek', 'panda');

INSERT INTO users(name, login, password)
    VALUES('Meka', 'mekis', 'meka2000');

INSERT INTO users(name, login, password, address)
    VALUES('Beka', 'bekis', 'beka1999', 'OSH city');

INSERT INTO users(name, login, password, address)
    VALUES('Emir', 'ema', 'ema2001', 'Bishkek City');


-- Добавляем данные на таблицу balance
INSERT INTO balance(bank_name, user_name, cash)
    VALUES('Demir Bank', 'amantur', 89400.50);

-- LAB - 1
-- Выберите свою базу данных
-- Создайте таблицу country 
-- Поля
    -- name 
    -- valuta
    -- population_count 

-- Добавьте 5 стран
    -- Кыргызстан, Сом, 7000000
    -- Тажикстан, Сомони, 1400000
    -- Узбекстан, Сум, 2300000
    -- Китай, Юань, 15000000
    -- Америка, $,  75000000
CREATE TABLE country;

INSERT INTO country(name, valuta, population_count)
    VALUES
        ('Kyrgyzstan', 'KG', 7000000),
        ('Uzbekstan', 'KG', 23000000),
        ('America', 'KG', 9000000),
        ('England', 'KG', 8000000);


-- LAB - 2
-- Выберите свою базу данных
-- Создайте таблицу banks
-- Поля
    -- bank_name (Название банка)
    -- bank_balance (Сколько денег в банке)
    -- bank_info (Коротко о банке)
    -- clients_count (Количество клиентов)


-- Меняем кодировку таблицы на utf8
ALTER TABLE posts
    CHARACTER SET utf8mb4,
    COLLATE 'utf8mb4_general_ci';


-- Фильтрация получение данных
SELECT * FROM bank
    WHERE bank.bank_info = 'bad' AND bank.bank_info = 'very good';

-- Изменение данных в таблице
UPDATE
DELETE
ALTER


-- LAB 3
-- Создайте films таблицу у себя
-- Поля
    -- name VARCHAR(200)
    -- year INT
    -- status (хороший, плохой, нормальный, плохой)
    -- actors TEXT
    -- money INT
-- CREATE TABLE films(
--     name VARCHAR(200) NULL,
--     year INT NULL,
--     status VARCHAR(50),
--     actors TEXT NULL,
--     money INT
-- );
-- INSERT INTO