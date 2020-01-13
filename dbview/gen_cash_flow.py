import os
import random
from dbview.models import CashFlow

companies_from = ['company_{}'.format(i) for i in range(1, 100)]
companies_to = ['company_{}'.format(i) for i in range(1, 100)]
ps = [random.randint() for _ in range(100)]


def foo(cf, ct, p):
    data = {
        'company_from': cf,
        'company_to': ct,
        'p1': p
    }
    return data


def main():
    data = foo(
        random.choice(companies_from),
        random.choice(companies_to),
        random.choice(ps)
    )
    for item in range(100):
        CashFlow.objects.create(data)


if __name__ == '__main__':
    main()
    print('done')
