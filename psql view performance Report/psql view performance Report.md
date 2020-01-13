simple aggregate sum() group by cashflow account\_from 

datasize 600000

**create**
![create.png](resources/078C6E58E33C38D7E9CA027871D6880E.png =460x345)

**select**
![read_view.png](resources/7B5543F20E21AA0D8B08DAED809D5C51.png =460x345)

model DDL
```SQL
-- auto-generated definition
create table dbview_cashflow
(
  id           serial           not null
    constraint dbview_cashflow_pkey
      primary key,
  date         date,
  p1           double precision not null,
  company_from varchar(63)      not null,
  company_to   varchar(63)      not null
);

alter table dbview_cashflow
  owner to postgres;
```

view DDL
```
create materialized view tempweek as
SELECT t.company_from,
       sum(t.p1) AS sum
FROM dbview_cashflow t
GROUP BY t.company_from;

alter materialized view tempweek owner to postgres;
```

django settings
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'testpsql2020',
        'HOST': 'localhost',
        'PORT': '54322',
    }
}
```

docker psql
```
docker run --name dockerPG11 -e POSTGRES_PASSWORD=testpsql2020 -p 54322:5432 -d postgres:11.5
```