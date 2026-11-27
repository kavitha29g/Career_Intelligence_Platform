-- 1. RECORD COUNT VALIDATION - ALL TABLES

select 'attendance_training' as table_name, count(*) as total_records from attendance_training
union all
select 'communication_assessments', count(*) from communication_assessments
union all
select 'company_requirements', count(*) from company_requirements
union all
select 'companies', count(*) from companies
union all
select 'historical_placements', count(*) from historical_placements
union all
select 'institutions', count(*) from institutions
union all
select 'job_descriptions_skills', count(*) from job_descriptions_skills
union all
select 'job_salary_roles', count(*) from job_salary_roles
union all
select 'job_skills', count(*) from job_skills
union all
select 'mock_interviews', count(*) from mock_interviews
union all
select 'programming_assessments', count(*) from programming_assessments
union all
select 'student_institution', count(*) from student_institution
union all
select 'student_job_applications', count(*) from student_job_applications
union all
select 'student_performance', count(*) from student_performance
union all
select 'students_master', count(*) from students_master
union all
select 'technical_assessments', count(*) from technical_assessments
union all
select 'dim_student', count(*) from dim_student
union all
select 'dim_skill', count(*) from dim_skill
union all
select 'dim_job', count(*) from dim_job
union all
select 'dim_institution', count(*) from dim_institution
union all
select 'dim_date', count(*) from dim_date
union all
select 'dim_company', count(*) from dim_company;

-- DUPLICATE VALIDATION - STUDENT TABLES
-- =====================================================

-- students_master
select student_id, count(*) as duplicate_count
from students_master
group by student_id
having count(*) > 1;

-- student_performance
select student_id, count(*) as duplicate_count
from student_performance
group by student_id
having count(*) > 1;

-- student_institution
select student_id, count(*) as duplicate_count
from student_institution
group by student_id
having count(*) > 1;

-- technical_assessments
select student_id, count(*) as duplicate_count
from technical_assessments
group by student_id
having count(*) > 1;

-- programming_assessments
select student_id, count(*) as duplicate_count
from programming_assessments
group by student_id
having count(*) > 1;

-- communication_assessments
select student_id, count(*) as duplicate_count
from communication_assessments
group by student_id
having count(*) > 1;

-- attendance_training
select student_id, count(*) as duplicate_count
from attendance_training
group by student_id
having count(*) > 1;

-- mock_interviews
select student_id, count(*) as duplicate_count
from mock_interviews
group by student_id
having count(*) > 1;


-- 3. DUPLICATE VALIDATION - BUSINESS TABLES
-- =====================================================

-- companies
select company_id, count(*) as duplicate_count
from companies
group by company_id
having count(*) > 1;

-- institutions
select institution_id, count(*) as duplicate_count
from institutions
group by institution_id
having count(*) > 1;

-- jobs
select job_id, count(*) as duplicate_count
from job_descriptions_skills
group by job_id
having count(*) > 1;

-- student applications
select application_id, count(*) as duplicate_count
from student_job_applications
group by application_id
having count(*) > 1;

-- placements
select placement_id, count(*) as duplicate_count
from historical_placements
group by placement_id
having count(*) > 1;

-- skills
select job_id, skill, count(*) as duplicate_count
from job_skills
group by job_id, skill
having count(*) > 1;

-- 4. DIMENSION TABLE DUPLICATE VALIDATION
-- =====================================================

-- dim_student
select student_id, count(*) as duplicate_count
from dim_student
group by student_id
having count(*) > 1;

-- dim_institution
select institution_id, count(*) as duplicate_count
from dim_institution
group by institution_id
having count(*) > 1;

-- dim_company
select company_id, count(*) as duplicate_count
from dim_company
group by company_id
having count(*) > 1;

-- dim_job
select job_id, count(*) as duplicate_count
from dim_job
group by job_id
having count(*) > 1;

-- dim_skill
select skill_name, count(*) as duplicate_count
from dim_skill
group by skill_name
having count(*) > 1;

-- dim_date
select date_id, count(*) as duplicate_count
from dim_date
group by date_id
having count(*) > 1;

-- 5. NULL VALIDATION - IMPORTANT KEY COLUMNS
-- =====================================================

-- students_master
select
    sum(student_id is null) as null_student_id,
    sum(institution_id is null) as null_institution_id,
    sum(placement_status is null) as null_placement_status
from students_master;

-- student_performance
select
    sum(student_id is null) as null_student_id,
    sum(institution_id is null) as null_institution_id,
    sum(cgpa is null) as null_cgpa,
    sum(placement_status is null) as null_placement_status
from student_performance;

-- companies
select
    sum(company_id is null) as null_company_id,
    sum(company_name is null) as null_company_name
from companies;

-- institutions
select
    sum(institution_id is null) as null_institution_id,
    sum(institution_name is null) as null_institution_name
from institutions;

-- job_descriptions_skills
select
    sum(job_id is null) as null_job_id,
    sum(company_id is null) as null_company_id
from job_descriptions_skills;

-- student_job_applications
select
    sum(application_id is null) as null_application_id,
    sum(student_id is null) as null_student_id,
    sum(job_id is null) as null_job_id,
    sum(company_id is null) as null_company_id
from student_job_applications;

-- historical_placements
select
    sum(placement_id is null) as null_placement_id,
    sum(student_id is null) as null_student_id,
    sum(company_id is null) as null_company_id
from historical_placements;

-- 6. FOREIGN KEY DATA INTEGRITY VALIDATION
-- =====================================================

-- students without institution records
select sm.student_id
from students_master sm
left join institutions i
    on sm.institution_id = i.institution_id
where i.institution_id is null;

-- applications with missing student records
select a.student_id
from student_job_applications a
left join students_master s
    on a.student_id = s.student_id
where s.student_id is null;

-- applications with missing job records
select a.job_id
from student_job_applications a
left join job_descriptions_skills j
    on a.job_id = j.job_id
where j.job_id is null;

-- applications with missing company records
select a.company_id
from student_job_applications a
left join companies c
    on a.company_id = c.company_id
where c.company_id is null;

-- placement records with missing students
select p.student_id
from historical_placements p
left join students_master s
    on p.student_id = s.student_id
where s.student_id is null;

-- placement records with missing companies
select p.company_id
from historical_placements p
left join companies c
    on p.company_id = c.company_id
where c.company_id is null;

-- 7. RANGE VALIDATION
-- =====================================================

-- CGPA validation
select student_id, cgpa
from students_master
where cgpa < 0 or cgpa > 10;

-- backlogs validation
select student_id, backlogs
from students_master
where backlogs < 0;

-- attendance validation
select student_id, attendance_pct
from attendance_training
where attendance_pct < 0 or attendance_pct > 100;

-- training completion validation
select student_id, training_completion_pct
from attendance_training
where training_completion_pct < 0
   or training_completion_pct > 100;


   
-- 8. DATE DIMENSION VALIDATION
-- =====================================================

select
    count(*) as total_dates,
    min(date_id) as start_date,
    max(date_id) as end_date
from dim_date;

-- missing dates in date dimension
select date_id
from dim_date
where date_id is null;

