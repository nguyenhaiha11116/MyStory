from flask import Flask, render_template, request, redirect, url_for, session
from db import find_username, add_user, get_all, add_post, get_allposts
app = Flask(__name__)
# app.secret_key = 'abjhejkwiooo123123'

@app.route('/signup')
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods= ["POST"])
def post_signup():
    username = request.form.get('username')
    password = request.form.get('password')
    nick_name = request.form.get('nick_name')
    if find_username(username) == None:
        add_user(username,nick_name,password)
        return render_template('login.html')
    else:
        return redirect(url_for('get_signup'))

# posts = [
#     {
#         'author': '',
#         'title': '',
#         'content': '',
#         'date_posted': ''
#     },
#     {
#         'author': '',
#         'title': ' ',
#         'content': '',
#         'date_posted': ''
#     }
# ]

# @app.route("/home")
# def home():
#     return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/login', methods = ["POST"])
def post_login():
    username = request.form.get('username')
    password = request.form.get('password')
    # user = {
    #     'username':username,
    #     'password':password,
    # }

    if username == find_username(username)['username'] and password == find_username(username)['password']:
        return redirect (url_for('get_story'))
    return redirect (url_for('get_login'))

@app.route('/login')
def get_login():
    return render_template('login.html')

@app.route('/story')
def get_story():
    return render_template('layout.html',data = get_allposts())

@app.route('/story', methods = ["POST"])
def post_story():
    content = request.form.get('content')
    add_post(content)
    return render_template('layout.html',data = get_allposts())

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 