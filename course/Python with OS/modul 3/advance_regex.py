import re

def rerange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

print(rerange_name("Hopper, Grace M."))

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")) # memotong 5 huruf

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # find all

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) # \b berarti mencari yang 5 huruf

print(re.findall(r"\w{5,10}", "I really like strawberries")) # range

print(re.findall(r"\w{5,}", "I really like strawberries")) # muncul setidaknya 5 huruf

print(re.search(r"s\w{,12}", "I really like strawberries")) # maksimal 20 karekter alphanumerical dengan awalan s

# output PID
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

def extract_pid(log_line):
    regex = r"\[(\d+)\]: \s*([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
