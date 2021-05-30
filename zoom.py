from pyzoom import ZoomClient
from datetime import datetime as dt

def create_meet(name, time, duration, password):
    client = ZoomClient('GRSmjD17T2mpYl0rXjHX5g', 'MyhEy6NOEIjTC9Mfavc8CtJdRqyJa0M1Hzqk')
    meeting = client.meetings.create_meeting(name, start_time=dt.isoformat(time), duration_min=duration, password=password)
    return meeting.join_url

