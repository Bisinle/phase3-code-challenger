def time_converter(hours, minutes, period):
    if period == "am" and hours > 11:
        return f"{hours-12:02d}:{minutes} "
    elif period == "pm":
        if hours == 12:
            return f"{hours:02d}:{minutes} "
        elif hours < 12:
            return f"{hours + 12:02d}:{minutes} "
        elif hours > 11:
            return f"{hours-12:02d}:{minutes} "
    else:
        return f"{hours:02d}:{minutes:02d} "


print(time_converter(1, 50, "am"))
