CREATE TABLE Author(
  name TEXT PRIMARY KEY,
  nationality TEXT,
  birthyear INTEGER
);
CREATE TABLE Patron(
  pid INTEGER PRIMARY KEY,
  name TEXT
);
CREATE TABLE Book(
  isbn INTEGER PRIMARY KEY,
  title TEXT,
  publisher TEXT,
  authorname TEXT REFERENCES Author(name)
);
CREATE TABLE Copy(
  cid INTEGER PRIMARY KEY,
  isbn INTEGER REFERENCES Book(isbn),
  patronid INTEGER REFERENCES Patron(pid)
);

