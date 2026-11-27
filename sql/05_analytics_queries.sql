-- Q7: which technical skills are most common among placed students?

select
    skill_name,
    count(*) as students_with_skill,
    round(
        count(*) * 100.0 /
        (select count(*)
         from students_master
         where lower(trim(placement_status)) = 'placed'),
        2
    ) as percentage_of_placed_students
from (
    select t.student_id, 'Python' as skill_name
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.Python >= 50

    union all

    select t.student_id, 'SQL'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.SQL >= 50

    union all

    select t.student_id, 'Java'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.Java >= 50

    union all

    select t.student_id, 'Excel'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.Excel >= 50

    union all

    select t.student_id, 'Power BI'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.`Power BI` >= 50

    union all

    select t.student_id, 'Tableau'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.Tableau >= 50

    union all

    select t.student_id, 'AWS'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.AWS >= 50

    union all

    select t.student_id, 'Azure'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.Azure >= 50

    union all

    select t.student_id, 'PySpark'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.PySpark >= 50

    union all

    select t.student_id, 'Machine Learning'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.`Machine Learning` >= 50

    union all

    select t.student_id, 'Statistics'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.Statistics >= 50

    union all

    select t.student_id, 'Git'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'placed'
      and t.Git >= 50

) skill_data
group by skill_name
order by students_with_skill desc;

-- Q8: which skills are frequently missing among unplaced students?

select
    skill_name,
    count(*) as students_with_skill_gap,
    round(
        count(*) * 100.0 /
        (select count(*)
         from students_master
         where lower(trim(placement_status)) = 'unplaced'),
        2
    ) as percentage_of_unplaced_students
from (
    select t.student_id, 'Python' as skill_name
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.Python < 50

    union all

    select t.student_id, 'SQL'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.SQL < 50

    union all

    select t.student_id, 'Java'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.Java < 50

    union all

    select t.student_id, 'Excel'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.Excel < 50

    union all

    select t.student_id, 'Power BI'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.`Power BI` < 50

    union all

    select t.student_id, 'Tableau'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.Tableau < 50

    union all

    select t.student_id, 'AWS'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.AWS < 50

    union all

    select t.student_id, 'Azure'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.Azure < 50

    union all

    select t.student_id, 'PySpark'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.PySpark < 50

    union all

    select t.student_id, 'Machine Learning'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.`Machine Learning` < 50

    union all

    select t.student_id, 'Statistics'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.Statistics < 50

    union all

    select t.student_id, 'Git'
    from technical_assessments t
    join students_master s on t.student_id = s.student_id
    where lower(trim(s.placement_status)) = 'unplaced'
      and t.Git < 50

) skill_gaps
group by skill_name
order by students_with_skill_gap desc;


-- Q9: which institutions have the highest placement percentage?

select
    i.institution_id,
    i.institution_name,
    count(s.student_id) as total_students,
    sum(
        case
            when lower(trim(s.placement_status)) = 'placed'
            then 1
            else 0
        end
    ) as placed_students,
    sum(
        case
            when lower(trim(s.placement_status)) = 'unplaced'
            then 1
            else 0
        end
    ) as unplaced_students,
    round(
        sum(
            case
                when lower(trim(s.placement_status)) = 'placed'
                then 1
                else 0
            end
        ) * 100.0 / nullif(count(s.student_id), 0),
        2
    ) as placement_percentage
from institutions i
left join students_master s
    on i.institution_id = s.institution_id
group by
    i.institution_id,
    i.institution_name
order by placement_percentage desc;


-- Q10: which training batches have the highest interview success rate?

select
    s.batch_id,
    count(m.student_id) as total_mock_interviews,
    sum(
        case
            when (m.technical_interview_score + m.hr_interview_score) / 2 >= 70
            then 1
            else 0
        end
    ) as successful_interviews,
    round(
        sum(
            case
                when (m.technical_interview_score + m.hr_interview_score) / 2 >= 70
                then 1
                else 0
            end
        ) * 100.0 / nullif(count(m.student_id), 0),
        2
    ) as interview_success_rate,
    round(avg(m.technical_interview_score), 2) as avg_technical_score,
    round(avg(m.hr_interview_score), 2) as avg_hr_score
from students_master s
join mock_interviews m
    on s.student_id = m.student_id
group by s.batch_id
order by interview_success_rate desc;

-- Q11: which companies offer the highest average salary?

select
    c.company_id,
    c.company_name,
    count(p.placement_id) as total_placements,
    round(avg(p.offered_salary_lpa), 2) as average_salary_lpa,
    round(max(p.offered_salary_lpa), 2) as highest_salary_lpa,
    round(min(p.offered_salary_lpa), 2) as lowest_salary_lpa
from companies c
join historical_placements p
    on c.company_id = p.company_id
where p.offered_salary_lpa is not null
group by
    c.company_id,
    c.company_name
order by average_salary_lpa desc;


-- Q12: which students have completed training but are still unplaced?

select
    s.student_id,
    s.institution_id,
    s.batch_id,
    s.degree,
    s.department,
    s.cgpa,
    s.placement_status,
    a.training_days_total,
    a.training_days_attended,
    a.modules_total,
    a.modules_completed,
    a.training_completion_pct,
    a.attendance_pct
from students_master s
join attendance_training a
    on s.student_id = a.student_id
where lower(trim(s.placement_status)) = 'unplaced'
  and a.training_completion_pct = 100
  and a.modules_completed = a.modules_total
order by a.attendance_pct desc;

-- Q13. What is the relationship between attendance and placement outcomes?

select
    skill_name,

    count(case when skill_score >= 70 then 1 end)
        as proficient_students,

    round(
        sum(case
            when skill_score >= 70
             and lower(trim(placement_status)) = 'placed'
            then 1 else 0
        end) * 100.0
        / nullif(count(case when skill_score >= 70 then 1 end), 0),
        2
    ) as proficient_placement_rate,

    count(case when skill_score < 70 then 1 end)
        as non_proficient_students,

    round(
        sum(case
            when skill_score < 70
             and lower(trim(placement_status)) = 'placed'
            then 1 else 0
        end) * 100.0
        / nullif(count(case when skill_score < 70 then 1 end), 0),
        2
    ) as non_proficient_placement_rate,

    round(
        (
            sum(case
                when skill_score >= 70
                 and lower(trim(placement_status)) = 'placed'
                then 1 else 0
            end) * 100.0
            / nullif(count(case when skill_score >= 70 then 1 end), 0)
        )
        -
        (
            sum(case
                when skill_score < 70
                 and lower(trim(placement_status)) = 'placed'
                then 1 else 0
            end) * 100.0
            / nullif(count(case when skill_score < 70 then 1 end), 0)
        ),
        2
    ) as placement_rate_difference_pct_points

from
(
    select student_id, 'python' as skill_name, Python as skill_score
    from technical_assessments

    union all

    select student_id, 'sql', `SQL`
    from technical_assessments

    union all

    select student_id, 'java', Java
    from technical_assessments

    union all

    select student_id, 'excel', Excel
    from technical_assessments

    union all

    select student_id, 'power bi', `Power BI`
    from technical_assessments

    union all

    select student_id, 'tableau', Tableau
    from technical_assessments

    union all

    select student_id, 'aws', AWS
    from technical_assessments

    union all

    select student_id, 'azure', Azure
    from technical_assessments

    union all

    select student_id, 'pyspark', PySpark
    from technical_assessments

    union all

    select student_id, 'machine learning', `Machine Learning`
    from technical_assessments

    union all

    select student_id, 'statistics', Statistics
    from technical_assessments

    union all

    select student_id, 'git', Git
    from technical_assessments
) skill_data

join students_master m
    on skill_data.student_id = m.student_id

where skill_score is not null
  and m.placement_status is not null

group by skill_name

order by placement_rate_difference_pct_points desc;
