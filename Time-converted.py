def time_converter(hours_, minutes_, period):
    min_to_sec = minutes_ * 60
    hrs_to_secs = hours_ * 3600

    # trun all into seconds
    time_in_sconds = min_to_sec + hrs_to_secs
    hours = time_in_sconds // 3600
    minutes = (time_in_sconds % 3600) // 60

    if period == "am" and hours > 11:
        return f"{hours-12:02d}:{minutes} "
    elif period == "pm" and hours < 12:
        return f"{hours + 12:02d}:{minutes} "
    elif period == "pm" and hours > 11:
        return f"{hours-12:02d}:{minutes} "

    else:
        return f"{hours:02d}:{minutes:02d} "


print(time_converter(5, 50, "pm"))
