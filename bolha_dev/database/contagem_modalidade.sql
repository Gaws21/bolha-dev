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

MAX_CREATE_DATE AS (
 select max(create_date) from DAY_COLLECT
),

SCHEMA_COUNTER as (
select title, location, job_id, 
CASE 
	when trim(substr(location,-1,-6)) = "Remoto" then "Remoto"
	when trim(substr(location,-1,-10)) = "Presencial" then "Presencial"
	when trim(substr(location,-1,-7)) = "Híbrido" then "Hibrido"
else "Não Especificado" end as attr
from DAY_COLLECT
where create_date = (select * from MAX_CREATE_DATE)
),

ROW_NUMBERS AS (
	select *, row_number() over(partition by job_id) as row_numbers from SCHEMA_COUNTER
),

--select distinct * from SCHEMA_COUNTER where attr is null
FINAL_COUNTER as (
	select attr, row_numbers, count() over(partition by attr) as count_attr from ROW_NUMBERS
	where row_numbers = 1
)

select distinct attr, count_attr from FINAL_COUNTER
where row_numbers = 1
order by count_attr desc
-- where nivel_profissional is not null
-- order by count_obj desc
-- limit 3