-- ===============================
-- DATABASE CREATION
-- ===============================
CREATE DATABASE IF NOT EXISTS 12A123;
USE 12A123;

-
-- TABLE: EASY

CREATE TABLE IF NOT EXISTS Easy (
    topic VARCHAR(50),
    ques TEXT,
    options TEXT,
    correct VARCHAR(10),
    trivia TEXT
);

-- 
-- TABLE: MEDIUM
-- 
CREATE TABLE IF NOT EXISTS Medium (
    topic VARCHAR(50),
    ques TEXT,
    options TEXT,
    correct VARCHAR(10),
    trivia TEXT
);

-- 
-- TABLE: HARD
--
CREATE TABLE IF NOT EXISTS Hard (
    topic VARCHAR(50),
    ques TEXT,
    options TEXT,
    correct VARCHAR(10),
    trivia TEXT
);


-- SAMPLE DATA FOR EASY

INSERT INTO Easy VALUES
('SCIENCE AND FUN','What is H2O?','A) Water B) Oxygen C) Hydrogen D) Helium','A','Water is essential for life'),
('MATHANGO','2+2 = ?','A) 3 B) 4 C) 5 D) 6','B','Basic arithmetic'),
('GENERAL KNOWLEDGE','Capital of India?','A) Mumbai B) Delhi C) Kolkata D) Chennai','B','New Delhi is capital of India'),
('HISTORY MYSTERY','Who discovered India?','A) Columbus B) Vasco da Gama C) Magellan D) Cook','B','Vasco da Gama reached India in 1498'),
('BOLLYWOOD BUFF','Who is known as King Khan?','A) Salman Khan B) Aamir Khan C) Shah Rukh Khan D) Saif Ali Khan','C','Shah Rukh Khan is called King Khan');


-- SAMPLE DATA FOR MEDIUM
-
INSERT INTO Medium VALUES
('SCIENCE AND FUN','What is CO2?','A) Oxygen B) Carbon Dioxide C) Nitrogen D) Hydrogen','B','CO2 is carbon dioxide'),
('MATHANGO','Square root of 144?','A) 10 B) 11 C) 12 D) 13','C','12*12 = 144'),
('GENERAL KNOWLEDGE','Largest planet?','A) Earth B) Mars C) Jupiter D) Saturn','C','Jupiter is the largest planet'),
('HISTORY MYSTERY','Who was first PM of India?','A) Gandhi B) Nehru C) Patel D) Bose','B','Jawaharlal Nehru'),
('BOLLYWOOD BUFF','First Bollywood movie?','A) Mughal-e-Azam B) Raja Harishchandra C) Sholay D) DDLJ','B','First Indian movie');


-- SAMPLE DATA FOR HARD

INSERT INTO Hard VALUES
('SCIENCE AND FUN','Speed of light?','A) 3x10^8 m/s B) 5x10^6 m/s C) 1x10^3 m/s D) 9x10^9 m/s','A','Physics constant'),
('MATHANGO','Derivative of x^2?','A) x B) 2x C) x^2 D) 1','B','Basic calculus'),
('GENERAL KNOWLEDGE','UN Headquarters located in?','A) Paris B) London C) New York D) Geneva','C','Located in New York'),
('HISTORY MYSTERY','Year of French Revolution?','A) 1789 B) 1776 C) 1857 D) 1914','A','Started in 1789'),
('BOLLYWOOD BUFF','Director of Inception?','A) Nolan B) Spielberg C) Cameron D) Scorsese','A','Christopher Nolan');