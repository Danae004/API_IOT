CREATE TABLE iot(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo TEXT,
    valor INTEGER
);

INSERT INTO iot (id, dispositivo, valor)
VALUES (1, 'led', 1);

INSERT INTO iot (id, dispositivo, valor)
VALUES (2, 'potenciometro', 500);
