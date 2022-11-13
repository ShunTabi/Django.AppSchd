CREATE TABLE T_MYBOOK(
BOOKID TEXT NOT NULL UNIQUE,
BOOKTITLE TEXT NOT NULL UNIQUE,
BOOKAUTHORS TEXT,
BOOKPUBLISHER TEXT,
BOOKPUBLISHEDDATE DATETIME,
BOOKPAGECOUNT INTEGER,
BOOKLANGUAGE INTEGER,
BOOKPREVIEWLINK TEXT,
BOOKINFOLINK TEXT,
BOOKUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE
);
CREATE TABLE T_DESCRIPTION(
BOOKID TEXT NOT NULL,
DESCROWID INTEGER NOT NULL,
DESCTEXT TEXT,
DESCUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
FOREIGN KEY(BOOKID) REFERENCES T_MYBOOK(BOOKID) ON DELETE CASCADE
);
