from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class Schedule:
    SQLLimit = "100"
    now = "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'"
    sqls = {
        "Schedule000": ""
        + "SELECT "
        + "SCHEDULEID,ALERTSTATUS,GOALID,GOALNAME,PLANID,PLANNAME,T_STATUS.STATUSID AS STATUSID,STATUSNAME,strftime('%Y-%m-%d',SCHEDULEDATE) AS SCHEDULEDATE,strftime('%H:%M',SCHEDULESTARTTIME) AS SCHEDULESTARTTIME,strftime('%H:%M',SCHEDULEENDTIME) AS SCHEDULEENDTIME,SCHEDULEHOURS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) AS SCHEDULEUPDATEDATE "
        + "FROM T_SCHEDULE "
        + "INNER JOIN T_PLAN USING(PLANID) "
        + "INNER JOIN T_GOAL USING(GOALID) "
        + "INNER JOIN T_STATUS USING(STATUSID) "
        + "INNER JOIN T_PRIOR USING(PRIORID) "
        + f"LEFT OUTER JOIN(SELECT SCHEDULEID,'！' AS ALERTSTATUS FROM T_SCHEDULE WHERE STATUSID in (1,2) AND SCHEDULEENDTIME<{now}) USING(SCHEDULEID) "
        + f"WHERE SCHEDULEVISIBLESTATUS=1 AND SCHEDULEDATE LIKE :SCHEDULEDATE ORDER BY SCHEDULESTARTTIME LIMIT {SQLLimit}",
        "Schedule001": ""
        + "SELECT "
        + "SCHEDULEID,ALERTSTATUS,GOALID,GOALNAME,PLANID,PLANNAME,T_STATUS.STATUSID AS STATUSID,STATUSNAME,strftime('%Y-%m-%d',SCHEDULEDATE) AS SCHEDULEDATE,strftime('%H:%M',SCHEDULESTARTTIME) AS SCHEDULESTARTTIME,strftime('%H:%M',SCHEDULEENDTIME) AS SCHEDULEENDTIME,SCHEDULEHOURS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) AS SCHEDULEUPDATEDATE "
        + "FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) "
        + "INNER JOIN T_GOAL USING(GOALID) "
        + "INNER JOIN T_STATUS USING(STATUSID) "
        + "INNER JOIN T_PRIOR USING(PRIORID) "
        + f"LEFT OUTER JOIN(SELECT SCHEDULEID,'！' AS ALERTSTATUS FROM T_SCHEDULE WHERE STATUSID in (1,2) AND SCHEDULEENDTIME<{now}) USING(SCHEDULEID) "
        + f"WHERE SCHEDULEVISIBLESTATUS=1 ORDER BY SCHEDULEDATE DESC,SCHEDULESTARTTIME,SCHEDULEENDTIME LIMIT {SQLLimit}",
        "Schedule002": ""
        + "SELECT "
        + "SCHEDULEID,ALERTSTATUS,GOALID,GOALNAME,PLANID,PLANNAME,T_STATUS.STATUSID AS STATUSID,STATUSNAME,strftime('%Y-%m-%d',SCHEDULEDATE) AS SCHEDULEDATE,strftime('%H:%M',SCHEDULESTARTTIME) AS SCHEDULESTARTTIME,strftime('%H:%M',SCHEDULEENDTIME) AS SCHEDULEENDTIME,SCHEDULEHOURS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) AS SCHEDULEUPDATEDATE "
        + "FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) "
        + "INNER JOIN T_GOAL USING(GOALID) "
        + "INNER JOIN T_STATUS USING(STATUSID) "
        + f"INNER JOIN T_PRIOR USING(PRIORID) LEFT OUTER JOIN(SELECT SCHEDULEID,'！' AS ALERTSTATUS FROM T_SCHEDULE WHERE STATUSID in (1,2) AND SCHEDULEENDTIME<{now}) USING(SCHEDULEID) "
        + f"WHERE SCHEDULEVISIBLESTATUS=1 AND (GOALNAME LIKE :KEYWORD OR PLANNAME LIKE :KEYWORD) ORDER BY SCHEDULEDATE DESC,SCHEDULESTARTTIME,SCHEDULEENDTIME LIMIT {SQLLimit}",
        "Schedule005": "SELECT SCHEDULESTARTTIME,SCHEDULEENDTIME FROM T_SCHEDULE WHERE SCHEDULEID != @SCHEDULEID AND SCHEDULEDATE=@SCHEDULEDATE",
        "Schedule010": ""
        + "INSERT INTO T_SCHEDULE(PLANID,SCHEDULEDATE,SCHEDULESTARTTIME,SCHEDULEENDTIME,SCHEDULEHOURS,SCHEDULELOCATION,SCHEDULEHEIGHT,SCHEDULEUPDATEDATE) "
        + f"VALUES(:PLANID,:SCHEDULEDATE,:SCHEDULESTARTTIME,:SCHEDULEENDTIME,round(cast((strftime('%s', :SCHEDULEENDTIME) - strftime('%s', :SCHEDULESTARTTIME)) as REAL)/ 3600,2),:SCHEDULELOCATION,:SCHEDULEHEIGHT,{now})",
        "Schedule020": f"UPDATE T_SCHEDULE SET PLANID=:PLANID,SCHEDULEDATE=:SCHEDULEDATE,SCHEDULESTARTTIME=:SCHEDULESTARTTIME,SCHEDULEENDTIME=:SCHEDULEENDTIME,SCHEDULEHOURS=round(cast((strftime('%s', :SCHEDULEENDTIME) - strftime('%s', :SCHEDULESTARTTIME)) as REAL)/ 3600,2),SCHEDULELOCATION=:SCHEDULELOCATION,SCHEDULEHEIGHT=:SCHEDULEHEIGHT,SCHEDULEUPDATEDATE={now} WHERE SCHEDULEID=:SCHEDULEID",
        "Schedule021": f"UPDATE T_SCHEDULE SET SCHEDULEVISIBLESTATUS=:VISIBLESTATUS,SCHEDULEUPDATEDATE={now} WHERE SCHEDULEID=:SCHEDULEID",
        "Schedule022": f"UPDATE T_SCHEDULE SET STATUSID=:STATUSID,SCHEDULEUPDATEDATE={now} WHERE SCHEDULEID=:SCHEDULEID",
        "Schedule030": "DELETE FROM T_SCHEDULE WHERE SCHEDULEID=:SCHEDULEID",
    }

    def ScheduleOneDay(req):
        if req.method == "GET":
            SCHEDULEDATE = req.GET["SCHEDULEDATE"]
            getData = {
                "getData": SQLFuns.SelectFun(
                    Schedule().sqls["Schedule000"], {"SCHEDULEDATE": f"{SCHEDULEDATE}%"}
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
                sqlParams = []
            elif KEYWORD != "":
                sql = Schedule.sqls["Schedule002"]
                sqlParams = {"KEYWORD": f"%{KEYWORD}%"}
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

    @csrf_exempt
    def ScheduleINSERT(req):
        if req.method == "POST":
            SCHEDULEDATE = req.POST["SCHEDULEDATE"]
            SCHEDULESTARTTIME = req.POST["SCHEDULESTARTTIME"]
            SCHEDULEENDTIME = req.POST["SCHEDULEENDTIME"]
            chkBox = SQLFuns.SelectFun(
                Schedule.sqls["Schedule005"],
                {
                    "SCHEDULEID": "",
                    "SCHEDULEDATE": SCHEDULEDATE,
                },
            )
            TGScheduleStartTime = datetime.strptime(
                f"{SCHEDULEDATE} {SCHEDULESTARTTIME}:00", "%Y-%m-%d %H:%M:%S"
            )
            TGScheduleEndTime = datetime.strptime(
                f"{SCHEDULEDATE} {SCHEDULEENDTIME}:00", "%Y-%m-%d %H:%M:%S"
            )
            CheckResult = TGScheduleStartTime < TGScheduleEndTime
            for index in range(len(chkBox)):
                ScheduledScheduleStartTime = datetime.strptime(
                    chkBox[index]["SCHEDULESTARTTIME"], "%Y-%m-%d %H:%M:%S"
                )
                ScheduledScheduleEndTime = datetime.strptime(
                    chkBox[index]["SCHEDULEENDTIME"], "%Y-%m-%d %H:%M:%S"
                )
                CheckResult = CheckResult and (
                    (
                        TGScheduleEndTime < ScheduledScheduleEndTime
                        and TGScheduleEndTime < ScheduledScheduleStartTime
                    )
                    or (
                        ScheduledScheduleStartTime < TGScheduleStartTime
                        and ScheduledScheduleEndTime < TGScheduleStartTime
                    )
                )
            if CheckResult:
                sql = Schedule.sqls["Schedule010"]
                SCHEDULESTARTHM = (SCHEDULESTARTTIME).split(":")
                SCHEDULELOCATION = int(SCHEDULESTARTHM[0]) * 60 + int(
                    SCHEDULESTARTHM[1]
                )
                SCHEDULEENDHM = (SCHEDULEENDTIME).split(":")
                SCHEDULEHEIGHT = (
                    int(SCHEDULEENDHM[0]) * 60
                    + int(SCHEDULEENDHM[1])
                    - SCHEDULELOCATION
                )
                sqlParams = {
                    "PLANID": req.POST["PLANID"],
                    "SCHEDULEDATE": SCHEDULEDATE,
                    "SCHEDULESTARTTIME": f"{SCHEDULEDATE} {SCHEDULESTARTTIME}:00",
                    "SCHEDULEENDTIME": f"{SCHEDULEDATE} {SCHEDULEENDTIME}:00",
                    "SCHEDULELOCATION": str(SCHEDULELOCATION),
                    "SCHEDULEHEIGHT": str(SCHEDULEHEIGHT),
                }
                SQLFuns.DmlFun(sql, sqlParams)
                return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ScheduleUPDATE(req):
        if req.method == "POST":
            SCHEDULEID = req.POST["SCHEDULEID"]
            SCHEDULEDATE = req.POST["SCHEDULEDATE"]
            SCHEDULESTARTTIME = req.POST["SCHEDULESTARTTIME"]
            SCHEDULEENDTIME = req.POST["SCHEDULEENDTIME"]
            chkBox = SQLFuns.SelectFun(
                Schedule.sqls["Schedule005"],
                {
                    "SCHEDULEID": SCHEDULEID,
                    "SCHEDULEDATE": SCHEDULEDATE,
                },
            )
            TGScheduleStartTime = datetime.strptime(
                f"{SCHEDULEDATE} {SCHEDULESTARTTIME}:00", "%Y-%m-%d %H:%M:%S"
            )
            TGScheduleEndTime = datetime.strptime(
                f"{SCHEDULEDATE} {SCHEDULEENDTIME}:00", "%Y-%m-%d %H:%M:%S"
            )
            CheckResult = TGScheduleStartTime < TGScheduleEndTime
            for index in range(len(chkBox)):
                ScheduledScheduleStartTime = datetime.strptime(
                    chkBox[index]["SCHEDULESTARTTIME"], "%Y-%m-%d %H:%M:%S"
                )
                ScheduledScheduleEndTime = datetime.strptime(
                    chkBox[index]["SCHEDULEENDTIME"], "%Y-%m-%d %H:%M:%S"
                )
                CheckResult = CheckResult and (
                    (
                        TGScheduleEndTime < ScheduledScheduleEndTime
                        and TGScheduleEndTime < ScheduledScheduleStartTime
                    )
                    or (
                        ScheduledScheduleStartTime < TGScheduleStartTime
                        and ScheduledScheduleEndTime < TGScheduleStartTime
                    )
                )
            if CheckResult:
                sql = Schedule.sqls["Schedule020"]
                SCHEDULESTARTHM = (req.POST["SCHEDULESTARTTIME"]).split(":")
                SCHEDULELOCATION = int(SCHEDULESTARTHM[0]) * 60 + int(
                    SCHEDULESTARTHM[1]
                )
                SCHEDULEENDHM = (req.POST["SCHEDULEENDTIME"]).split(":")
                SCHEDULEHEIGHT = (
                    int(SCHEDULEENDHM[0]) * 60
                    + int(SCHEDULEENDHM[1])
                    - SCHEDULELOCATION
                )
                sqlParams = {
                    "PLANID": req.POST["PLANID"],
                    "SCHEDULEDATE": SCHEDULEDATE,
                    "SCHEDULESTARTTIME": f"{SCHEDULEDATE} {SCHEDULESTARTTIME}:00",
                    "SCHEDULEENDTIME": f"{SCHEDULEDATE} {SCHEDULEENDTIME}:00",
                    "SCHEDULELOCATION": str(SCHEDULELOCATION),
                    "SCHEDULEHEIGHT": str(SCHEDULEHEIGHT),
                    "SCHEDULEID": SCHEDULEID,
                }
                SQLFuns.DmlFun(sql, sqlParams)
                return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ScheduleUPDATEVISIBLESTATUS(req):
        if req.method == "POST":
            sql = Schedule.sqls["Schedule021"]
            sqlParams = {
                "VISIBLESTATUS": req.POST["VISIBLESTATUS"],
                "SCHEDULEID": req.POST["SCHEDULEID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ScheduleUPDATESTATUS(req):
        if req.method == "POST":
            sql = Schedule.sqls["Schedule022"]
            sqlParams = {
                "STATUSID": req.POST["STATUSID"],
                "SCHEDULEID": req.POST["SCHEDULEID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})

    @csrf_exempt
    def ScheduleDELETE(req):
        if req.method == "POST":
            sql = Schedule.sqls["Schedule030"]
            sqlParams = {
                "SCHEDULEID": req.POST["SCHEDULEID"],
            }
            SQLFuns.DmlFun(sql, sqlParams)
            return JsonResponse({"getData": [{"RESULT": "OK!"}]})
