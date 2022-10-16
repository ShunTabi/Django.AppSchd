from django.urls import path
from ..views.Record import Record
from ..views.Prior import Prior
from ..views.Schedule import Schedule
from ..views.ToDo import ToDo

urlpatterns = [
    #####################################################################################
    path("Record/RecordGenre", Record.RecordGenre, name="RecordGenre"),
    path(
        "Record/RecordGenre/RecordGenreItems",
        Record.RecordGenreItems,
        name="RecordGenreItems",
    ),
    path(
        "Record/RecordGenre/RecordGenreINSERT",
        Record.RecordGenreINSERT,
        name="RecordGenreINSERT",
    ),
    path(
        "Record/RecordGenre/RecordGenreUPDATE",
        Record.RecordGenreUPDATE,
        name="RecordGenreUPDATE",
    ),
    #####################################################################################
    path("Record/RecordGoal", Record.RecordGoal, name="RecordGoal"),
    path(
        "Record/RecordGoal/RecordGoalItems",
        Record.RecordGoalItems,
        name="RecordGoalItems",
    ),
    path(
        "Record/RecordGoal/RecordGoalINSERT",
        Record.RecordGoalINSERT,
        name="RecordGoalINSERT",
    ),
    path(
        "Record/RecordGoal/RecordGoalUPDATE",
        Record.RecordGoalUPDATE,
        name="RecordGoalUPDATE",
    ),
    #####################################################################################
    path("Record/RecordPlan", Record.RecordPlan, name="RecordPlan"),
    path(
        "Record/RecordPlan/RecordPlanItems",
        Record.RecordPlanItems,
        name="RecordPlanItems",
    ),
    path(
        "Record/RecordPlan/RecordPlanINSERT",
        Record.RecordPlanINSERT,
        name="RecordPlanINSERT",
    ),
    path(
        "Record/RecordPlan/RecordPlanUPDATE",
        Record.RecordPlanUPDATE,
        name="RecordPlanUPDATE",
    ),
    #####################################################################################
    path(
        "Schedule/ScheduleOneDay",
        Schedule.ScheduleOneDay,
        name="ScheduleOneDay",
    ),
    path("Schedule/ScheduleList", Schedule.ScheduleList, name="ScheduleList"),
    path("Schedule/ScheduleINSERT", Schedule.ScheduleINSERT, name="ScheduleINSERT"),
    path("Schedule/ScheduleUPDATE", Schedule.ScheduleUPDATE, name="ScheduleUPDATE"),
    #####################################################################################
    path("ToDo/ToDoToDo", ToDo.ToDoToDo, name="ToDoToDo"),
    path("ToDo/ToDoDone", ToDo.ToDoDone, name="ToDoDone"),
    path("ToDo/ToDoINSERT", ToDo.ToDoINSERT, name="ToDoINSERT"),
    path("ToDo/ToDoUPDATE", ToDo.ToDoUPDATE, name="ToDoUPDATE"),
    #####################################################################################
    path("Prior/PriorItems", Prior.PriorItems, name="PriorItems"),
    #####################################################################################
]
