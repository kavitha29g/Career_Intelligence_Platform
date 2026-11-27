show tables;

select 'students_master' as table_name, count(*) as total_records from students_master
union all
select 'technical_assessments', count(*) from technical_assessments
union all
select 'programming_assessments', count(*) from programming_assessments
union all
select 'communication_assessments', count(*) from communication_assessments
union all
select 'attendance_training', count(*) from attendance_training
union all
select 'mock_interviews', count(*) from mock_interviews
union all
select 'historical_placements', count(*) from historical_placements
union all
select 'student_job_applications', count(*) from student_job_applications;

select
    table_name,column_name,column_type,is_nullable,column_key,extra
from information_schema.columns
where table_schema = 'career_intelligence'
order by table_name, ordinal_position;


-- 1. institutions
alter table institutions
modify institution_id varchar(50),
modify institution_name varchar(255),
modify city varchar(100),
modify institution_type varchar(100);


-- 2. students_master
alter table students_master
modify student_id varchar(50),
modify institution_id varchar(50),
modify batch_id varchar(50),
modify degree varchar(100),
modify department varchar(100),
modify placement_status varchar(50),
modify cgpa decimal(4,2),
modify expected_salary_lpa decimal(10,2);


-- 3. student_institution
alter table student_institution
modify student_id varchar(50),
modify institution_id varchar(50),
modify batch_id varchar(50),
modify degree varchar(100),
modify department varchar(100),
modify placement_status varchar(50),
modify institution_name varchar(255),
modify city varchar(100),
modify institution_type varchar(100),
modify cgpa decimal(4,2),
modify expected_salary_lpa decimal(10,2);


-- 4. technical_assessments
alter table technical_assessments
modify student_id varchar(50);


-- 5. programming_assessments
alter table programming_assessments
modify student_id varchar(50),
modify assessment_date date;


-- 6. communication_assessments
alter table communication_assessments
modify student_id varchar(50),
modify verbal_score int;


-- 7. attendance_training
alter table attendance_training
modify student_id varchar(50),
modify training_completion_pct decimal(5,2),
modify attendance_pct decimal(5,2);


-- 8. mock_interviews
alter table mock_interviews
modify student_id varchar(50),
modify mock_interview_date date;


-- 9. companies
alter table companies
modify company_id varchar(50),
modify company_name varchar(255),
modify industry varchar(100),
modify company_size varchar(50),
modify headquarters varchar(255);


-- 10. job_descriptions_skills
alter table job_descriptions_skills
modify job_id varchar(50),
modify company_id varchar(50),
modify job_title varchar(255),
modify location varchar(255),
modify experience_level varchar(100),
modify salary_min_lpa decimal(10,2),
modify salary_max_lpa decimal(10,2),
modify description text,
modify required_skills text,
modify posted_date date,
modify extracted_skills text;


-- 11. job_skills
alter table job_skills
modify job_id varchar(50),
modify skill varchar(100),
modify standardized_skill varchar(100);


-- 12. company_requirements
alter table company_requirements
modify company_id varchar(50),
modify job_title varchar(255),
modify required_skills text,
modify minimum_cgpa decimal(4,2),
modify salary_lpa decimal(10,2);


-- 13. student_job_applications
alter table student_job_applications
modify application_id varchar(50),
modify student_id varchar(50),
modify job_id varchar(50),
modify company_id varchar(50),
modify application_date date,
modify application_status varchar(100);


-- 14. historical_placements
alter table historical_placements
modify placement_id varchar(50),
modify student_id varchar(50),
modify company_id varchar(50),
modify job_title varchar(255),
modify placement_date date,
modify offered_salary_lpa decimal(10,2),
modify placement_type varchar(100),
modify offer_status varchar(100);


-- 15. job_salary_roles
alter table job_salary_roles
modify job_role varchar(255),
modify salary_min_lpa decimal(10,2),
modify salary_max_lpa decimal(10,2),
modify job_category varchar(100);


-- 16. student_performance
alter table student_performance
modify student_id varchar(50),
modify institution_id varchar(50),
modify batch_id varchar(50),
modify degree varchar(100),
modify department varchar(100),
modify placement_status varchar(50),
modify cgpa decimal(4,2),
modify expected_salary_lpa decimal(10,2),
modify training_training_completion_pct decimal(5,2),
modify training_attendance_pct decimal(5,2),
modify technical_assessment_date date,
modify programming_assessment_date date,
modify interviews_mock_interview_date date;

select
    table_name,
    column_name,
    column_type
from information_schema.columns
where table_schema = 'career_intelligence'
order by table_name, ordinal_position;

-- parent tables
alter table institutions
add primary key (institution_id);

alter table students_master
add primary key (student_id);

alter table companies
add primary key (company_id);

alter table job_descriptions_skills
add primary key (job_id);

-- student profile / integrated tables
alter table student_institution
add primary key (student_id);

alter table student_performance
add primary key (student_id);

-- student assessments
alter table technical_assessments
add primary key (student_id);

alter table programming_assessments
add primary key (student_id);

alter table communication_assessments
add primary key (student_id);

alter table attendance_training
add primary key (student_id);

alter table mock_interviews
add primary key (student_id);

-- job applications
alter table student_job_applications
add primary key (application_id);

-- placement records
alter table historical_placements
add primary key (placement_id);

-- job skills
alter table job_skills
add primary key (job_id, skill);

-- students master -> institutions
alter table students_master
add constraint fk_students_institution
foreign key (institution_id)
references institutions(institution_id);

-- student institution -> students master
alter table student_institution
add constraint fk_student_institution_student
foreign key (student_id)
references students_master(student_id);

-- student institution -> institutions
alter table student_institution
add constraint fk_student_institution_institution
foreign key (institution_id)
references institutions(institution_id);

-- student performance -> students master
alter table student_performance
add constraint fk_performance_student
foreign key (student_id)
references students_master(student_id);

-- student performance -> institutions
alter table student_performance
add constraint fk_performance_institution
foreign key (institution_id)
references institutions(institution_id);

-- technical assessments -> students master
alter table technical_assessments
add constraint fk_technical_student
foreign key (student_id)
references students_master(student_id);

-- programming assessments -> students master
alter table programming_assessments
add constraint fk_programming_student
foreign key (student_id)
references students_master(student_id);

-- communication assessments -> students master
alter table communication_assessments
add constraint fk_communication_student
foreign key (student_id)
references students_master(student_id);

-- training -> students master
alter table attendance_training
add constraint fk_training_student
foreign key (student_id)
references students_master(student_id);

-- mock interviews -> students master
alter table mock_interviews
add constraint fk_mock_student
foreign key (student_id)
references students_master(student_id);

-- job descriptions -> companies
alter table job_descriptions_skills
add constraint fk_job_company
foreign key (company_id)
references companies(company_id);

-- job skills -> job descriptions
alter table job_skills
add constraint fk_job_skills_job
foreign key (job_id)
references job_descriptions_skills(job_id);

-- job applications -> students
alter table student_job_applications
add constraint fk_application_student
foreign key (student_id)
references students_master(student_id);

-- job applications -> jobs
alter table student_job_applications
add constraint fk_application_job
foreign key (job_id)
references job_descriptions_skills(job_id);

-- job applications -> companies
alter table student_job_applications
add constraint fk_application_company
foreign key (company_id)
references companies(company_id);

-- historical placements -> students
alter table historical_placements
add constraint fk_placement_student
foreign key (student_id)
references students_master(student_id);

-- historical placements -> companies
alter table historical_placements
add constraint fk_placement_company
foreign key (company_id)
references companies(company_id);

-- company requirements -> companies
alter table company_requirements
add constraint fk_requirements_company
foreign key (company_id)
references companies(company_id);

select
    table_name,
    constraint_name,
    constraint_type
from information_schema.table_constraints
where table_schema = 'career_intelligence'
order by table_name, constraint_type;

select
    table_name,
    column_name,
    constraint_name,
    referenced_table_name,
    referenced_column_name
from information_schema.key_column_usage
where table_schema = 'career_intelligence'
  and referenced_table_name is not null
order by table_name;
