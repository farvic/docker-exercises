import datetime
import pytz

# Timezone can be changed to any allowed values.
current_time = datetime.datetime.now(pytz.timezone(
    'America/Bahia')).strftime(" %m.%d.%Y %H:%M:%S %z")

print(current_time)
