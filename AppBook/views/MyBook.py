from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime
import re


class MyBook:
    com = {
        "Com000": "100",
        "Com002": "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'",
    }
    sqls = {
        "MyBook001": f"SELECT * FROM T_MYBOOK LIMIT {com['Com000']}",
        "MyBook002": f"SELECT * FROM T_MYBOOK WHERE BOOKTITLE LIKE ? LIMIT {com['Com000']}",
        "MyBook003": f"SELECT * FROM T_DESCRIPTION WHERE BOOKID=? ORDER BY DESCROWID",
        "MyBook010": f"INSERT INTO T_MYBOOK(BOOKID,BOOKTITLE,BOOKAUTHORS,BOOKPUBLISHER,BOOKPUBLISHEDDATE,BOOKPAGECOUNT,BOOKLANGUAGE,BOOKPREVIEWLINK,BOOKINFOLINK,BOOKUPDATEDATE) VALUES(?,?,?,?,?,?,?,?,?,{com['Com002']})",
        "MyBook011": f"INSERT INTO T_DESCRIPTION(BOOKID,DESCROWID,DESCTEXT,DESCUPDATEDATE) VALUES(?,?,?,{com['Com002']})",
        "MyBook030": f"DELETE FROM T_MYBOOK WHERE BOOKID=?",
        "MyBook031": f"DELETE FROM T_DESCRIPTION WHERE BOOKID=?",
    }

    def MyBookSEARCH(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "ALL":
                sql = MyBook.sqls["MyBook001"]
                sqlParams = []
            elif KEYWORD != "":
                sql = MyBook.sqls["MyBook002"]
                sqlParams = [f"%{KEYWORD}%"]
            result = SQLFuns.SelectFun(sql, sqlParams)
            output = []
            for item in result:
                BOOKID = item["BOOKID"]
                sql = MyBook.sqls["MyBook003"]
                DESCRTEXT = SQLFuns.SelectFun(sql, [BOOKID])
                DESCRIPTION = ""
                for item2 in DESCRTEXT:
                    DESCRIPTION = DESCRIPTION + item2["DESCTEXT"]
                output.append(
                    {
                        "id": BOOKID,
                        "volumeInfo": {
                            "title": item["BOOKTITLE"],
                            "authors": item["BOOKAUTHORS"],
                            "publisher": item["BOOKPUBLISHER"],
                            "publisheddate": item["BOOKPUBLISHEDDATE"],
                            "description": DESCRIPTION,
                            "pageCount": item["BOOKPAGECOUNT"],
                            "language": item["BOOKLANGUAGE"],
                            "previewLink": item["BOOKPREVIEWLINK"],
                            "infoLink": item["BOOKINFOLINK"],
                        },
                    }
                )
            getData = {"items": output}
            return JsonResponse(getData)

    @csrf_exempt
    def MyBookINSERT(req):
        if req.method == "POST":
            MyBook.MyBookDELETE(req)
            sql = MyBook.sqls["MyBook010"]
            sqlParams = [
                req.POST["BOOKID"],
                req.POST["BOOKTITLE"],
                req.POST["BOOKAUTHORS"],
                req.POST["BOOKPUBLISHER"],
                req.POST["BOOKPUBLISHEDDATE"],
                req.POST["BOOKPAGECOUNT"],
                req.POST["BOOKLANGUAGE"],
                req.POST["BOOKPREVIEWLINK"],
                req.POST["BOOKINFOLINK"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            MyBook.MyBookINSERT2(req)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def MyBookDELETE(req):
        if req.method == "POST":
            sql = MyBook.sqls["MyBook031"]
            sqlParams = [req.POST["BOOKID"]]
            SQLFuns.DmlFun(sql, sqlParams)
            sql = MyBook.sqls["MyBook030"]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    def MyBookINSERT2(req):
        if req.method == "POST":
            sql = MyBook.sqls["MyBook011"]
            BOOKID = req.POST["BOOKID"]
            TARGETTEXT = req.POST["BOOKDESCRIPTION"]
            LEN = 45
            DESCTEXT = [TARGETTEXT[i : i + LEN] for i in range(0, len(TARGETTEXT), LEN)]
            for i in range(0, len(DESCTEXT)):
                sqlParams = [BOOKID, i + 1, DESCTEXT[i]]
                SQLFuns.DmlFun(sql, sqlParams)
