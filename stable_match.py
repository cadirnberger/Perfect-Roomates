# 0-indexed preference matrices for algorithm implementation
students = {
    0: [8, 6, 5, 9, 7],
    1: [8, 9, 7, 5, 6],
    2: [9, 8, 5, 7, 6],
    3: [5, 7, 9, 8, 6],
    4: [5, 8, 7, 6, 9]
}

students_2 = {
    5: [4, 1, 0, 3, 2],
    6: [1, 3, 0, 4, 2],
    7: [2, 1, 0, 3, 4],
    8: [3, 1, 2, 4, 0],
    9: [0, 4, 1, 2, 3]
}


def stable_match(students, students_2):
    """ This function takes in the room and student data and 
    returns a stable matching of students to rooms. """
    #Create a dictionary to hold the matches
    matches = {}
    #looks at the data it resives and matches them 
    while any(student not in matches for student in students):
            pref = next(student for student in students if student not in matches )
            act = next(student_2 for student_2 in students[pref])
            if act not in matches.values():
                matches[pref] = act
            elif students_2[act].index(pref) > students_2[act].index(matches.values()):
                matches.pop(matches[act])
                matches[pref] = act
                
            else:
                continue

    return matches

def main(students, students_2) -> None:
    matches = stable_match(students, students_2)
    print("Stable Matching of Students to Rooms:")
    for student, room in matches.items():
        print(f"Student {student} is matched to Room {room}")


if __name__ == "__main__":
	main(students, students_2)
         