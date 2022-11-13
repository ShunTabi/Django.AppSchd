from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime, timedelta
import re


class Note:
    def getNow():
        return "'" + now + "'"

    com = {
        "Com000": "100",
    }
    sqls = {
        "Note000": f"SELECT NOTEID,NOTEDATE,NOTEFIRSTDATE,NOTEUPDATEDATE FROM T_NOTE WHERE NOTEDATE LIKE ? ORDER BY NOTEDATE ASC",
        "Note001": f"SELECT NOTETEXT FROM T_NOTETEXT WHERE NOTEGENERATIONID='999999' AND NOTEID=?",
        "Note010": f"INSERT INTO T_NOTE(NOTEDATE,NOTEFIRSTDATE,NOTEUPDATEDATE) VALUES(?,?,?)",
        "Note011": f"INSERT INTO T_NOTETEXT(NOTEID,NOTEROWID,NOTETEXT) VALUES((SELECT NOTEID FROM T_NOTE WHERE NOTEDATE=?),?,?)",
    }

    def NoteSELECT(req):
        if req.method == "GET":
            STARTDATE = req.GET["DATE1"]
            TARGETDATE = req.GET["DATE2"]
            params = []
            sql = Note.sqls["Note000"]
            while STARTDATE <= TARGETDATE:
                sqlParams = [f"%{TARGETDATE}%"]
                DATA1 = SQLFuns.SelectFun(sql, sqlParams)
                params2 = []
                for item in DATA1:
                    sql2 = Note.sqls["Note001"]
                    DATA2 = SQLFuns.SelectFun(sql2, [item["NOTEID"]])
                    NOTETEXT = ""
                    for item2 in DATA2:
                        NOTETEXT = NOTETEXT + item2["NOTETEXT"]
                        # print(NOTETEXT)
                    params2.append(
                        {
                            "NOTEID": item["NOTEID"],
                            "NOTEDATE": item["NOTEDATE"],
                            "NOTEFIRSTDATE": item["NOTEFIRSTDATE"],
                            "NOTEUPDATEDATE": item["NOTEUPDATEDATE"],
                            "NOTETEXT": NOTETEXT,
                        }
                    )
                params.append({"NOTEDATE": TARGETDATE, "NOTES": params2})
                TARGETDATE = datetime.strftime(
                    datetime.strptime(TARGETDATE, "%Y-%m-%d") + timedelta(days=-1),
                    "%Y-%m-%d",
                )
            return JsonResponse({"getData": params})

    @csrf_exempt
    def NoteINSERT(req):
        if req.method == "POST":
            sql = Note.sqls["Note010"]
            sqlParams = [
                req.POST["NOTEDATE"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            Note.NoteINSERT2(req)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    def NoteINSERT2(req):
        if req.method == "POST":
            sql = Note.sqls["Note011"]
            NOTEDATE = req.POST["NOTEDATE"]
            NOTE = req.POST["NOTE"]
            LEN = 40
            NOTETEXT = [NOTE[i : i + LEN] for i in range(0, len(NOTE), LEN)]
            for i in range(0, len(NOTETEXT)):
                sqlParams = [NOTEDATE, i + 1, NOTETEXT[i]]
                SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
