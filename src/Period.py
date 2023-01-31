def get_day_period(hour):
    if 6 < hour <= 12:
        return "MORNING"
    elif 12 < hour <= 18:
        return "AFTERNOON"
    elif 18 < hour <= 23:
        return "EVENING"
    else:
        return "NIGHT"
