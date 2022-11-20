from django.urls import path
from ..views.Record import Record
from ..views.Prior import Prior
from ..views.Schedule import Schedule
from ..views.ToDo import ToDo
from ..views.Bin import Bin
from ..views.Note import Note

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
    path(
        "Record/RecordGenre/RecordGenreUPDATEVISIBLESTATUS",
        Record.RecordGenreUPDATEVISIBLESTATUS,
        name="RecordGenreUPDATEVISIBLESTATUS",
    ),
    path(
        "Record/RecordGenre/RecordGenreDELETE",
        Record.RecordGenreDELETE,
        name="RecordGenreDELETE",
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
    path(
        "Record/RecordGoal/RecordGoalUPDATEVISIBLESTATUS",
        Record.RecordGoalUPDATEVISIBLESTATUS,
        name="RecordGoalUPDATEVISIBLESTATUS",
    ),
    path(
        "Record/RecordGoal/RecordGoalDELETE",
        Record.RecordGoalDELETE,
        name="RecordPlanDELETE",
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
    path(
        "Record/RecordPlan/RecordPlanUPDATEVISIBLESTATUS",
        Record.RecordPlanUPDATEVISIBLESTATUS,
        name="RecordPlanUPDATEVISIBLESTATUS",
    ),
    path(
        "Record/RecordPlan/RecordPlanUPDATESTATUS",
        Record.RecordPlanUPDATESTATUS,
        name="RecordPlanUPDATESTATUS",
    ),
    path(
        "Record/RecordPlan/RecordPlanDELETE",
        Record.RecordPlanDELETE,
        name="RecordPlanDELETE",
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
    path(
        "Schedule/ScheduleUPDATEVISIBLESTATUS",
        Schedule.ScheduleUPDATEVISIBLESTATUS,
        name="ScheduleUPDATEVISIBLESTATUS",
    ),
    path(
        "Schedule/ScheduleUPDATESTATUS",
        Schedule.ScheduleUPDATESTATUS,
        name="ScheduleUPDATESTATUS",
    ),
    path("Schedule/ScheduleDELETE", Schedule.ScheduleDELETE, name="ScheduleDELETE"),
    #####################################################################################
    path("ToDo/ToDoToDo", ToDo.ToDoToDo, name="ToDoToDo"),
    path("ToDo/ToDoDone", ToDo.ToDoDone, name="ToDoDone"),
    path("ToDo/ToDoINSERT", ToDo.ToDoINSERT, name="ToDoINSERT"),
    path("ToDo/ToDoUPDATE", ToDo.ToDoUPDATE, name="ToDoUPDATE"),
    path(
        "ToDo/ToDoUPDATEVISIBLESTATUS",
        ToDo.ToDoUPDATEVISIBLESTATUS,
        name="ToDoUPDATEVISIBLESTATUS",
    ),
    path("ToDo/ToDoUPDATESTATUS", ToDo.ToDoUPDATESTATUS, name="ToDoUPDATESTATUS"),
    path("ToDo/ToDoDELETE", ToDo.ToDoDELETE, name="ToDoDELETE"),
    #####################################################################################
    path("Bin/BinStorage", Bin.BinStorage, name="BinStorage"),
    path("Bin/BinRecycle", Bin.BinRecycle, name="BinRecycle"),
    #####################################################################################
    path("Prior/PriorItems", Prior.PriorItems, name="PriorItems"),
    #####################################################################################
    #####################################################################################
    path("Note/NoteRecord", Note.NoteRecord, name="NoteRecord"),
    path("Note/NoteList", Note.NoteList, name="NoteList"),
    path("Note/NoteINSERT", Note.NoteINSERT, name="NoteINSERT"),
    path("Note/NoteUPDATE", Note.NoteUPDATE, name="NoteUPDATE"),
    #####################################################################################
]
