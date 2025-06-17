CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

INSERT INTO Roster (Name, Species, Age) VALUES
('Бенджамин Сиско', 'Человек', 40),
('Джадзия Дакс', 'Трель', 300),
('Кира Нерис', 'баджорский', 29);

UPDATE Roster
SET Name = 'Эзри Дакс'
WHERE Name = 'Джадзия Дакс';

SELECT Name, Age
FROM Roster
WHERE Species = 'баджорский';

|     Name      | Age |
|---------------|-----|
| Кира Нерис    |  29 |

import sqlite3

# Создание и подключение к базе
conn = sqlite3.connect("roster.db")
cur = conn.cursor()

# Создание таблицы
cur.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Вставка данных
cur.executemany('''
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ('Бенджамин Сиско', 'Человек', 40),
    ('Джадзия Дакс', 'Трель', 300),
    ('Кира Нерис', 'баджорский', 29)
])

# Обновление
cur.execute('''
UPDATE Roster SET Name = 'Эзри Дакс' WHERE Name = 'Джадзия Дакс'
''')

# Выборка
cur.execute('''
SELECT Name, Age FROM Roster WHERE Species = 'баджорский'
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
