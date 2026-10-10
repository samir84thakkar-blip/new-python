student_data = {"id1":{"name":"Sara", "class":"V", "subject_integration":"english, math, science"}}
{"id2":{"name":"David", "class":"V", "subject_integration":"english, math, science"}}
{"id3":{"name":"Sara", "class":"V", "subject_integration":"english, math, science"}}
{"id4":{"name":"Surya", "class":"V", "subject_integration":"english, math, science"}}
result = {}
seen_keys = []
for student_id in student_data:
    student_info = student_data[student_id]
    name = student_info["name"]
    
    if name not in seen_keys:
        result[student_id] = student_info
        seen_keys.append(name)
        for k,v in result.items():
            print(k, ":",v)



