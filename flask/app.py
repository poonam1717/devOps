from flask import Flask
app=Flask(__name__)
@app.route('/')
def myapp():
    return """<h1>Hello welcome to login page</h1>
                <form>
                First name:<br>
                <input type="text" name="firstname"><br>
                 Last name:<br>
                <input type="text" name="lastname">
                <input type="submit" value="Submit">
</form>"""
if __name__=="__main__":
    app.run(debug=True , host="0.0.0.0")
