morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ["Python", "C#", "C", "Java", "Ruby"]

possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)