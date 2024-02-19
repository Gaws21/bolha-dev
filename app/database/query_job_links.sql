delete from job_link where title is not null;

with DAY_COLLECT AS (select * from engenheiro_de_dados_sao_paulo
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

MAX_CREATE_DATE AS (
 select max(create_date) from DAY_COLLECT
),

JOB_LINKS AS (
	select
		"https://www.linkedin.com/jobs/view/" || job_id as url_id,
		title
	from DAY_COLLECT
	where company not in ("Netvagas","GeekHunter","Turing","Croosover")
	and create_date = (select * from MAX_CREATE_DATE)
)

insert into job_link select distinct url_id, title from JOB_LINKS