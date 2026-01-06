from datetime import timedelta

def parse_time(time_str: str) -> timedelta:
    if not time_str:
        return timedelta(seconds=0)
    
    time_str = time_str.strip().lower()
    unit = time_str[-1]
    
    try:
        if unit.isdigit():
            return timedelta(seconds=int(time_str))
        
        value = int(time_str[:-1])
        if unit == 's':
            return timedelta(seconds=value)
        if unit == 'm':
            return timedelta(minutes=value)
        if unit == 'h':
            return timedelta(hours=value)
        if unit == 'd':
            return timedelta(days=value)
    except (ValueError, IndexError):
        return timedelta(seconds=0)
        
    return timedelta(seconds=0)
