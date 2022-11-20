from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class Record:
    SQLLimit = "100"
    now = "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'"
    sqls = {
        "RecordGenre000": ""
        + f"SELECT GENREID,GENRENAME,strftime('%Y-%m-%d',GENREUPDATEDATE) AS GENREUPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS=1 ORDER BY GENRENAME,GENREUPDATEDATE DESC LIMIT {SQLLimit}",
        "RecordGenre001": ""
        + f"SELECT GENREID,GENRENAME,strftime('%Y-%m-%d',GENREUPDATEDATE) AS GENREUPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS=1 AND GENRENAME LIKE :GENRENAME ORDER BY GENRENAME,GENREUPDATEDATE DESC LIMIT {SQLLimit}",
        "RecordGenre002": ""
        + "SELECT GENREID AS ID,GENRENAME AS NAME FROM T_GENRE WHERE GENREVISIBLESTATUS=1 ORDER BY GENRENAME,GENREUPDATEDATE DESC",
        "RecordGenre010": ""
        + f"INSERT INTO T_GENRE(GENRENAME,GENREUPDATEDATE) VALUES(:GENRENAME,{now})",
        "RecordGenre020": f"UPDATE T_GENRE SET GENRENAME=:GENRENAME,GENREUPDATEDATE={now} WHERE GENREID=:GENREID",
        "RecordGenre021": f"UPDATE T_GENRE SET GENREVISIBLESTATUS=:VISIBLESTATUS,GENREUPDATEDATE={now} WHERE GENREID=:GENREID",
        "RecordGenre030": "DELETE FROM T_GENRE WHERE GENREID=:GENREID",
        "RecordGoal000": ""
        + f"SELECT GOALID,GENREID,GENRENAME,GOALNAME,strftime('%Y-%m-%d',GOALUPDATEDATE) AS GOALUPDATEDATE FROM T_GOAL "
        + f"INNER JOIN T_GENRE USING(GENREID) WHERE GENREVISIBLESTATUS=1 AND GOALVISIBLESTATUS=1 ORDER BY GOALNAME,GOALUPDATEDATE DESC LIMIT {SQLLimit}",
        "RecordGoal001": ""
        + f"SELECT GOALID,GENREID,GENRENAME,GOALNAME,strftime('%Y-%m-%d',GOALUPDATEDATE) AS GOALUPDATEDATE FROM T_GOAL "
        + f"INNER JOIN T_GENRE USING(GENREID) WHERE GENREVISIBLESTATUS=1 AND GOALVISIBLESTATUS=1 AND GOALNAME LIKE :GOALNAME ORDER BY GOALNAME,GOALUPDATEDATE DESC LIMIT {SQLLimit}",
        "RecordGoal002": ""
        + "SELECT GOALID AS ID,GOALNAME AS NAME FROM T_GOAL WHERE GOALVISIBLESTATUS=1 ORDER BY GOALNAME,GOALUPDATEDATE DESC",
        "RecordGoal010": f"INSERT INTO T_GOAL(GENREID,GOALNAME,GOALUPDATEDATE) VALUES(:GENREID,:GOALNAME,{now})",
        "RecordGoal020": f"UPDATE T_GOAL SET GENREID=:GENREID,GOALNAME=:GOALNAME,GOALUPDATEDATE={now} WHERE GOALID=:GOALID",
        "RecordGoal021": f"UPDATE T_GOAL SET GOALVISIBLESTATUS=:VISIBLESTATUS,GOALUPDATEDATE={now} WHERE GOALID=:GOALID",
        "RecordGoal030": "DELETE FROM T_GOAL WHERE GOALID=:GOALID",
        "RecordPlan000": ""
        + f"SELECT "
        + f"PLANID,ALERTSTATUS,GOALID,GOALNAME,PLANNAME,T_PLAN.PRIORID,PRIORNAME,PRIORSUBNAME,T_PLAN.STATUSID,STATUSNAME,strftime('%Y-%m-%d',PLANSTARTDATE) AS PLANSTARTDATE,strftime('%Y-%m-%d',PLANENDDATE) AS PLANENDDATE,strftime('%Y-%m-%d',PLANUPDATEDATE) AS PLANUPDATEDATE "
        + f"FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_PRIOR ON T_PLAN.PRIORID = T_PRIOR.PRIORID "
        + f"INNER JOIN T_STATUS ON T_PLAN.STATUSID = T_STATUS.STATUSID "
        + f"LEFT OUTER JOIN (SELECT PLANID,'！' AS ALERTSTATUS FROM T_PLAN WHERE STATUSID in (1,2) AND PLANENDDATE<{now}) USING(PLANID) WHERE GOALVISIBLESTATUS=1 AND PLANVISIBLESTATUS=1 ORDER BY T_PLAN.PRIORID ASC,T_PLAN.STATUSID ASC,PLANENDDATE ASC,GOALNAME,PLANNAME,PLANUPDATEDATE DESC LIMIT {SQLLimit}",
        "RecordPlan001": ""
        + f"SELECT "
        + f"PLANID,ALERTSTATUS,GOALID,GOALNAME,PLANNAME,T_PLAN.PRIORID,PRIORNAME,PRIORSUBNAME,T_PLAN.STATUSID,STATUSNAME,strftime('%Y-%m-%d',PLANSTARTDATE) AS PLANSTARTDATE,strftime('%Y-%m-%d',PLANENDDATE) AS PLANENDDATE,strftime('%Y-%m-%d',PLANUPDATEDATE) AS PLANUPDATEDATE "
        + f"FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_PRIOR ON T_PLAN.PRIORID = T_PRIOR.PRIORID INNER JOIN T_STATUS ON T_PLAN.STATUSID = T_STATUS.STATUSID "
        + f"LEFT OUTER JOIN (SELECT PLANID,'！' AS ALERTSTATUS "
        + f"FROM T_PLAN WHERE STATUSID in (1,2) AND PLANENDDATE<{now}) USING(PLANID) WHERE GOALVISIBLESTATUS=1 AND PLANVISIBLESTATUS=1 AND (GOALNAME LIKE :KEYWORD OR PLANNAME LIKE :KEYWORD) ORDER BY T_PLAN.PRIORID ASC,T_PLAN.STATUSID ASC,PLANENDDATE ASC,GOALNAME,PLANNAME,PLANUPDATEDATE DESC LIMIT {SQLLimit}",
        "RecordPlan002": ""
        + "SELECT PLANID AS ID,PLANNAME AS NAME FROM T_PLAN WHERE GOALID=@GOALID AND PLANVISIBLESTATUS=1 ORDER BY PRIORID ASC,STATUSID ASC,PLANENDDATE ASC,PLANNAME,PLANUPDATEDATE DESC",
        "RecordPlan010": ""
        + f"INSERT INTO T_PLAN(GOALID,PLANNAME,PRIORID,PLANSTARTDATE,PLANENDDATE,PLANUPDATEDATE) VALUES(:GOALID,:PLANNAME,:PRIORID,strftime('%Y-%m-%d 00:00:00',:PLANSTARTDATE),strftime('%Y-%m-%d 00:00:00',:PLANENDDATE),{now})",
        "RecordPlan020": ""
        + f"UPDATE T_PLAN SET GOALID=:GOALID,PLANNAME=:PLANNAME,PRIORID=:PRIORID,PLANSTARTDATE=strftime('%Y-%m-%d 00:00:00',:PLANSTARTDATE),PLANENDDATE=strftime('%Y-%m-%d 00:00:00',:PLANENDDATE),PLANUPDATEDATE={now} WHERE PLANID=:PLANID",
        "RecordPlan021": f"UPDATE T_PLAN SET PLANVISIBLESTATUS=:VISIBLESTATUS,PLANUPDATEDATE={now} WHERE PLANID=:PLANID",
        "RecordPlan022": f"UPDATE T_PLAN SET STATUSID=:STATUSID,PLANUPDATEDATE={now} WHERE PLANID=:PLANID",
        "RecordPlan023": f"UPDATE T_PLAN SET PRIORID=:PRIORID,PLANUPDATEDATE={now} WHERE PLANID=:PLANID",
        "RecordPlan030": "DELETE FROM T_PLAN WHERE PLANID=:PLANID",
    }

    def RecordGenre(req):
        if req.method == "GET":
            GENRENAME = req.GET["GENRENAME"]
            sql = ""
            sqlParams = []
            if GENRENAME == "":
                sql = Record.sqls["RecordGenre000"]
                sqlParams = []
            elif GENRENAME != "":
                sql = Record.sqls["RecordGenre001"]
                sqlParams = {"GENRENAME": f"%{GENRENAME}%"}
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def RecordGenreItems(req):
        if req.method == "GET":
            getData = {"getData": SQLFuns.SelectFun(Record.sqls["RecordGenre002"], {})}
            return JsonResponse(getData)

    @csrf_exempt
    def RecordGenreINSERT(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGenre010"]
            sqlParams = {"GENRENAME": req.POST["GENRENAME"]}
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGenreUPDATE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGenre020"]
            sqlParams = {
                "GENRENAME": req.POST["GENRENAME"],
                "GENREID": req.POST["GENREID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGenreUPDATEVISIBLESTATUS(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGenre021"]
            sqlParams = {
                "VISIBLESTATUS": req.POST["VISIBLESTATUS"],
                "GENREID": req.POST["GENREID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGenreDELETE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGenre030"]
            sqlParams = {
                "GENREID": req.POST["GENREID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    def RecordGoal(req):
        if req.method == "GET":
            GOALNAME = req.GET["GOALNAME"]
            sql = ""
            sqlParams = []
            if GOALNAME == "":
                sql = Record.sqls["RecordGoal000"]
                sqlParams = []
            elif GOALNAME != "":
                sql = Record.sqls["RecordGoal001"]
                sqlParams = {"GOALNAME": f"%{GOALNAME}%"}
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def RecordGoalItems(req):
        if req.method == "GET":
            getData = {"getData": SQLFuns.SelectFun(Record.sqls["RecordGoal002"], [])}
            return JsonResponse(getData)

    @csrf_exempt
    def RecordGoalINSERT(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGoal010"]
            sqlParams = {
                "GENREID": req.POST["GENREID"],
                "GOALNAME": req.POST["GOALNAME"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGoalUPDATE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGoal020"]
            sqlParams = {
                "GENREID": req.POST["GENREID"],
                "GOALNAME": req.POST["GOALNAME"],
                "GOALID": req.POST["GOALID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGoalUPDATEVISIBLESTATUS(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGoal021"]
            sqlParams = {
                "VISIBLESTATUS": req.POST["VISIBLESTATUS"],
                "GOALID": req.POST["GOALID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordGoalDELETE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordGoal030"]
            sqlParams = {
                "GOALID": req.POST["GOALID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    def RecordPlan(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = Record.sqls["RecordPlan000"]
                sqlParams = []
            elif KEYWORD != "":
                sql = Record.sqls["RecordPlan001"]
                sqlParams = {"KEYWORD": f"%{KEYWORD}%"}
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def RecordPlanItems(req):
        if req.method == "GET":
            getData = {
                "getData": SQLFuns.SelectFun(
                    Record.sqls["RecordPlan002"], {"GOALID": req.GET["GOALID"]}
                )
            }
            return JsonResponse(getData)

    @csrf_exempt
    def RecordPlanINSERT(req):
        if req.method == "POST":
            sql = Record.sqls["RecordPlan010"]
            sqlParams = {
                "GOALID": req.POST["GOALID"],
                "PLANNAME": req.POST["PLANNAME"],
                "PRIORID": req.POST["PRIORID"],
                "PLANSTARTDATE": req.POST["PLANSTARTDATE"],
                "PLANENDDATE": req.POST["PLANENDDATE"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordPlanUPDATE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordPlan020"]
            sqlParams = {
                "GOALID": req.POST["GOALID"],
                "PLANNAME": req.POST["PLANNAME"],
                "PRIORID": req.POST["PRIORID"],
                "PLANSTARTDATE": req.POST["PLANSTARTDATE"],
                "PLANENDDATE": req.POST["PLANENDDATE"],
                "PLANID": req.POST["PLANID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordPlanUPDATEVISIBLESTATUS(req):
        if req.method == "POST":
            sql = Record.sqls["RecordPlan021"]
            sqlParams = {
                "VISIBLESTATUS": req.POST["VISIBLESTATUS"],
                "PLANID": req.POST["PLANID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordPlanUPDATESTATUS(req):
        if req.method == "POST":
            sql = Record.sqls["RecordPlan022"]
            sqlParams = {
                "STATUSID": req.POST["STATUSID"],
                "PLANID": req.POST["PLANID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def RecordPlanDELETE(req):
        if req.method == "POST":
            sql = Record.sqls["RecordPlan030"]
            sqlParams = {
                "PLANID": req.POST["PLANID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
