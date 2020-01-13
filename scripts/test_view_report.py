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
