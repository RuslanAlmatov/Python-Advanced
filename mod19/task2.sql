SELECT full_name as "ФИО ученика", AVG(grade) as average_grade
FROM students
         JOIN assignments_grades ag on students.student_id = ag.student_id
GROUP BY full_name
ORDER BY average_grade DESC
LIMIT 10