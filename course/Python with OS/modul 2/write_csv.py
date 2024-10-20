import csv

# hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
# with open('hosts.csv', 'w') as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)

# write dictionary
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)