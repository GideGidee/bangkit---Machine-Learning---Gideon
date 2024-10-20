import re
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!")) # memisahkan kalimat dengan [.?!]

print(re.split(r"([.?!])", "One sentence. Another one? And the last one!")) # memisahkan kalimat dengan [.!?] tetapi [.!?] ikut terpisah

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")) # repalce email dengan [REDACTED]

print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")) # menukar posisi