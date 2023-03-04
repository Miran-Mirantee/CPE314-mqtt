import datetime
import pytz

# convert time in epoch format to human-readable format
def convertEpoch(epoch):
    # Convert Unix epoch time to a datetime object
    tz = pytz.timezone('GMT')
    date_time = datetime.datetime.fromtimestamp(epoch, tz)

    # Convert datetime object to a string in the desired format
    formatted_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time