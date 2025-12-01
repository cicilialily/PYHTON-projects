from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def index():
    # Get the name parameter from the query string
    name = request.args.get('name', 'Nobody')

    # Determine the greeting message
    if name:
        greeting = f"Hello, {name}"
    else:
        greeting = "Hello World"

    # Render the template with the greeting
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
