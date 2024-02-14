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

SCHEMA_COUNT AS (
	select count(create_date) as count_attr, "Total Coletado" as attr from DAY_COLLECT where create_date = (select * from MAX_CREATE_DATE)
	union all 
	select count(distinct job_id) as count_attr, "Vagas Unicas" as attr from DAY_COLLECT where create_date = (select * from MAX_CREATE_DATE)
	union all 
	select count(distinct job_id) as count_attr, "Vagas Relevantes" as attr from DAY_COLLECT where create_date = (select * from MAX_CREATE_DATE)
	and (
		title like "%ytho%" or 
		title like "%data%engineer%" or
		title like "%engenh%dados%"  or
		title like "%etl%"  or
		title like "engenh%dados%"
	)
)

select attr, count_attr from SCHEMA_COUNT
order by count_attr desc 

