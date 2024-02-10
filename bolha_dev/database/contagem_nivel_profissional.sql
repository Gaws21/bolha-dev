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


SCHEMA_COUNTER as (
select title, job_id, 
CASE 
when title like "s%nior%" then "Senior" 
when title like "%s%nior%" then "Senior" 
when title like "%s%nior" then "Senior" 
when title like "%principal%" then "Senior" 
when title like "%lead%" then "Senior" 
when title like "% SR %" then "Senior" 
when title like "SR%" then "Senior"
when title like "%SR" then "Senior" 
when title like "%manager%" then "Senior"
when title like "%rchitec%" then "Senior"
when title like "%xper%" then "Senior"
when title like "%spec%" then "Senior"
when title like "%l%der%" then "Senior"
when title like "Pleno%" then "Pleno" 
when title like "%Pleno%" then "Pleno" 
when title like "% PL %" then "Pleno"
when title like "% PL" then "Pleno"
when title like "%Pleno" then "Pleno"
when title like "mid%level%" then "Pleno" 
when title like "%mid%level%" then "Pleno" 
when title like "%mid%level" then "Pleno" 
when title like "junior%" then "Junior" 
when title like "%junior%" then "Junior" 
when title like "%junior" then "Junior" 
when title like "%est%gi%" then "Junior" 
when title like "%jr.%" then "Junior" 
when title like "%pecialist%" then "Especialista" 

else "Não Especificado"
end as attr
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
