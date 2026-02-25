from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/join', methods=['POST'])
def join():
    name = request.form.get('name')
    email = request.form.get('email')
    plan = request.form.get('plan')

    return f"""
    <h2>Thank You {name}!</h2>
    <p>You have successfully joined the {plan} plan.</p>
    <p>We will contact you at {email} soon.</p>
    <a href="/">Go Back</a>
    """

if __name__ == '__main__':
    app.run(debug=True)

