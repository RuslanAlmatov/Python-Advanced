SELECT students_groups.group_id as "номер группы",
       round(AVG(grade), 2)     as "средний балл в группе",
       min(grade)               as "минимальный балл в группе",
       max(grade)               as "максимальный балл в группе"
FROM (SELECT group_id, grade
      FROM students,
           assignments_grades
      WHERE assignments_grades.student_id = students.student_id) as st_gr,
     students_groups
WHERE "номер группы" = st_gr.group_id
GROUP BY "номер группы"
ORDER BY "номер группы";