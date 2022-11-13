import sqlite3


class SQLFuns:
    dbname = "db/AppNote/AppNote.db"

    def RemakeDict(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def SelectFun(sql, params):
        mainOutput = []
        conn = sqlite3.connect(SQLFuns.dbname)
        cur = conn.cursor()
        try:
            cur.execute(sql, params)
            rows = cur.fetchall()
            for item in rows:
                subOutput = {}
                for idx, col in enumerate(cur.description):
                    subOutput[col[0]] = item[idx]
                mainOutput.append(subOutput)
            # print(mainOutput)
        finally:
            cur.close()
            conn.close()
        return mainOutput

    def DmlFun(sql, params):
        print("-----------------------------------------------")
        print(sql)
        print(params)
        print("-----------------------------------------------")
        conn = sqlite3.connect(SQLFuns.dbname)
        cur = conn.cursor()
        cur.execute(sql, params)
        cur.close()
        conn.commit()
        conn.close()
