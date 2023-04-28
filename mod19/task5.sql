SELECT students_groups.group_id AS "Номер группы", COUNT(student_id) AS "Количество человек в группе"
FROM students,
     students_groups
WHERE students.group_id = students_groups.group_id
GROUP BY students_groups.group_id;

SELECT group_id AS "Номер группы", round(AVG(grade), 2) AS "Средняя оценка группы"
FROM students,
     assignments_grades
WHERE students.student_id = assignments_grades.student_id
GROUP BY group_id;

SELECT COUNT(assignments_grades.student_id)
FROM students,
     assignments_grades
WHERE students.student_id = assignments_grades.student_id
  AND grade = 0;

SELECT COUNT(student_id)
FROM assignments,
     assignments_grades
WHERE due_date < date;

SELECT student_id, COUNT(student_id) AS cnt
FROM assignments_grades
GROUP BY student_id
HAVING cnt > 2

