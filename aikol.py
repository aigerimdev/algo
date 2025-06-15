# loop trough the list
students = [
	{
		id: 11,
		fullName: 'Adam Dan',
		age: 25,
		grade: '4.2',
		enrolledDate: '03/08/1995',
	},
	{
		id: 2,
		fullName: 'Vika Butorchuk',
		age: 26,
		grade: '3.5',
		enrolledDate: '03/08/2025',
	},
	{
		id: 3,
		fullName: 'Lina Carlos',
		age: 26,
		grade: '4',
		enrolledDate: '03/08/2025',
	},
	{
		id: 4,
		fullName: 'Marina Kosnyak',
		age: 40,
		grade: '2',
		enrolledDate: '03/08/2025',
	},
	{
		id: 7,
		fullName: 'Aigerim Kalygulova',
		age: 31,
		grade: '4',
		enrolledDate: '03/08/2025',
	},
	{
		id: 9,
		fullName: 'Adam Charleson',
		age: 25,
		grade: '4.5',
		enrolledDate: '03/08/2023',
	},
	{
		id: 10,
		fullName: 'Scott Rireka',
		age: 30,
		grade: '3',
		enrolledDate: '03/08/2022',
	},
]

def find_greater_grades(students):
    high_scored_students = []
    for student in students:
        if float(student['grade']) >= 4:
            high_scored_students.append(student)
    return high_scored_students


def curentCohortStudents(students):
	result = []
	for student in students[student]:
			if(new Date(student.enrolledDate) > new Date("01/01/2025"))
    		result.append(student)
  return result
  
