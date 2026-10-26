from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        department = request.form.get("department", "").strip()
        if not name or not department:
            return "<h3>Please fill in all fields.</h3>"
        return f"""
        <h2>Student Details</h2>
        <p>Name: {name}</p>
        <p>Department: {department}</p>
        """
    return """
    <h2>Student Management System</h2>
    <form method="POST">
        Student Name: <input name="name" required><br><br>
        Department: <input name="department" required><br><br>
        <button type="submit">Submit</button>
    </form>
    """
if __name__ == "__main__":
    app.run(debug=True)
