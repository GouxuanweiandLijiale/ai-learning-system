#["VS Code", "Git", "Python"]
#classwork1
tools = ["VS Code", "Git", "Python"]
print(tools[0])
print(tools[2])
print(len(tools))
tools.append("SQLite")
tools.remove("Git")
for tool in tools:
    print(tool)
#classwork2
student = {
    "name": "Tom",
    "major": "telecommunication",
    "day": 4,
    "topic": "list and dict"
}
print(student["name"])
student["mood"] = "good"
student["day"] = 5
for key,value in student.items():
    print(f"{key}: {value}")
#classwork3
study_records = [
    {"date": "2026-03-04", "minutes": 58, "done": "learnt if"},
    {"date": "2026-03-05", "minutes": 62, "done": "learnt for and while loop"},
    {"date": "2026-03-06", "minutes": 66, "done": "learnt list and dic"},
]
for record in study_records:
    print(f"on {record['date']} I spent {record['minutes']} on learning {record['done']}")
#add study
for index,tool in enumerate(tools,start=1):
    print(f"{index}: {tool}")