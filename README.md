# sqlite_view_performance


###start project
**python version**
```bash
Python 3.6.4
```
**install requirements**
```bash
pip install -r requirements.txt
```
**script for django makemigrations and migrate**
```bash
chmod +x mm.sh
./mm.sh
```

####utils
some helper functions

####scripts
script for insert data into database
script for select data fromn view

####ViewDDL
```SQL
CREATE VIEW temp_date AS
SELECT company_from, company_to, sum(p1)
FROM dbview_cashflow
group by date;
```