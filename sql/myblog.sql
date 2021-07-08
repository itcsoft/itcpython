
CREATE DATABASE itc_zaki_myblog;
USE itc_zaki_myblog;

-- ТАБЛИЦА ПОЛЬЗОВАТЕЛИ
-- ---------------------------------------
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
-- ---------------------------------------
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


	
-- ТАБЛИЦА КАТЕГОРИЯ СТАТЬЕЙ
-- ---------------------------------------
CREATE TABLE post_category(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(200) NULL,
	PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
INSERT INTO post_category(name)
    VALUES
        ('Economic'),
        ('Programming'),
        ('Python'),
        ('IT Engineer'),
        ('Bitcoin');

-- ТАБЛИЦА СТАТЬИ
-- ---------------------------------------
CREATE TABLE posts(
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NULL,
	title VARCHAR(200) NULL,
	content LONGTEXT NULL,
	short_content TEXT NULL,
	image_url TEXT NULL,
	PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;

-- Добавляем новую колонку для таблицы posts
ALTER TABLE posts
    ADD COLUMN post_category_id INT NULL;

    
-- ---------------------------------------
INSERT INTO posts(user_id, title, content, short_content, image_url)
    VALUES
        (
            1, 
            'Биткойн подоражал на 60 000$', 
            'Биткойн цифровая валюта для всех людей',
            'Биткойн всегда актуален',
            'bitcoin.png'
        ),
        (
            1, 
            'Садыр Жапаров', 
            'Садыр Жапаров Встретился с Путином',
            'Садыр Жапаров Встретился...',
            'politics.png'
        ),
        (
            1, 
            'Питон стал 1 языков прог-я мира', 
            'Питон стал самым популярным языков программирования на 2021 во всем мире',
            'Питон стал...',
            'python.png'
        ),
        (
            1, 
            'IT Инженеры начали хорошо зарабатывать', 
            'IT Инженеры начали зарабатывать 150 000$ в год',
            'IT Инженеры начали...',
            'engineer.png'
        ),
        (
            1, 
            'Экономика Кыргызстана растет', 
            'Кыргызстан стал лидером в Средней Азии по поставке Электрокаров',
            'Кыргызстан стал лидером...',
            'kyrgyzstan.png'
        );

-- ТАБЛИЦА МЕНЮ САЙТА
-- ---------------------------------------
CREATE TABLE menu(
	id INT NOT NULL AUTO_INCREMENT,
	menu_name VARCHAR(200) NULL,
	menu_url VARCHAR(200) NULL,
	PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
INSERT INTO menu(menu_name, menu_url)
    VALUES
        ('Главная', '/'),
        ('Статьи', '/posts'),
        ('Программирование', '/posts/programming'),
        ('О мне', '/about'),
        ('Контакты', '/contact');