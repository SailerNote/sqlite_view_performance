simple aggregate sum() group by cashflow account_from 

datasize 600000

ModelDLL

```SQL
-- auto-generated definition
create table dbview_cashflow
(
  id           integer     not null
    primary key autoincrement,
  p1           real        not null,
  company_from varchar(63) not null,
  company_to   varchar(63) not null,
  date         date
);
```

ViewDDL
```SQL
CREATE VIEW temp_week AS
SELECT company_from, company_to, sum(p1)
FROM dbview_cashflow
group by company_from;
```


insert perforance
![insert.jpg](resources/780656B22FAF53D59E8F6B60D970BEEF.png =640x480)

select performance
![read.jpg](resources/780656B22FAF53D59E8F6B60D970BEEF.png =640x480)

in one graph
![IMAGE](resources/B9666D26512D9E66E354B7B02C2EE180.jpg =640x480)

part source code
```
import time
import random
from functools import wraps

from dbview.models import CashFlow
from dbview.models import TempWeek
from utils.pickle_helper import load_variable
from utils.pickle_helper import save_variable
from progress.bar import Bar

companies_from = ['company_{}'.format(i) for i in range(1, 100)]
companies_to = ['company_{}'.format(i) for i in range(1, 100)]
ps = [random.randint(100, 1000) for _ in range(100)]


def timing(func):
    """
    计时装饰器
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        装饰函数
        """
        start = time.clock()
        r = func(*args, **kwargs)
        end = time.clock()
        return end - start

    return wrapper


@timing
def create():
    CashFlow.objects.create(
        company_from=random.choice(companies_from),
        company_to=random.choice(companies_to),
        p1=random.choice(ps)
    )


@timing
def get_from_view():
    cf = [TempWeek.objects.all()]
    del cf


def run():
    print('start gen')
    report = []
    bar = Bar('Processing', max=600000)
    for _ in range(600000):
        report.append((create(), get_from_view()))
        bar.next()
    bar.finish()
    print('finish gen')
    print('start save time performance into pickle')
    save_variable(report, './data.report')
    print('finish save time performance into pickle')
```

github https://github.com/SailerNote/sqlite_view_performance