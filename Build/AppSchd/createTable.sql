CREATE TABLE T_PRIOR(
PRIORID INTEGER PRIMARY KEY AUTOINCREMENT,
PRIORNAME TEXT NOT NULL UNIQUE,
PRIORSUBNAME TEXT NOT NULL UNIQUE,
PRIORVISIBLESTATUS INTEGER NOT NULL DEFAULT 1
);
CREATE TABLE T_STATUS(
STATUSID INTEGER PRIMARY KEY AUTOINCREMENT,
STATUSNAME TEXT NOT NULL UNIQUE,
STATUSSUBNAME TEXT NOT NULL UNIQUE,
STATUSVISIBLESTATUS INTEGER NOT NULL DEFAULT 1
);
CREATE TABLE T_GENRE (
GENREID INTEGER PRIMARY KEY AUTOINCREMENT,
GENRENAME TEXT NOT NULL UNIQUE,
GENREUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
GENREVISIBLESTATUS INTEGER NOT NULL DEFAULT 1
);
CREATE TABLE T_GOAL (
GOALID INTEGER PRIMARY KEY AUTOINCREMENT,
GENREID INTEGER NOT NULL,
GOALNAME TEXT NOT NULL UNIQUE,
GOALUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
GOALVISIBLESTATUS INTEGER NOT NULL DEFAULT 1,
UNIQUE(GENREID,GOALNAME),
FOREIGN KEY(GENREID) REFERENCES T_GENRE(GENREID) ON DELETE CASCADE
);
CREATE TABLE T_PLAN (
PLANID INTEGER PRIMARY KEY AUTOINCREMENT,
GOALID INTEGER NOT NULL,
PLANNAME TEXT NOT NULL,
PRIORID INTEGER NOT NULL,
STATUSID INTEGER NOT NULL DEFAULT 2,
PLANSTARTDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
PLANENDDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
PLANUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
PLANVISIBLESTATUS INTEGER NOT NULL DEFAULT 1,
UNIQUE(GOALID,PLANNAME),
FOREIGN KEY(GOALID) REFERENCES T_GOAL(GOALID) ON DELETE CASCADE
);
CREATE TABLE T_TODO (
TODOID INTEGER PRIMARY KEY AUTOINCREMENT,
PLANID INTEGER NOT NULL,
TODONAME TEXT NOT NULL,
STATUSID INTEGER NOT NULL DEFAULT 2,
TODOENDDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
TODOVISIBLESTATUS INTEGER NOT NULL DEFAULT 1,
TODOUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
UNIQUE(PLANID,TODONAME),
FOREIGN KEY(PLANID) REFERENCES T_PLAN(PLANID) ON DELETE CASCADE
);
CREATE TABLE T_SCHEDULE (
SCHEDULEID INTEGER PRIMARY KEY AUTOINCREMENT,
PLANID INTEGER NOT NULL,
STATUSID INTEGER NOT NULL DEFAULT 2,
SCHEDULEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
SCHEDULESTARTTIME DATETIME NOT NULL DEFAULT CURRENT_DATE,
SCHEDULEENDTIME DATETIME NOT NULL DEFAULT CURRENT_DATE,
SCHEDULEHOURS REAL NOT NULL,
SCHEDULELOCATION INTEGER NOT NULL,
SCHEDULEHEIGHT INTEGER NOT NULL,
SCHEDULEVISIBLESTATUS INTEGER NOT NULL DEFAULT 1,
SCHEDULEUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE,
FOREIGN KEY(PLANID) REFERENCES T_PLAN(PLANID) ON DELETE CASCADE,
UNIQUE(SCHEDULEDATE,SCHEDULESTARTTIME,SCHEDULEENDTIME,PLANID)
);
CREATE TABLE T_ANALYSISDATA(
ANALYSISDATE DATETIME NOT NULL,
ANALYSISITEMID NOT NULL,
ANALYSISITEMNAME NOT NULL,
ANALYSISREMARKS TEXT,
ANALYSISUPDATEDATE DATETIME NOT NULL DEFAULT CURRENT_DATE
);