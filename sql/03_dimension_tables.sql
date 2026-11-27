-- ==========================================
-- 1. dim_student
-- ==========================================

create table dim_student as
select
    student_id,
    institution_id,
    batch_id,
    degree,
    department,
    graduation_year
from students_master;

alter table dim_student
add primary key (student_id);


-- ==========================================
-- 2. dim_institution
-- ==========================================

create table dim_institution as
select
    institution_id,
    institution_name,
    city,
    institution_type
from institutions;

alter table dim_institution
add primary key (institution_id);


-- ==========================================
-- 3. dim_company
-- ==========================================

create table dim_company as
select
    company_id,
    company_name,
    industry,
    company_size,
    headquarters
from companies;

alter table dim_company
add primary key (company_id);


-- ==========================================
-- 4. dim_job
-- ==========================================

create table dim_job as
select
    job_id,
    company_id,
    job_title,
    location,
    experience_level,
    salary_min_lpa,
    salary_max_lpa,
    posted_date,
    skill_count
from job_descriptions_skills;

alter table dim_job
add primary key (job_id);


-- ==========================================
-- 5. dim_skill
-- ==========================================

create table dim_skill as
select distinct
    standardized_skill as skill_name
from job_skills
where standardized_skill is not null
  and trim(standardized_skill) <> '';

alter table dim_skill
add primary key (skill_name);


-- ==========================================
-- 6. dim_date
-- ==========================================

-- increase recursive cte limit
set session cte_max_recursion_depth = 5000;
create table dim_date (
    date_id date primary key,
    year int,
    quarter int,
    month_number int,
    month_name varchar(20),
    day_number int,
    day_name varchar(20),
    week_number int
);
-- populate date dimension
insert into dim_date (
    date_id,
    year,
    quarter,
    month_number,
    month_name,
    day_number,
    day_name,
    week_number
)
with recursive date_series as (
    select date('2020-01-01') as calendar_date

    union all

    select date_add(calendar_date, interval 1 day)
    from date_series
    where calendar_date < '2030-12-31'
)
select
    calendar_date,
    year(calendar_date),
    quarter(calendar_date),
    month(calendar_date),
    monthname(calendar_date),
    day(calendar_date),
    dayname(calendar_date),
    week(calendar_date)
from date_series;
show tables;

select 'dim_student' as table_name, count(*) as total_records from dim_student
union all
select 'dim_institution', count(*) from dim_institution
union all
select 'dim_company', count(*) from dim_company
union all
select 'dim_job', count(*) from dim_job
union all
select 'dim_skill', count(*) from dim_skill
union all
select 'dim_date', count(*) from dim_date;

select count(*) as total_dates,
       min(date_id) as start_date,
       max(date_id) as end_date
from dim_date;
