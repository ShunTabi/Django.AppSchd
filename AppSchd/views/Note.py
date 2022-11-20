from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class Note:
    SQLLimit = "500"
    now = "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'"
    sqls = {
        "Note000": ""
        + "SELECT NOTETITLEID,SOURCEID,KINDID,'★最新' AS NOTEVERSION,NOTETITLE,NOTETEXT,strftime('%Y-%m-%d',NOTEDATE) AS NOTEDATE,ROWID,FIN FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) WHERE T_NOTETITLE.NOTEVERSION = '0' AND NOTEDATE IN (SELECT NOTEDATE FROM T_NOTETITLE WHERE NOTEVERSION='0' GROUP BY strftime('%Y-%m-%d', NOTEDATE) HAVING NOTEDATE<=:NOTEDATE ORDER BY NOTEDATE DESC LIMIT 2) ORDER BY NOTEDATE ASC,NOTETITLEID,ROWID",
        "Note001": ""
        + "SELECT NOTETITLEID,SOURCEID,KINDID,CASE WHEN T_NOTETITLE.NOTEVERSION='0' THEN '★最新' ELSE T_NOTETITLE.NOTEVERSION END AS NOTEVERSION,NOTETITLE,NOTETEXT,strftime('%Y-%m-%d',NOTEDATE) AS NOTEDATE,ROWID,FIN FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) WHERE NOTEDATE IN (SELECT NOTEDATE FROM T_NOTETITLE GROUP BY strftime('%Y-%m-%d', NOTEDATE) HAVING NOTEDATE<=:NOTEDATE ORDER BY NOTEDATE DESC LIMIT 2) ORDER BY NOTEDATE ASC,NOTETITLEID,ROWID",
        "Note002": ""
        + f"SELECT NOTETITLEID,SOURCEID,KINDID,'★最新' AS NOTEVERSION,CASE WHEN NOTETYPE='0' THEN '【ノート】' WHEN NOTETYPE='1' THEN '【履歴】' END AS NOTETYPE,NOTETITLE,NOTETEXT,strftime('%Y-%m-%d',NOTEDATE) AS NOTEDATE,ROWID,FIN FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) WHERE T_NOTETITLE.NOTEVERSION = '0' ORDER BY NOTEDATE DESC,NOTETITLEID,ROWID LIMIT {SQLLimit}",
        "Note003": ""
        + f"SELECT NOTETITLEID,SOURCEID,KINDID,'★最新' AS NOTEVERSION,CASE WHEN NOTETYPE='0' THEN '【ノート】' WHEN NOTETYPE='1' THEN '【履歴】' END AS NOTETYPE,NOTETITLE,NOTETEXT,strftime('%Y-%m-%d',NOTEDATE) AS NOTEDATE,ROWID,FIN FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) WHERE T_NOTETITLE.NOTEVERSION = '0' AND NOTETITLEID IN (SELECT DISTINCT NOTETITLEID FROM T_NOTETEXT WHERE NOTETEXT LIKE @KEYWORD) ORDER BY NOTEDATE DESC,NOTETITLEID,ROWID LIMIT {SQLLimit}",
        "Note004": ""
        + f"SELECT NOTETITLEID,SOURCEID,KINDID,CASE WHEN T_NOTETITLE.NOTEVERSION='0' THEN '★最新' ELSE T_NOTETITLE.NOTEVERSION END AS NOTEVERSION,CASE WHEN NOTETYPE='0' THEN '【ノート】' WHEN NOTETYPE='1' THEN '【履歴】' END AS NOTETYPE,NOTETITLE,NOTETEXT,strftime('%Y-%m-%d',NOTEDATE) AS NOTEDATE,ROWID,FIN FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) ORDER BY NOTEDATE DESC,NOTETITLEID,ROWID LIMIT {SQLLimit}",
        "Note005": ""
        + f"SELECT NOTETITLEID,SOURCEID,KINDID,CASE WHEN T_NOTETITLE.NOTEVERSION='0' THEN '★最新' ELSE T_NOTETITLE.NOTEVERSION END AS NOTEVERSION,CASE WHEN NOTETYPE='0' THEN '【ノート】' WHEN NOTETYPE='1' THEN '【履歴】' END AS NOTETYPE,NOTETITLE,NOTETEXT,strftime('%Y-%m-%d',NOTEDATE) AS NOTEDATE,ROWID,FIN FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) WHERE NOTETITLEID IN (SELECT DISTINCT NOTETITLEID FROM T_NOTETEXT WHERE NOTETEXT LIKE @KEYWORD) ORDER BY NOTEDATE DESC,NOTETITLEID,ROWID LIMIT {SQLLimit}",
        # "Note006": ""
        # + "SELECT * FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) WHERE NOTETITLE=@NOTETITLE AND NOTEDATE LIKE @NOTEDATE",
        # "Note007": ""
        # + "SELECT NOTEDATE,NOTETITLE,NOTETEXT,ROWID,FIN FROM T_NOTETITLE INNER JOIN T_NOTETEXT USING (NOTETITLEID) WHERE T_NOTETITLE.NOTEVERSION = 0 AND (SOURCEID=@NOTETITLEID OR NOTETITLEID=@NOTETITLEID) ORDER BY ROWID",
        "Note008": ""
        + "SELECT * FROM T_NOTETITLE WHERE (SOURCEID=@SOURCEID OR NOTETITLEID=@SOURCEID) AND NOTEDATE LIKE @NOTEDATE",
        "Note010": ""
        + f"INSERT INTO T_NOTETITLE(SOURCEID,KINDID,NOTETITLE,NOTETYPE,NOTEVERSION,NOTEDATE,NOTEFIRSTDATE,NOTEUPDATEDATE) VALUES(:SOURCEID,:KINDID,:NOTETITLE,:NOTETYPE,'0',:NOTEDATE,{now},{now})",
        "Note011": ""
        + f"INSERT INTO T_NOTETEXT(NOTETITLEID,ROWID,NOTETEXT,FIN) VALUES((SELECT NOTETITLEID FROM T_NOTETITLE WHERE NOTETITLE=:NOTETITLE AND NOTEDATE LIKE :NOTEDATE),:ROWID,:NOTETEXT,:FIN)",
        "Note020": ""
        + f"UPDATE T_NOTETITLE SET NOTEVERSION=(SELECT COUNT(NOTEVERSION) FROM T_NOTETITLE WHERE NOTETITLEID=:SOURCEID OR SOURCEID=:SOURCEID),SOURCEID=:SOURCEID,NOTETITLE=:NOTETITLE,NOTEUPDATEDATE={now} WHERE NOTETITLEID=:NOTETITLEID",
        "Note021": ""
        + f"UPDATE T_NOTETITLE SET NOTETITLE=:NOTETITLE,NOTEUPDATEDATE={now} WHERE NOTETITLEID=:NOTETITLEID",
        "Note030": "" + "DELETE FROM T_NOTETEXT WHERE NOTETITLEID=:NOTETITLEID",
    }

    def NoteRecord(req):
        if req.method == "GET":
            DATE = f"{req.GET['NOTEDATE']} 23:59:59"
            LEVEL = req.GET["LEVEL"]
            items = []
            if LEVEL == "1":
                items = SQLFuns.SelectFun(Note.sqls["Note000"], {"NOTEDATE": DATE})
            elif LEVEL == "0":
                items = SQLFuns.SelectFun(Note.sqls["Note001"], {"NOTEDATE": DATE})
            mainBox = []
            NOTETITLEID = ""
            SOURCEID = ""
            NOTETITLE = ""
            NOTETEXT = ""
            NOTEDATE = ""
            NOTEVERSION = ""
            for index in range(len(items)):
                if items[index]["ROWID"] == 1:
                    NOTETITLEID = items[index]["NOTETITLEID"]
                    SOURCEID = items[index]["SOURCEID"]
                    NOTETITLE = items[index]["NOTETITLE"]
                    NOTETEXT = items[index]["NOTETEXT"]
                    NOTEDATE = items[index]["NOTEDATE"]
                    NOTEVERSION = items[index]["NOTEVERSION"]
                else:
                    NOTETEXT += items[index]["NOTETEXT"]
                if items[index]["FIN"] == 1:
                    mainBox.append(
                        {
                            "NOTETITLEID": NOTETITLEID,
                            "SOURCEID": SOURCEID,
                            "NOTETITLE": NOTETITLE,
                            "NOTETEXT": NOTETEXT,
                            "NOTEFULLTEXT": f"【{NOTETITLE}】\n{NOTETEXT}",
                            "NOTEDATE": NOTEDATE,
                            "NOTEVERSION": NOTEVERSION,
                        }
                    )
                    NOTETEXT = ""
            getData = {"getData": mainBox}
            return JsonResponse(getData)

    def NoteList(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            LEVEL = req.GET["LEVEL"]
            items = []
            if LEVEL == "1":
                if KEYWORD == "":
                    items = SQLFuns.SelectFun(Note.sqls["Note002"], {})
                elif KEYWORD != "":
                    items = SQLFuns.SelectFun(
                        Note.sqls["Note003"], {"KEYWORD": f"%{KEYWORD}%"}
                    )
            elif LEVEL == "0":
                if KEYWORD == "":
                    items = SQLFuns.SelectFun(Note.sqls["Note004"], {})
                elif KEYWORD != "":
                    items = SQLFuns.SelectFun(
                        Note.sqls["Note005"], {"KEYWORD": f"%{KEYWORD}%"}
                    )
            mainBox = []
            NOTETITLEID = ""
            SOURCEID = ""
            NOTETITLE = ""
            NOTETEXT = ""
            NOTETYPE = ""
            NOTEDATE = ""
            NOTEVERSION = ""
            for index in range(len(items)):
                if items[index]["ROWID"] == 1:
                    NOTETITLEID = items[index]["NOTETITLEID"]
                    SOURCEID = items[index]["SOURCEID"]
                    NOTETITLE = items[index]["NOTETITLE"]
                    NOTETYPE = items[index]["NOTETYPE"]
                    NOTETEXT = items[index]["NOTETEXT"]
                    NOTEDATE = items[index]["NOTEDATE"]
                    NOTEVERSION = items[index]["NOTEVERSION"]
                else:
                    NOTETEXT += items[index]["NOTETEXT"]
                if items[index]["FIN"] == 1:
                    mainBox.append(
                        {
                            "NOTETITLEID": NOTETITLEID,
                            "SOURCEID": SOURCEID,
                            "NOTETITLE": NOTETITLE,
                            "NOTEINFO": f"VER：{NOTEVERSION}\nタイトル：{NOTETITLE}\n種類：{NOTETYPE}\n日付：{NOTEDATE}",
                            "NOTETEXT": NOTETEXT,
                            "NOTEDATE": NOTEDATE,
                            "NOTEVERSION": NOTEVERSION,
                        }
                    )
                    NOTETEXT = ""
            getData = {"getData": mainBox}
            return JsonResponse(getData)

    @csrf_exempt
    def NoteINSERT(req):
        if req.method == "POST":
            sqls = []
            params = []
            NOTETITLE = req.POST["NOTETITLE"]
            NOTETEXT = req.POST["NOTETEXT"]
            NOTEDATE = req.POST["NOTEDATE"]
            sqls.append(Note.sqls["Note010"])
            params.append(
                {
                    "SOURCEID": req.POST["SOURCEID"],
                    "KINDID": req.POST["KINDID"],
                    "NOTETITLE": NOTETITLE,
                    "NOTETYPE": req.POST["NOTETYPE"],
                    "NOTEDATE": NOTEDATE,
                }
            )
            NOTETEXTS = [NOTETEXT[x : x + 70] for x in range(0, len(NOTETEXT), 70)]
            for index in range(len(NOTETEXTS)):
                FIN = 0
                if index == len(NOTETEXTS) - 1:
                    FIN = 1
                sqls.append(Note.sqls["Note011"])
                params.append(
                    {
                        "NOTETITLE": NOTETITLE,
                        "NOTEDATE": NOTEDATE,
                        "ROWID": index + 1,
                        "NOTETEXT": NOTETEXTS[index],
                        "FIN": FIN,
                    }
                )
            SQLFuns.DmlFun2(sqls, params)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def NoteUPDATE(req):
        if req.method == "POST":
            sqls = []
            params = []
            NOTETITLEID = req.POST["NOTETITLEID"]
            NOTETITLE = req.POST["NOTETITLE"]
            NOTETEXT = req.POST["NOTETEXT"]
            NOTEDATE = req.POST["NOTEDATE"]
            thisSOURCEID = req.POST["SOURCEID"]
            if thisSOURCEID == "0":
                thisSOURCEID = NOTETITLEID
            checkBox = SQLFuns.SelectFun(
                Note.sqls["Note008"],
                {
                    "SOURCEID": thisSOURCEID,
                    "NOTETITLEID": thisSOURCEID,
                    "NOTEDATE": f"{NOTEDATE}%",
                },
            )
            if len(checkBox) > 0:
                sqls.append(Note.sqls["Note021"])
                sqls.append(Note.sqls["Note030"])
                params.append({"NOTETITLE": NOTETITLE, "NOTETITLEID": NOTETITLEID})
                params.append({"NOTETITLEID": NOTETITLEID})
            elif len(checkBox) == 0:
                sqls.append(Note.sqls["Note020"])
                sqls.append(Note.sqls["Note010"])
                params.append(
                    {
                        "SOURCEID": thisSOURCEID,
                        "NOTETITLE": NOTETITLE,
                        "NOTETITLEID": NOTETITLEID,
                    }
                )
                params.append(
                    {
                        "SOURCEID": thisSOURCEID,
                        "KINDID": req.POST["KINDID"],
                        "NOTETITLE": NOTETITLE,
                        "NOTETYPE": req.POST["NOTETYPE"],
                        "NOTEDATE": NOTEDATE,
                    }
                )
            NOTETEXTS = [NOTETEXT[x : x + 70] for x in range(0, len(NOTETEXT), 70)]
            for index in range(len(NOTETEXTS)):
                FIN = 0
                if index == len(NOTETEXTS) - 1:
                    FIN = 1
                sqls.append(Note.sqls["Note011"])
                params.append(
                    {
                        "NOTETITLE": NOTETITLE,
                        "NOTEDATE": NOTEDATE,
                        "ROWID": index + 1,
                        "NOTETEXT": NOTETEXTS[index],
                        "FIN": FIN,
                    }
                )
            SQLFuns.DmlFun2(sqls, params)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
