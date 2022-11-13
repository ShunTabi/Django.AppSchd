import sqlite3


class SQLFuns:
    dbname = "E:/03.C#/01.AppSchd/AppSchd/AppSchd/bin/Debug/resources/db/AppSchd.db"
    # dbname = "D:/Tools/AppSchd/resources/db/AppSchd.db"

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
        conn = sqlite3.connect(SQLFuns.dbname)
        cur = conn.cursor()
        cur.execute(sql, params)
        print("-----------------------------------------------")
        print(sql)
        print(params)
        print("-----------------------------------------------")
        cur.close()
        conn.commit()
        conn.close()

    def DmlFun2(sql, params):
        conn = sqlite3.connect(SQLFuns.dbname)
        cur = conn.cursor()
        for i in range(len(sql)):
            cur.execute(sql[i], params[i])
            print("-----------------------------------------------")
            print(sql[i])
            print(params[i])
            print("-----------------------------------------------")
        cur.close()
        conn.commit()
        conn.close()
