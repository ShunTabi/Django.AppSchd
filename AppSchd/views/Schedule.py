from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class Schedule:
    com = {
        "Com000": "100",
        "Com002": "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'",
    }
    sqls = {
        "Schedule000": f"SELECT SCHEDULEID,GOALID,GOALNAME,PLANID,PLANNAME,T_STATUS.STATUSID AS STATUSID,T_STATUS.STATUSNAME AS STATUSNAME,strftime('%Y-%m-%d',SCHEDULEDATE) AS SCHEDULEDATE,strftime('%H:%M',SCHEDULESTARTTIME) AS SCHEDULESTARTTIME,strftime('%H:%M',SCHEDULEENDTIME) AS SCHEDULEENDTIME,SCHEDULEHOURS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) AS SCHEDULEUPDATEDATE FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_STATUS USING(STATUSID) WHERE SCHEDULEVISIBLESTATUS = ? AND SCHEDULEDATE LIKE ? LIMIT {com['Com000']}",
        "Schedule001": f"SELECT SCHEDULEID,GOALID,GOALNAME,PLANID,PLANNAME,T_STATUS.STATUSID AS STATUSID,T_STATUS.STATUSNAME AS STATUSNAME,strftime('%Y-%m-%d',SCHEDULEDATE) AS SCHEDULEDATE,strftime('%H:%M',SCHEDULESTARTTIME) AS SCHEDULESTARTTIME,strftime('%H:%M',SCHEDULEENDTIME) AS SCHEDULEENDTIME,SCHEDULEHOURS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) AS SCHEDULEUPDATEDATE FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_STATUS USING(STATUSID) WHERE SCHEDULEVISIBLESTATUS = ? ORDER BY SCHEDULEDATE DESC,SCHEDULESTARTTIME,SCHEDULEENDTIME LIMIT {com['Com000']}",
        "Schedule002": f"SELECT SCHEDULEID,GOALID,GOALNAME,PLANID,PLANNAME,T_STATUS.STATUSID AS STATUSID,T_STATUS.STATUSNAME AS STATUSNAME,strftime('%Y-%m-%d',SCHEDULEDATE) AS SCHEDULEDATE,strftime('%H:%M',SCHEDULESTARTTIME) AS SCHEDULESTARTTIME,strftime('%H:%M',SCHEDULEENDTIME) AS SCHEDULEENDTIME,SCHEDULEHOURS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) AS SCHEDULEUPDATEDATE FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) INNER JOIN T_STATUS USING(STATUSID) WHERE SCHEDULEVISIBLESTATUS = ? AND (GOALNAME LIKE ? OR PLANNAME LIKE ?) ORDER BY SCHEDULEDATE DESC,SCHEDULESTARTTIME,SCHEDULEENDTIME LIMIT {com['Com000']}",
        "Schedule010": f"INSERT INTO T_SCHEDULE(PLANID,SCHEDULEDATE,SCHEDULESTARTTIME,SCHEDULEENDTIME,SCHEDULEHOURS,SCHEDULELOCATION,SCHEDULEHEIGHT,SCHEDULEUPDATEDATE) VALUES(?,?,?,?,round(cast((strftime('%s', ?) - strftime('%s', ?)) as REAL)/ 3600,2),?,?,{com['Com002']})",
        "Schedule020": f"UPDATE T_SCHEDULE SET PLANID=?,SCHEDULEDATE=?,SCHEDULESTARTTIME=?,SCHEDULEENDTIME=?,SCHEDULEHOURS=round(cast((strftime('%s', ?) - strftime('%s', ?)) as REAL)/ 3600,2),SCHEDULELOCATION=?,SCHEDULEHEIGHT=?,SCHEDULEUPDATEDATE={com['Com002']} WHERE SCHEDULEID=?",
    }

    def ScheduleOneDay(req):
        if req.method == "GET":
            SCHEDULEDATE = req.GET["SCHEDULEDATE"]
            getData = {
                "getData": SQLFuns.SelectFun(
                    Schedule().sqls["Schedule000"], ["1", f"{SCHEDULEDATE}%"]
                )
            }
            return JsonResponse(getData)

    def ScheduleList(req):
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = Schedule.sqls["Schedule001"]
                sqlParams = ["1"]
            elif KEYWORD != "":
                sql = Schedule.sqls["Schedule002"]
                sqlParams = ["1", f"%{KEYWORD}%", f"%{KEYWORD}%"]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    @csrf_exempt
    def ScheduleINSERT(req):
        if req.method == "POST":
            sql = Schedule.sqls["Schedule010"]
            SCHEDULESTARTHM = (req.POST["SCHEDULESTARTTIME"]).split(":")
            SCHEDULELOCATION = SCHEDULESTARTHM[0] * 60 + SCHEDULESTARTHM[1]
            SCHEDULEENDHM = (req.POST["SCHEDULEENDTIME"]).split(":")
            SCHEDULEHEIGHT = SCHEDULEENDHM[0] * 60 + SCHEDULEENDHM[1]
            sqlParams = [
                req.POST["PLANID"],
                req.POST["SCHEDULEDATE"],
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULESTARTTIME']}:00",
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULEENDTIME']}:00",
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULEENDTIME']}:00",
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULESTARTTIME']}:00",
                str(SCHEDULELOCATION),
                str(SCHEDULEHEIGHT),
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ScheduleUPDATE(req):
        if req.method == "POST":
            sql = Schedule.sqls["Schedule020"]
            SCHEDULESTARTHM = (req.POST["SCHEDULESTARTTIME"]).split(":")
            SCHEDULELOCATION = int(SCHEDULESTARTHM[0]) * 60 + int(SCHEDULESTARTHM[1])
            SCHEDULEENDHM = (req.POST["SCHEDULEENDTIME"]).split(":")
            SCHEDULEHEIGHT = int(SCHEDULEENDHM[0]) * 60 + int(SCHEDULEENDHM[1])
            sqlParams = [
                req.POST["PLANID"],
                req.POST["SCHEDULEDATE"],
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULESTARTTIME']}:00",
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULEENDTIME']}:00",
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULEENDTIME']}:00",
                f"{req.POST['SCHEDULEDATE']} {req.POST['SCHEDULESTARTTIME']}:00",
                str(SCHEDULELOCATION),
                str(SCHEDULEHEIGHT),
                req.POST["SCHEDULEID"],
            ]
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
