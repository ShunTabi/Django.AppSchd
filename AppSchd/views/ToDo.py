from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class ToDo:
    SQLLimit = "100"
    now = "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'"
    sqls = {
        "ToDo000": ""
        + f"SELECT TODOID,ALERTSTATUS,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_TODO.STATUSID AS STATUSID,STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_GENRE USING(GENREID) LEFT OUTER JOIN(SELECT TODOID,'！' AS ALERTSTATUS FROM T_TODO WHERE STATUSID in (1,2) AND TODOENDDATE<{now}) USING(TODOID) WHERE GENREVISIBLESTATUS=1 AND GOALVISIBLESTATUS=1 AND PLANVISIBLESTATUS=1 AND TODOVISIBLESTATUS=1 ORDER BY T_TODO.STATUSID ASC,TODOENDDATE,GOALNAME,PLANNAME,TODOUPDATEDATE LIMIT {SQLLimit}",
        "ToDo001": ""
        + f"SELECT TODOID,ALERTSTATUS,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_TODO.STATUSID AS STATUSID,STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_GENRE USING(GENREID) LEFT OUTER JOIN(SELECT TODOID,'！' AS ALERTSTATUS FROM T_TODO WHERE STATUSID in (1,2) AND TODOENDDATE<{now}) USING(TODOID) WHERE GENREVISIBLESTATUS=1 AND GOALVISIBLESTATUS=1 AND PLANVISIBLESTATUS=1 AND TODOVISIBLESTATUS=1 AND (GOALNAME LIKE :KEYWORD OR PLANNAME LIKE :KEYWORD) ORDER BY T_TODO.STATUSID ASC,TODOENDDATE,GOALNAME,PLANNAME,TODOUPDATEDATE LIMIT {SQLLimit}",
        "ToDo002": ""
        + f"SELECT TODOID,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_STATUS.STATUSID AS STATUSID,STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_GENRE USING(GENREID) WHERE GENREVISIBLESTATUS=1 AND GOALVISIBLESTATUS=1 AND PLANVISIBLESTATUS=1 AND TODOVISIBLESTATUS=1 AND T_TODO.STATUSID=3 ORDER BY TODOENDDATE,GOALNAME,PLANNAME LIMIT {SQLLimit}",
        "ToDo003": ""
        + f"SELECT TODOID,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_STATUS.STATUSID AS STATUSID,STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_GENRE USING(GENREID) WHERE GENREVISIBLESTATUS=1 AND GOALVISIBLESTATUS=1 AND PLANVISIBLESTATUS=1 AND TODOVISIBLESTATUS=1 AND T_TODO.STATUSID=3 AND (GOALNAME LIKE :KEYWORD OR PLANNAME LIKE :KEYWORD) ORDER BY TODOENDDATE,GOALNAME,PLANNAME LIMIT {SQLLimit}",
        "ToDo010": f"INSERT INTO T_TODO(PLANID,TODONAME,STATUSID,TODOENDDATE,TODOUPDATEDATE) VALUES(:PLANID,:TODONAME,:STATUSID,:TODOENDDATE,{now})",
        "ToDo020": f"UPDATE T_TODO SET PLANID=:PLANID,TODONAME=:TODONAME,TODOENDDATE=:TODOENDDATE,TODOUPDATEDATE={now} WHERE TODOID=:TODOID",
        "ToDo021": f"UPDATE T_TODO SET TODOVISIBLESTATUS=:VISIBLESTATUS,TODOUPDATEDATE={now} WHERE TODOID=:TODOID",
        "ToDo022": f"UPDATE T_TODO SET STATUSID=:STATUSID,TODOUPDATEDATE={now} WHERE TODOID=:TODOID",
        "ToDo030": "DELETE FROM T_TODO WHERE TODOID=:TODOID",
    }

    def ToDoToDo(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = ToDo.sqls["ToDo000"]
                sqlParams = {}
            elif KEYWORD != "":
                sql = ToDo.sqls["ToDo001"]
                sqlParams = {"KEYWORD": f"%{KEYWORD}%"}
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def ToDoDone(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = ToDo.sqls["ToDo002"]
                sqlParams = []
            elif KEYWORD != "":
                sql = ToDo.sqls["ToDo003"]
                sqlParams = {"KEYWORD": f"%{KEYWORD}%"}
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    @csrf_exempt
    def ToDoINSERT(req):
        if req.method == "POST":
            sql = ToDo.sqls["ToDo010"]
            sqlParams = {
                "PLANID": req.POST["PLANID"],
                "TODONAME": req.POST["TODONAME"],
                "TODOENDDATE": req.POST["TODOENDDATE"],
                "STATUSID": req.POST["STATUSID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ToDoUPDATE(req):
        if req.method == "POST":
            sql = ToDo.sqls["ToDo020"]
            sqlParams = {
                "PLANID": req.POST["PLANID"],
                "TODONAME": req.POST["TODONAME"],
                "TODOENDDATE": req.POST["TODOENDDATE"],
                "TODOID": req.POST["TODOID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ToDoUPDATEVISIBLESTATUS(req):
        if req.method == "POST":
            sql = ToDo.sqls["ToDo021"]
            sqlParams = {
                "VISIBLESTATUS": req.POST["VISIBLESTATUS"],
                "TODOID": req.POST["TODOID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ToDoUPDATESTATUS(req):
        if req.method == "POST":
            sql = ToDo.sqls["ToDo022"]
            sqlParams = {
                "STATUSID": req.POST["STATUSID"],
                "TODOID": req.POST["TODOID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ToDoDELETE(req):
        if req.method == "POST":
            sql = ToDo.sqls["ToDo030"]
            sqlParams = {
                "TODOID": req.POST["TODOID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
