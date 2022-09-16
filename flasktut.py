from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
    'author':'Robin',
    'title': 'why i love merel das',
    'content': 'cuz she prettyyy',
    'date_posted': 'September 20, 2022'
    },
    {
    'author':'Merel',
    'title': 'why robin really cool',
    'content': 'cuz he prettyyy',
    'date_posted': 'September 20, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('mereldas.html',title="Merel Das Page!!!!!!");
    #return render_template('home.html', posts=posts);
    
@app.route("/mereldas") 
def mereldas():
    return render_template('mereldas.html',title="Merel Das Page!!!!!!");

@app.route("/about")
def about():
    return render_template('about.html', title = "About");

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")