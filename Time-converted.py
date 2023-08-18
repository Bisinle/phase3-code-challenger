def time_converter(hours, minutes, period):
    if (period == "am" or period == "pm") and (minutes <= 59) and (0 <= hours <= 12):
        if period == "am" and hours > 11:
            return f"{hours-12:02d}:{minutes} Hours"
        elif period == "pm":
            if hours == 12:
                return f"{hours:02d}:{minutes} Hours"
            elif hours < 12:
                return f"{hours + 12:02d}:{minutes} Hours"
            elif hours > 11:
                return f"{hours-12:02d}:{minutes} Hours"
        else:
            return f"{hours:02d}:{minutes:02d} Hours"
    else:
        return "NOT A VALID HOUR"


print(time_converter(1, 50, "am"))
