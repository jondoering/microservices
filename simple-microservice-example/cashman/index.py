#main file for RESTful example

from flask import Flask, jsonify, request

from cashman.model.expense import  Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import  TransactionType

app = Flask(__name__)

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('Pizza', 50),
    Expense('Concert', 100)
]

#GET for getting dcitoionary
@app.route("/incomes")
def get_income():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda x: x.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes.data)


#POST to append list of incomes
@app.route("/incomes", methods=['POST'])
def add_income():

    income = IncomeSchema().load(request.get_json())
    transactions.append(income.data)
    return '', 204

@app.route("/expenses")
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda x: x.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses.data)

@app.route("/expenses", methods=['POST'])
def add_expenses():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense.data)
    return '', 204

if __name__ == "__main__":
    app.run()