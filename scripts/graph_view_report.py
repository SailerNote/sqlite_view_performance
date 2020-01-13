import matplotlib.pyplot as plt

from utils.pickle_helper import load_variable

report_data = load_variable('data.report')
c1 = [item[0] for item in report_data]
r1 = [item[1] for item in report_data]

if __name__ == '__main__':
    plt.plot(range(len(c1)), c1)
    plt.plot(range(len(r1)), r1)
    plt.show()
