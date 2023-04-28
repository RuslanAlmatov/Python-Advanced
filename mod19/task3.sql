SELECT full_name
FROM students
WHERE group_id = (SELECT group_id
                  FROM students_groups
                  WHERE teacher_id = (SELECT teacher_id
                                      FROM (SELECT teachers.teacher_id, AVG(grade) as avaga
                                            FROM teachers
                                                     INNER JOIN (SELECT assignments.teacher_id, grade
                                                                 FROM assignments
                                                                          JOIN main.assignments_grades ag
                                                                               on assignments.assisgnment_id = ag.assisgnment_id) a
                                                                on teachers.teacher_id = a.teacher_id
                                            GROUP BY full_name
                                            ORDER BY avaga DESC
                                            LIMIT 1)))
GROUP BY full_name
