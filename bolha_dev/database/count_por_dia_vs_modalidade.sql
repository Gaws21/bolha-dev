with DAY_COLLECT AS (
select * from engenheiro_de_dados_sao_paulo
UNION
select * from data_engineer_sao_paulo
UNION
select * from programador_python_sao_paulo
UNION
select * from desenvolvedor_python_sao_paulo
UNION
select * from python_desenvolvedor_sao_paulo
UNION
select * from python_programador_sao_paulo
UNION
select * from python_developer_sao_paulo
UNION
select * from engenheiro_de_dados_brasil_remoto
UNION
select * from data_engineer_brasil_remoto
UNION
select * from programador_python_brasil_remoto
UNION
select * from desenvolvedor_python_brasil_remoto),

UNION_TABLES AS (
	select create_date, job_id, title, company, location, publish_time from DAY_COLLECT
	UNION ALL
	select * from LinkedinJobs
),

ROW_NUMBERS AS (
	select *, row_number() over(partition by job_id) as row_numbers from UNION_TABLES
),

UNIQUE_ROWS AS (
 select * from ROW_NUMBERS where row_numbers = 1
),

PRE_PIVOT_TABLE AS (
select count_day, create_date, modalidade, count() as counter from 
(select create_date,
count() over(partition by create_date) as count_day,
case 
		when trim(substr(location,-1,-6)) = "Remoto" then "Remoto"
		when trim(substr(location,-1,-10)) = "Presencial" then "Presencial"
		when trim(substr(location,-1,-7)) = "Híbrido" then "Hibrido"
		else "Remoto" end as modalidade
 from UNIQUE_ROWS
 where row_numbers = 1
 ) as b
 group by create_date, modalidade)
 
 select
 create_date, count_day, 
 max(counter) filter(where modalidade = "Hibrido") as hibrido, 
 max(counter) filter(where modalidade = "Presencial") as presencial, 
 max(counter) filter(where modalidade = "Remoto") as remoto
 from PRE_PIVOT_TABLE
 group by create_date
 order by create_date asc 