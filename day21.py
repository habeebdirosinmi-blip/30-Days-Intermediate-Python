from collections import Counter
import math

class Statistics:
    def __init__(My, data):
        My.data = data

    def count(My):
        return len(My.data)

    def sum(My):
        return sum(My.data)

    def min(My):
        return min(My.data)

    def max(My):
        return max(My.data)

    def range(My):
        return My.max() - My.min()

    def mean(My):
        return My.sum() / My.count()

    def median(My):
        sorted_data = sorted(My.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(My):
        counts = Counter(My.data)
        mode_val, mode_count = counts.most_common(1)[0]
        return {'mode': mode_val, 'count': mode_count}

    def var(My):
        m = My.mean()
        deviations = [(x - m) ** 2 for x in My.data]
        return sum(deviations) / My.count()

    def std(My):
        return round(math.sqrt(My.var()), 1)

    def freq_dist(My):
        counts = Counter(My.data)
        total = My.count()
        freq = [(round((count / total) * 100, 1), val) for val, count in counts.most_common()]
        return freq

    def describe(My):
        mode_data = My.mode()
        display_mean = round(My.mean())
        return (
            f"Count: {My.count()}\n"
            f"Sum: {My.sum()}\n"
            f"Min: {My.min()}\n"
            f"Max: {My.max()}\n"
            f"Range: {My.range()}\n"
            f"Mean: {display_mean}\n"
            f"Median: {int(My.median()) if My.median().is_integer() else My.median()}\n"
            f"Mode: ({mode_data['mode']}, {mode_data['count']})\n"
            f"Variance: {round(My.var(), 1)}\n"
            f"Standard Deviation: {My.std()}\n"
            f"Frequency Distribution: {My.freq_dist()}"
        )

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print(data.describe())
class PersonAccount:
    def __init__(My, firstname, lastname):
        My.firstname = firstname
        My.lastname = lastname
        My.incomes = set()  
        My.expenses = set()

    def add_income(My, description, amount):
        My.incomes.add((description, amount))

    def add_expense(My, description, amount):
        My.expenses.add((description, amount))

    def total_income(My):
        return sum(amount for desc, amount in My.incomes)

    def total_expense(My):
        return sum(amount for desc, amount in My.expenses)

    def account_balance(My):
        return My.total_income() - My.total_expense()

    def account_info(My):
        return (
            f"Account Holder: {My.firstname} {My.lastname}\n"
            f"Total Income: {My.total_income()}\n"
            f"Total Expense: {My.total_expense()}\n"
            f"Current Balance: {My.account_balance()}"
        )
account = PersonAccount("Habeeb", "Durosinmi")
account.add_income("Salary", 10000000)
account.add_income("Side Hustle", 150000)

account.add_expense("Rent", 400000)
account.add_expense("Food", 550000)

print(account.account_info())