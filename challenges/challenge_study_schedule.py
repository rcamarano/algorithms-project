def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    # raise NotImplementedError
    if target_time is None:
        return None

    count = 0
    for time_start, time_end in permanence_period:
        if not isinstance(time_start, int) or not isinstance(time_end, int):
            return None
        if time_start <= target_time <= time_end:
            count += 1
        # if not isinstance(time_start, int) or not isinstance(time_end, int):
        #     return None
        # if time_start <= target_time <= time_end:
        #     count += 1
    return count
