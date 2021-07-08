-- Создание базы данных
CREATE DATABASE itc_amantur;
USE itc_amantur;

-- ОЧИСТИТЬ ТАБЛИЦУ
TRUNCATE TABLE users;

-- создание базы данных для блога --
-- TABLE users
CREATE TABLE users(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(200) NULL,
	login VARCHAR(200) NULL,
	password VARCHAR(300) NULL,
	is_admin BIT NULL,
    PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;

INSERT INTO users(name, login, password, is_admin)
    VALUES
        ('Zalkar', 'zalkar', '123', 1),
        ('Meerim', 'meka', '123456', 0),
        ('Aiganysh', 'aika', '123456', 0),
        ('Bekbolot', 'beka', '9601', 0),
        ('Amantur', 'amantur', '4513', 0),
        ('Emir', 'ema', '5354', 0),
        ('Bekzat', 'bekzat', '4502', 0),
        ('Nurmuhammed', 'nur', '1210', 0),
        ('Iskender', 'iskender', '5656', 1);

-- Удаление записей
DELETE FROM users WHERE id IN(10, 12, 14);
DELETE FROM users WHERE login = 'aika';
DELETE FROM users WHERE id = 9;
DELETE FROM users WHERE id BETWEEN 13 AND 19;

-- Обновление записей
UPDATE users 
    SET 
        name = 'Anonymous',
        login = 'anon',
        password = '1111'
    WHERE id BETWEEN 20 AND 24;

-- Обновление записей
UPDATE users 
    SET 
        name = 'Hacker',
        login = 'hacker',
        password = 'hack'
    WHERE name = 'Anonymous';

INSERT INTO customers(customerNumber, customerName, country)
    VALUES
        (7777, 'Zalkarbek', 'Kyrgyzstan');

UPDATE customers
    SET
        customerName = 'Hack'
    WHERE customerNumber > 500;
