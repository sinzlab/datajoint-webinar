import datajoint as dj

username = dj.conn().conn_info["user"]
schema = dj.schema(username + "_pipeline_session02")


@schema
class Mouse(dj.Manual):
    definition = """
    mouse_id: int                       # mouse id
    ---
    dob:      date                      # date of birth
    sex:      enum("M", "F", "unknown") # sex
    """


mouse_data = [
    {"dob": "2017-03-01", "mouse_id": 0, "sex": "M"},
    {"dob": "2016-11-19", "mouse_id": 1, "sex": "M"},
    {"dob": "2016-11-20", "mouse_id": 2, "sex": "unknown"},
    {"dob": "2016-12-25", "mouse_id": 5, "sex": "F"},
    {"dob": "2017-01-01", "mouse_id": 10, "sex": "F"},
    {"dob": "2017-01-03", "mouse_id": 11, "sex": "F"},
    {"dob": "2017-05-12", "mouse_id": 100, "sex": "F"},
]
Mouse.insert(mouse_data, skip_duplicates=True)


@schema
class Session(dj.Manual):
    definition = """
    # experimental session
    -> Mouse
    session_date       : date          # session date
    ---
    experiment_setup   : int           # experiment setup ID
    experimenter       : varchar(100)  # name of the experimenter
    start              : time          # starting time of the session
    end                : time          # ending time of the session
    """


session_data = [
    {
        "experiment_setup": 0,
        "experimenter": "Edgar Y. Walker",
        "mouse_id": 0,
        "session_date": "2017-05-15",
        "start": "10:12:43",
        "end": "11:05:21",
    },
    {
        "experiment_setup": 0,
        "experimenter": "Edgar Y. Walker",
        "mouse_id": 0,
        "session_date": "2017-05-19",
        "start": "10:15:37",
        "end": "11:02:41",
    },
    {
        "experiment_setup": 1,
        "experimenter": "Fabian Sinz",
        "mouse_id": 5,
        "session_date": "2017-01-05",
        "start": "12:54:23",
        "end": "14:43:25",
    },
    {
        "experiment_setup": 100,
        "experimenter": "Jacob Reimer",
        "mouse_id": 100,
        "session_date": "2017-05-25",
        "start": "16:51:39",
        "end": "18:32:18",
    },
]
Session.insert(session_data, skip_duplicates=True)
