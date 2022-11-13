from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class ToDo:
    com = {
        "Com000": "100",
        "Com002": "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'",
    }
    sqls = {
        "ToDo000": f"SELECT TODOID,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_STATUS.STATUSID AS STATUSID,T_STATUS.STATUSNAME AS STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE GOALVISIBLESTATUS = ? AND PLANVISIBLESTATUS = ? AND TODOVISIBLESTATUS = ? ORDER BY TODOUPDATEDATE DESC LIMIT {com['Com000']}",
        "ToDo001": f"SELECT TODOID,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_STATUS.STATUSID AS STATUSID,T_STATUS.STATUSNAME AS STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE GOALVISIBLESTATUS = ? AND PLANVISIBLESTATUS = ? AND TODOVISIBLESTATUS = ? AND (GOALNAME LIKE ? OR PLANNAME LIKE ?) ORDER BY TODOUPDATEDATE DESC LIMIT {com['Com000']}",
        "ToDo002": f"SELECT TODOID,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_STATUS.STATUSID AS STATUSID,T_STATUS.STATUSNAME AS STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE GOALVISIBLESTATUS = ? AND PLANVISIBLESTATUS = ? AND TODOVISIBLESTATUS = ? AND T_STATUS.STATUSID = ? LIMIT {com['Com000']}",
        "ToDo003": f"SELECT TODOID,GOALID,GOALNAME,PLANID,PLANNAME,TODONAME,T_STATUS.STATUSID AS STATUSID,T_STATUS.STATUSNAME AS STATUSNAME,strftime('%Y-%m-%d',TODOENDDATE) AS TODOENDDATE,strftime('%Y-%m-%d',TODOUPDATEDATE) AS TODOUPDATEDATE FROM T_TODO INNER JOIN T_STATUS USING(STATUSID) INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE GOALVISIBLESTATUS = ? AND PLANVISIBLESTATUS = ? AND TODOVISIBLESTATUS = ? AND T_STATUS.STATUSID = ? AND (GOALNAME LIKE ? OR PLANNAME LIKE ?) LIMIT {com['Com000']}",
        "ToDo010": f"INSERT INTO T_TODO(PLANID,TODONAME,TODOENDDATE,TODOUPDATEDATE) VALUES(?,?,strftime('%Y-%m-%d 00:00:00',?),{com['Com002']})",
        "ToDo020": f"UPDATE T_TODO SET PLANID=?,TODONAME=?,TODOENDDATE=strftime('%Y-%m-%d 00:00:00',?),TODOUPDATEDATE={com['Com002']} WHERE TODOID=?",
    }

    def ToDoToDo(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = ToDo.sqls["ToDo000"]
                sqlParams = ["1", "1", "1"]
            elif KEYWORD != "":
                sql = ToDo.sqls["ToDo001"]
                sqlParams = ["1", "1", "1", f"%{KEYWORD}%", f"%{KEYWORD}%"]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    def ToDoDone(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = ToDo.sqls["ToDo002"]
                sqlParams = ["1", "1", "1", "3"]
            elif KEYWORD != "":
                sql = ToDo.sqls["ToDo003"]
                sqlParams = ["1", "1", "1", "3", f"%{KEYWORD}%", f"%{KEYWORD}%"]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    @csrf_exempt
    def ToDoINSERT(req):
        if req.method == "POST":
            sql = ToDo.sqls["ToDo010"]
            sqlParams = [
                req.POST["PLANID"],
                req.POST["TODONAME"],
                req.POST["TODOENDDATE"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ToDoUPDATE(req):
        if req.method == "POST":
            sql = ToDo.sqls["ToDo020"]
            sqlParams = [
                req.POST["PLANID"],
                req.POST["TODONAME"],
                req.POST["TODOENDDATE"],
                req.POST["TODOID"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
