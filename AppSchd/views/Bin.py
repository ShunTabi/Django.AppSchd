from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .SQLFuns import SQLFuns
from datetime import datetime


class Bin:
    com = {
        "Com000": "100",
        "Com002": "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'",
    }
    sqls = {
<<<<<<< HEAD
        "Bin000": "SELECT 'GENRE^'||GENREID AS COL_KEY,'種別項目' AS COL_ITEM,GENRENAME AS COL_NAME,'' AS COL_REMARKS1,'' AS COL_REMARKS2,GENREVISIBLESTATUS AS COL_VISIBLESTATUS,strftime('%Y-%m-%d',GENREUPDATEDATE) AS COL_UPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS IN (?,?) "
        + "UNION "
        + "SELECT 'GOAL^'||GOALID,'目標項目',GOALNAME,'','',GOALVISIBLESTATUS,strftime('%Y-%m-%d',GOALUPDATEDATE) FROM T_GOAL WHERE GOALVISIBLESTATUS IN (?,?) "
        + "UNION "
        + "SELECT 'PLAN^'||PLANID,'計画項目',PLANNAME,GOALNAME||'-'||PLANNAME,strftime('%Y%m%d', PLANSTARTDATE)||'-'||strftime('%Y%m%d', PLANENDDATE),PLANVISIBLESTATUS,strftime('%Y-%m-%d',PLANUPDATEDATE) FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) WHERE PLANVISIBLESTATUS IN (?,?) "
        + "UNION "
        + "SELECT 'SCHEDULE^'||SCHEDULEID,'予定項目',strftime('%Y%m%d', SCHEDULEDATE),strftime('%H%M', SCHEDULESTARTTIME)||'-'||strftime('%H%M', SCHEDULEENDTIME),GOALNAME||'-'||PLANNAME,SCHEDULEVISIBLESTATUS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE SCHEDULEVISIBLESTATUS IN (?,?) "
        + "UNION "
        + "SELECT 'TODO^'||TODOID,'復習項目',TODONAME,GOALNAME||'-'||PLANNAME,'',TODOVISIBLESTATUS,strftime('%Y-%m-%d',TODOUPDATEDATE) FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE TODOVISIBLESTATUS IN (?,?)",
        "Bin001": "SELECT 'GENRE^'||GENREID AS COL_KEY,'種別項目' AS COL_ITEM,GENRENAME AS COL_NAME,'' AS COL_REMARKS1,'' AS COL_REMARKS2,GENREVISIBLESTATUS AS COL_VISIBLESTATUS,strftime('%Y-%m-%d',GENREUPDATEDATE) AS COL_UPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS IN (?,?) AND GENRENAME LIKE ? "
        + "UNION "
        + "SELECT 'GOAL^'||GOALID,'目標項目',GOALNAME,'','',GOALVISIBLESTATUS,strftime('%Y-%m-%d',GOALUPDATEDATE) FROM T_GOAL WHERE GOALVISIBLESTATUS IN (?,?) AND GOALNAME LIKE ? "
        + "UNION "
        + "SELECT 'PLAN^'||PLANID,'計画項目',PLANNAME,GOALNAME||'-'||PLANNAME,strftime('%Y%m%d', PLANSTARTDATE)||'-'||strftime('%Y%m%d', PLANENDDATE),PLANVISIBLESTATUS,strftime('%Y-%m-%d',PLANUPDATEDATE) FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) WHERE PLANVISIBLESTATUS IN (?,?) AND PLANNAME LIKE ?"
        + "UNION "
        + "SELECT 'SCHEDULE^'||SCHEDULEID,'予定項目',strftime('%Y%m%d', SCHEDULEDATE),strftime('%H%M', SCHEDULESTARTTIME)||'-'||strftime('%H%M', SCHEDULEENDTIME),GOALNAME||'-'||PLANNAME,SCHEDULEVISIBLESTATUS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE SCHEDULEVISIBLESTATUS IN (?,?) AND (GOALNAME LIKE ? OR PLANNAME LIKE ?) "
        + "UNION "
        + "SELECT 'TODO^'||TODOID,'復習項目',TODONAME,GOALNAME||'-'||PLANNAME,'',TODOVISIBLESTATUS,strftime('%Y-%m-%d',TODOUPDATEDATE) FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE TODOVISIBLESTATUS IN (?,?) AND (GOALNAME LIKE ? OR PLANNAME LIKE ?)",
        "Bin002": "SELECT 'GENRE^'||GENREID AS COL_KEY,'種別項目' AS COL_ITEM,GENRENAME AS COL_NAME,'' AS COL_REMARKS1,'' AS COL_REMARKS2,GENREVISIBLESTATUS AS COL_VISIBLESTATUS,strftime('%Y-%m-%d',GENREUPDATEDATE) AS COL_UPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'GOAL^'||GOALID,'目標項目',GOALNAME,'','',GOALVISIBLESTATUS,strftime('%Y-%m-%d',GOALUPDATEDATE) FROM T_GOAL WHERE GOALVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'PLAN^'||PLANID,'計画項目',PLANNAME,GOALNAME||'-'||PLANNAME,strftime('%Y%m%d', PLANSTARTDATE)||'-'||strftime('%Y%m%d', PLANENDDATE),PLANVISIBLESTATUS,strftime('%Y-%m-%d',PLANUPDATEDATE) FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) WHERE PLANVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'SCHEDULE^'||SCHEDULEID,'予定項目',strftime('%Y%m%d', SCHEDULEDATE),strftime('%H%M', SCHEDULESTARTTIME)||'-'||strftime('%H%M', SCHEDULEENDTIME),GOALNAME||'-'||PLANNAME,SCHEDULEVISIBLESTATUS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE SCHEDULEVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'TODO^'||TODOID,'復習項目',TODONAME,GOALNAME||'-'||PLANNAME,'',TODOVISIBLESTATUS,strftime('%Y-%m-%d',TODOUPDATEDATE) FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE TODOVISIBLESTATUS = ?",
        "Bin003": "SELECT 'GENRE^'||GENREID AS COL_KEY,'種別項目' AS COL_ITEM,GENRENAME AS COL_NAME,'' AS COL_REMARKS1,'' AS COL_REMARKS2,GENREVISIBLESTATUS AS COL_VISIBLESTATUS,strftime('%Y-%m-%d',GENREUPDATEDATE) AS COL_UPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS = ? AND GENRENAME LIKE ? "
        + "UNION "
        + "SELECT 'GOAL^'||GOALID,'目標項目',GOALNAME,'','',GOALVISIBLESTATUS,strftime('%Y-%m-%d',GOALUPDATEDATE) FROM T_GOAL WHERE GOALVISIBLESTATUS IN (?,?) AND GOALNAME LIKE ? "
        + "UNION "
        + "SELECT 'PLAN^'||PLANID,'計画項目',PLANNAME,GOALNAME||'-'||PLANNAME,strftime('%Y%m%d', PLANSTARTDATE)||'-'||strftime('%Y%m%d', PLANENDDATE),PLANVISIBLESTATUS,strftime('%Y-%m-%d',PLANUPDATEDATE) FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) WHERE PLANVISIBLESTATUS = ? AND PLANNAME LIKE ?"
        + "UNION "
        + "SELECT 'SCHEDULE^'||SCHEDULEID,'予定項目',strftime('%Y%m%d', SCHEDULEDATE),strftime('%H%M', SCHEDULESTARTTIME)||'-'||strftime('%H%M', SCHEDULEENDTIME),GOALNAME||'-'||PLANNAME,SCHEDULEVISIBLESTATUS,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE SCHEDULEVISIBLESTATUS IN (?,?) AND (GOALNAME LIKE ? OR PLANNAME LIKE ?) "
        + "UNION "
        + "SELECT 'TODO^'||TODOID,'復習項目',TODONAME,GOALNAME||'-'||PLANNAME,'',TODOVISIBLESTATUS,strftime('%Y-%m-%d',TODOUPDATEDATE) FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE TODOVISIBLESTATUS = ? AND (GOALNAME LIKE ? OR PLANNAME LIKE ?)",
    }

    def BinStorage(req):
=======
        "Bin000": "SELECT 'GENRE^'||GENREID AS COL_KEY,'種別項目' AS COL_ITEM,GENRENAME AS COL_NAME,'' AS COL_REMARKS1,'' AS COL_REMARKS2,strftime('%Y-%m-%d',GENREUPDATEDATE) AS COL_UPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'GOAL^'||GOALID,'目標項目',GOALNAME,'','',strftime('%Y-%m-%d',GOALUPDATEDATE) FROM T_GOAL WHERE GOALVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'PLAN^'||PLANID,'計画項目',PLANNAME,GOALNAME||'-'||PLANNAME,strftime('%Y%m%d', PLANSTARTDATE)||'-'||strftime('%Y%m%d', PLANENDDATE),strftime('%Y-%m-%d',PLANUPDATEDATE) FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) WHERE PLANVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'SCHEDULE^'||SCHEDULEID,'予定項目',strftime('%Y%m%d', SCHEDULEDATE),strftime('%H%M', SCHEDULESTARTTIME)||'-'||strftime('%H%M', SCHEDULEENDTIME),GOALNAME||'-'||PLANNAME,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE SCHEDULEVISIBLESTATUS = ? "
        + "UNION "
        + "SELECT 'TODO^'||TODOID,'復習項目',TODONAME,GOALNAME||'-'||PLANNAME,'',strftime('%Y-%m-%d',TODOUPDATEDATE) FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE TODOVISIBLESTATUS = ?",
        "Bin001": "SELECT 'GENRE^'||GENREID AS COL_KEY,'種別項目' AS COL_ITEM,GENRENAME AS COL_NAME,'' AS COL_REMARKS1,'' AS COL_REMARKS2,strftime('%Y-%m-%d',GENREUPDATEDATE) AS COL_UPDATEDATE FROM T_GENRE WHERE GENREVISIBLESTATUS = ? AND GENRENAME LIKE ? "
        + "UNION "
        + "SELECT 'GOAL^'||GOALID,'目標項目',GOALNAME,'','',strftime('%Y-%m-%d',GOALUPDATEDATE) FROM T_GOAL WHERE GOALVISIBLESTATUS = ? AND GOALNAME LIKE ? "
        + "UNION "
        + "SELECT 'PLAN^'||PLANID,'計画項目',PLANNAME,GOALNAME||'-'||PLANNAME,strftime('%Y%m%d', PLANSTARTDATE)||'-'||strftime('%Y%m%d', PLANENDDATE),strftime('%Y-%m-%d',PLANUPDATEDATE) FROM T_PLAN INNER JOIN T_GOAL USING(GOALID) WHERE PLANVISIBLESTATUS = ? AND PLANNAME LIKE ?"
        + "UNION "
        + "SELECT 'SCHEDULE^'||SCHEDULEID,'予定項目',strftime('%Y%m%d', SCHEDULEDATE),strftime('%H%M', SCHEDULESTARTTIME)||'-'||strftime('%H%M', SCHEDULEENDTIME),GOALNAME||'-'||PLANNAME,strftime('%Y-%m-%d',SCHEDULEUPDATEDATE) FROM T_SCHEDULE INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE SCHEDULEVISIBLESTATUS = ? AND (GOALNAME LIKE ? OR PLANNAME LIKE ?) "
        + "UNION "
        + "SELECT 'TODO^'||TODOID,'復習項目',TODONAME,GOALNAME||'-'||PLANNAME,'',strftime('%Y-%m-%d',TODOUPDATEDATE) FROM T_TODO INNER JOIN T_PLAN USING(PLANID) INNER JOIN T_GOAL USING(GOALID) WHERE TODOVISIBLESTATUS = ? AND (GOALNAME LIKE ? OR PLANNAME LIKE ?)",
    }

    def StorageBin(req):
>>>>>>> fc65522f7a2f97deb245599f5ceb31a093195c1a
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
                sql = Bin.sqls["Bin000"]
<<<<<<< HEAD
                sqlParams = ["0", "2", "0", "2", "0", "0", "0", "2", "0", "2"]
            elif KEYWORD != "":
                sql = Bin.sqls["Bin001"]
                sqlParams = [
                    "0",
                    "2",
                    f"%{KEYWORD}%",
                    "0",
                    "2",
                    f"%{KEYWORD}%",
                    "0",
                    "2",
                    f"%{KEYWORD}%",
                    "0",
                    "2",
                    f"%{KEYWORD}%",
                    f"%{KEYWORD}%",
                    "0",
=======
                sqlParams = ["2", "2", "2", "2", "2"]
            elif KEYWORD != "":
                sql = Bin.sqls["Bin001"]
                sqlParams = [
                    "2",
                    f"%{KEYWORD}%",
                    "2",
                    f"%{KEYWORD}%",
                    "2",
                    f"%{KEYWORD}%",
                    "2",
                    f"%{KEYWORD}%",
                    f"%{KEYWORD}%",
>>>>>>> fc65522f7a2f97deb245599f5ceb31a093195c1a
                    "2",
                    f"%{KEYWORD}%",
                    f"%{KEYWORD}%",
                ]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)

<<<<<<< HEAD
    def BinRecycle(req):
=======
    def RecycleBin(req):
>>>>>>> fc65522f7a2f97deb245599f5ceb31a093195c1a
        if req.method == "GET":
            KEYWORD = req.GET["KEYWORD"]
            sql = ""
            sqlParams = []
            if KEYWORD == "":
<<<<<<< HEAD
                sql = Bin.sqls["Bin002"]
                sqlParams = ["0", "0", "0", "0", "0"]
            elif KEYWORD != "":
                sql = Bin.sqls["Bin003"]
=======
                sql = Bin.sqls["Bin000"]
                sqlParams = ["0", "0", "0", "0", "0"]
            elif KEYWORD != "":
                sql = Bin.sqls["Bin001"]
>>>>>>> fc65522f7a2f97deb245599f5ceb31a093195c1a
                sqlParams = [
                    "0",
                    f"%{KEYWORD}%",
                    "0",
                    f"%{KEYWORD}%",
                    "0",
                    f"%{KEYWORD}%",
                    "0",
                    f"%{KEYWORD}%",
                    f"%{KEYWORD}%",
                    "0",
                    f"%{KEYWORD}%",
                    f"%{KEYWORD}%",
                ]
            getData = {"getData": SQLFuns.SelectFun(sql, sqlParams)}
            return JsonResponse(getData)
