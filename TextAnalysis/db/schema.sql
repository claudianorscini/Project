CREATE TABLE document (
    Id       INT     PRIMARY KEY,
    raw_text TEXT,
    TITLE    CHAR,
    YEAR     INTEGER
);

CREATE TABLE Words_count (
    Id        INT,
    word      TEXT,
    frequency INT
);
