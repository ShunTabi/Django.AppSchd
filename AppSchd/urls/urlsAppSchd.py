from django.urls import path
from ..views.Record import Record
from ..views.Prior import Prior
from ..views.Schedule import Schedule
from ..views.ToDo import ToDo
from ..views.Bin import Bin
<<<<<<< HEAD
from ..views.Note import Note
=======
>>>>>>> fc65522f7a2f97deb245599f5ceb31a093195c1a

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
<<<<<<< HEAD
    path("Bin/BinStorage", Bin.BinStorage, name="BinStorage"),
    path("Bin/BinRecycle", Bin.BinRecycle, name="BinRecycle"),
=======
    path("Bin/StorageBin", Bin.StorageBin, name="StorageBin"),
    path("Bin/RecycleBin", Bin.RecycleBin, name="RecycleBin"),
>>>>>>> fc65522f7a2f97deb245599f5ceb31a093195c1a
    #####################################################################################
    path("Prior/PriorItems", Prior.PriorItems, name="PriorItems"),
    #####################################################################################
    #####################################################################################
    path("Note/NoteOneDay", Note.NoteOneDay, name="NoteOneDay"),
    path("Note/NoteList", Note.NoteList, name="NoteList"),
    path("Note/NoteINSERT", Note.NoteINSERT, name="NoteINSERT"),
    path("Note/NoteUPDATE", Note.NoteUPDATE, name="NoteUPDATE"),
    #####################################################################################
]
