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
when title like "%ytho%" then "python" 
when title like "%php%" then "php"
when title like "%react%" then "react"
when title like "% BI %" then "BI"
when title like "%business%intelligence%" then "BI"
when title like "%devops%" then "devops" 
when title like "%.net%" then "dotnet"
when title like "%dotnet%" then "dotnet"
when title like "% go %" then "go"
when title like "%olang%" then "golang"
when title like "%kotlin%" then "kotlin"
when title like "%rust%" then "rust"
when title like "%elixir%" then "elixir"
when title like "%java%" then "java"
when title like "%ruby%" then "ruby"
when title like "%C++%" then "C++"
when title like "% C %" then "C"
when title like "% C# %" then "C#"
when title like "%DBA%" then "DBA"
when title like "%sap%" then "sap"
when title like "%cobol%" then "cobol"
when title like "%angular%" then "angular"
when title like "%flutter%" then "flutter"
when title like "%SQL%" then "SQL"
when title like "%node%" then "java script"
when title like "%quality%" then "qa"
when title like "%tester%" then "qa"
when title like "%QA%" then "qa"
when title like "QA%" then "qa"
when title like "%ios%" then "ios"
when title like "%android%" then "android"
when title like "%mobile%" then "mobile"
when title like "%salesforce%" then "salesforce"
when title like "%data%engineer%" then "engenheiro de dados"
when title like "%engenh%dados%" then "engenheiro de dados"
when title like "%etl%" then "engenheiro de dados"
when title like "engenh%dados%" then "engenheiro de dados"
when title like "engenh%software%" then "software engineer"
when title like "engenh%sistemas%" then "software engineer"
when title like "%software%engineer%" then "software engineer" 
when title like "%engenheir%software" then "software engineer"
when title like "engenh%aplicaoes%" then "software engineer"
when title like "%analista%" then "analista" 
when title like "%analyst%" then "analista"
when title like "%analyt%" then "analista"
when title like "%est%gi%" then "estagio"
when title like "%data%scien%" then "cientista de dados"
when title like "%cientist%dados%" then "cientista de dados"
when title like "%machine%learning%" then "cientista de dados"
when title like "% AI %" then "AI"
when title like "%linux%" then "linux"
when title like "%full%stack%" then "full stack"
when title like "%front%end%" then "front end"
when title like "%solutions%engineers%" then "engenheiro de solucoes"
when title like "%infra%structure%" then "infra"
when title like "%network%engin%" then "infra"
when title like "%support%" then "suporte"
when title like "%suporte%" then "suporte"
when title like "%arquitet%" then "arquiteto"
when title like "%architect%" then "arquiteto"
when title like "%automation%" then "automacao"
when title like "%CRM%" then "crm"
when title like "%back%end%" then "backend"
when title like "%mlops%" then "mlops"
when title like "%cloud%" then "cloud"
when title like "%LLM%" then "AI"
when title like "%NLP%" then "AI"
when title like "%game%" then "game"
when title like "%sre%" then "sre" 
when title like "%Adops%" then "Adops"
when title like "%cyber%" then "seguranca"
when title like "%tech%lead%" then "tech lead"
when title like "l%der%t%cnico%" then "tech lead"
when title like "%team%lead%" then "tech lead"
when title like "%lead%" then "lider"
when title like "%databricks%" then "cloud"
when title like "%data%developer%" then "dados"
when title like "%data%" then "dados"
when title like "%database%" then "DBA"
when title like "%consult%" then "consultor"
when title like "%coordenador%" then "consultor"
when title like "%pecialist%" then "especialista"
when title like "Espec%" then "especialista"
when title like "%expert%" then "especialista"
when title like "%manage%" then "gerente"
when title like "%plataform%" then "plataforma"
when title like "%research%" then "pesquisador"
when title like "%executivo%" then "executivo"
when title like "%Prompt%Engineer%" then "prompt engineer"
when title like "%enginee%" then "engenheiro"
when title like "%engenh%" then "engenheiro"
when title like "%ssistente %" then "assistente" 
when title like "%development%" then "desenvolvedor"
when title like "Developer%" then "desenvolvedor"
when title like "%developer%" then "desenvolvedor"
when title like "%developer%" then "desenvolvedor"
when title like "%desenvolvedor%" then "desenvolvedor"
when title like "%desenvolvimento%" then "desenvolvedor"
else title 
end as attr 
from DAY_COLLECT
where create_date = (select * from MAX_CREATE_DATE)
-- where create_date = date("now")
),

ROW_NUMBERS AS (
	select *, row_number() over(partition by job_id) as row_numbers from SCHEMA_COUNTER
	-- where attr is null
),

UNIQUE_ROWS AS (
	select * from ROW_NUMBERS where row_numbers = 1
),

COUNTER_ATTR AS (
	select *, count() over(partition by attr) as count_attr from UNIQUE_ROWS
)

select distinct attr, count_attr from COUNTER_ATTR order by count_attr desc limit 10
