SELECT full_name as "ФИО преподавателя", round(AVG(grade), 2) as "самый низкий балл"
FROM teachers
         INNER JOIN (SELECT assignments.teacher_id, grade
                     FROM assignments
                              JOIN main.assignments_grades ag on assignments.assisgnment_id = ag.assisgnment_id) a
                    on teachers.teacher_id = a.teacher_id
GROUP BY full_name
ORDER BY "самый низкий балл"
LIMIT 1
