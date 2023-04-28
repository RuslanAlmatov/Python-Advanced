SELECT round(AVG(grade), 2) AS "Средняя оценка за те задания, где нужно выучить или прочитать"
FROM assignments_grades,
     assignments
WHERE (assignment_text LIKE 'выучить%'
    OR assignment_text LIKE 'прочитать%')
  AND (assignments.assisgnment_id = assignments_grades.assisgnment_id)