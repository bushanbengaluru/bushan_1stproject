from datetime import datetime
import pytz

"""This script will coverts Eastern time to India time."""

def convert_time(src_time, src_tz, dest_tz):
    src_tz = pytz.timezone(src_tz)
    dest_tz = pytz.timezone(dest_tz)
    src_time = src_tz.localize(src_time)
    dest_time = src_time.astimezone(dest_tz)
    return dest_time

def main():
    src_time = datetime.now()
    src_tz = 'EST'
    dest_tz = 'INDIAN/MAURITIUS'
    dest_time = convert_time(src_time, src_tz, dest_tz)
    print(f"TIME IN INDIA IS: {dest_time.strftime('%Y-%m-%d %H:%M')}")

if __name__ == '__main__':
    main()