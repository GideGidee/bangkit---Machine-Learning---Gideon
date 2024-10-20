# import re

# def show_time_of_pid(line):
#     # Regex pattern to match the date/time and PID
#     pattern = r"([A-Za-z]+\s+\d+\s+\d+:\d+:\d+).*?\[([0-9]+)\]"
#     result = re.search(pattern, line)
#     if result:
#         # Return the matched date/time and PID
#         return f"{result.group(1)} pid:{result.group(2)}"
#     return None

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
# print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
# print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
# print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
# print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
# print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
# print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

import re

regex = r"IP \(\d+\)$"

print(re.search(regex, "IP (2314213)"))