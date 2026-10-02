# Author: Mukul Kumar
# Date: 9/30/2026
# Name: app.py
# Description: runs the flask app and shows the payroll page on / and /payroll


from flask import Flask, render_template
from payroll.payroll import build_payroll_data
app = Flask(__name__)


@app.route('/')
@app.route('/payroll')
def pay_roll():
    data = build_payroll_data()
    return render_template('payroll.html', data=data)


if __name__ == '__main__':
    app.run()
