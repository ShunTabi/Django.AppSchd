from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class Record:
    com = {
        "Com000": "100",
        "Com002": "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'",
    }
    sqls = {
        "RecordGenre000": f"SELECT GENREID,GENRENAME,strftime('%Y-%m-%d',GENREUPDATEDATE) AS GENREUPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS = ? LIMIT {com['Com000']}",
        "RecordGenre001": f"SELECT GENREID,GENRENAME,strftime('%Y-%m-%d',GENREUPDATEDATE) AS GENREUPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS = ? AND GENRENAME LIKE ? LIMIT {com['Com000']}",
        "RecordGenre002": f"SELECT GENREID AS ID,GENRENAME AS NAME FROM T_GENRE WHERE GENREVISIBLESTATUS = ?",
        "RecordGenre010": f"INSERT INTO T_GENRE(GENRENAME,GENREUPDATEDATE) VALUES(?,{com['Com002']})",
        "RecordGenre020": f"UPDATE T_GENRE SET GENRENAME=?,GENREUPDATEDATE={com['Com002']} WHERE GENREID=?",
        "RecordGoal000": f"SELECT GOALID,GENREID,GENRENAME,GOALNAME,strftime('%Y-%m-%d',GOALUPDATEDATE) AS GOALUPDATEDATE FROM T_GOAL INNER JOIN T_GENRE USING(GENREID) WHERE GENREVISIBLESTATUS = ? AND GOALVISIBLESTATUS = ? LIMIT  {com['Com000']}",
        "RecordGoal001": f"SELECT GOALID,GENREID,GENRENAME,GOALNAME,strftime('%Y-%m-%d',GOALUPDATEDATE) AS GOALUPDATEDATE FROM T_GOAL INNER JOIN T_GENRE USING(GENREID) WHERE GENREVISIBLESTATUS = ? AND GOALVISIBLESTATUS = ? AND GOALNAME LIKE ? LIMIT  {com['Com000']}",
        "RecordGoal010": f"INSERT INTO T_GOAL(GENREID,GOALNAME,GOALUPDATEDATE) VALUES(?,?,{com['Com002']})",
        "RecordGoal020": f"UPDATE T_GOAL SET GENREID=?,GOALNAME=?,GOALUPDATEDATE={com['Com002']} WHERE GOALID=?",
        "RecordGoal002": f"SELECT GOALID AS ID,GOALNAME AS NAME FROM T_GOAL INNER JOIN T_GENRE USING(GENREID) WHERE GENREVISIBLESTATUS = ? AND GOALVISIBLESTATUS = ? ",
        "RecordPlan000": f"SELECT PLANID,GOALID,GOALNAME,PLANNAME,PRIORID,PRIORNAME,PRIORSUBNAME,strftime('%Y-%m-%d',PLANSTARTDATE) AS PLANSTARTDATE,strftime('%Y-%m-%d',PLANENDDATE) AS PLANENDDATE,strftime('%Y-%m-%d',PLANUPDATEDATE) AS PLANUPDATEDATE FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_PRIOR USING(PRIORID) WHERE GOALVISIBLESTATUS = ? AND PLANVISIBLESTATUS = ? AND PRIORVISIBLESTATUS = ? LIMIT  {com['Com000']}",
        "RecordPlan001": f"SELECT PLANID,GOALID,GOALNAME,PLANNAME,PRIORID,PRIORNAME,PRIORSUBNAME,strftime('%Y-%m-%d',PLANSTARTDATE) AS PLANSTARTDATE,strftime('%Y-%m-%d',PLANENDDATE) AS PLANENDDATE,strftime('%Y-%m-%d',PLANUPDATEDATE) AS PLANUPDATEDATE FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_PRIOR USING(PRIORID) WHERE GOALVISIBLESTATUS = ? AND PLANVISIBLESTATUS = ? AND PRIORVISIBLESTATUS = ? AND (GOALNAME LIKE ? OR PLANNAME LIKE ?) LIMIT  {com['Com000']}",
        "RecordPlan002": f"SELECT PLANID AS ID,PLANNAME AS NAME FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_GENRE USING(GENREID) INNER JOIN T_PRIOR USING(PRIORID) WHERE GENREVISIBLESTATUS = ? AND GOALVISIBLESTATUS = ? AND PLANVISIBLESTATUS = ? AND PRIORVISIBLESTATUS = ? AND GOALID = ?",
        "RecordPlan010": f"INSERT INTO T_PLAN(GOALID,PLANNAME,PRIORID,PLANSTARTDATE,PLANENDDATE,PLANUPDATEDATE) VALUES(?,?,?,strftime('%Y-%m-%d 00:00:00',?),strftime('%Y-%m-%d 00:00:00',?),{com['Com002']})",
        "RecordPlan020": f"UPDATE T_PLAN SET GOALID=?,PLANNAME=?,PRIORID=?,PLANSTARTDATE=strftime('%Y-%m-%d 00:00:00',?),PLANENDDATE=strftime('%Y-%m-%d 00:00:00',?),PLANUPDATEDATE={com['Com002']} WHERE PLANID=?",
    }

    def RecordGenre(req):
        if req.method == "GET":
            GENRENAME = req.GET["GENRENAME"]
            sql = ""
            sqlParams = []
            if GENRENAME == "":
                sql = Record.sqls["RecordGenre000"]
                sqlParams = ["1"]
            elif GENRENAME != "":
                sql = Record.sqls["RecordGenre001"]
                sqlParams = ["1", f"%{GENRENAME}%"]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def RecordGenreItems(req):
        if req.method == "GET":
            getData = {
                "getData": SQLFuns.SelectFun(Record.sqls["RecordGenre002"], ["1"])
            }
            return JsonResponse(getData)

    @csrf_exempt
    def RecordGenreINSERT(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGenre010"]
            sqlParams = [req.POST["GENRENAME"]]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGenreUPDATE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGenre020"]
            sqlParams = [req.POST["GENRENAME"], req.POST["GENREID"]]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    def RecordGoal(req):
        if req.method == "GET":
            GOALNAME = req.GET["GOALNAME"]
            sql = ""
            sqlParams = []
            if GOALNAME == "":
                sql = Record.sqls["RecordGoal000"]
                sqlParams = ["1", "1"]
            elif GOALNAME != "":
                sql = Record.sqls["RecordGoal001"]
                sqlParams = ["1", "1", f"%{GOALNAME}%"]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def RecordGoalItems(req):
        if req.method == "GET":
            getData = {
                "getData": SQLFuns.SelectFun(Record.sqls["RecordGoal002"], ["1", "1"])
            }
            return JsonResponse(getData)

    @csrf_exempt
    def RecordGoalINSERT(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGoal010"]
            sqlParams = [
                req.POST["GENREID"],
                req.POST["GOALNAME"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGoalUPDATE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGoal020"]
            sqlParams = [
                req.POST["GENREID"],
                req.POST["GOALNAME"],
                req.POST["GOALID"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    def RecordPlan(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = Record.sqls["RecordPlan000"]
                sqlParams = ["1", "1", "1"]
            elif KEYWORD != "":
                sql = Record.sqls["RecordPlan001"]
                sqlParams = ["1", "1", "1", f"%{KEYWORD}%", f"%{KEYWORD}%"]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def RecordPlanItems(req):
        if req.method == "GET":
            GOALID = req.GET["GOALID"]
            getData = {
                "getData": SQLFuns.SelectFun(
                    Record.sqls["RecordPlan002"], ["1", "1", "1", "1", GOALID]
                )
            }
            return JsonResponse(getData)

    @csrf_exempt
    def RecordPlanINSERT(req):
        if req.method == "POST":
            sql = Record.sqls["RecordPlan010"]
            sqlParams = [
                req.POST["GOALID"],
                req.POST["PLANNAME"],
                req.POST["PRIORID"],
                req.POST["PLANSTARTDATE"],
                req.POST["PLANENDDATE"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordPlanUPDATE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordPlan020"]
            sqlParams = [
                req.POST["GOALID"],
                req.POST["PLANNAME"],
                req.POST["PRIORID"],
                req.POST["PLANSTARTDATE"],
                req.POST["PLANENDDATE"],
                req.POST["PLANID"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
