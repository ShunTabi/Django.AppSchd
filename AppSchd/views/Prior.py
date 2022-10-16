from django.http import JsonResponse
from .SQLFuns import SQLFuns
from datetime import datetime


class Prior:
    com = {
        "Com000": "100",
        "Com001": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    sqls = {
        "Prior000": f"SELECT PRIORID AS ID,PRIORNAME||'('||PRIORSUBNAME||')' AS NAME FROM T_PRIOR",
    }

    def PriorItems(req):
        if req.method == "GET":
            getData = {"getData": SQLFuns.SelectFun(Prior.sqls["Prior000"], [])}
            return JsonResponse(getData)
