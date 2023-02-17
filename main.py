from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
post = Post().all_posts

@app.route('/')
def home():
    # post_url = "https://api.npoint.io/c790b4d5cab58020d391"
    # post_response = requests.get(post_url)
    # all_posts = post_response.json()
    all_posts = post
    return render_template("index.html", posts=all_posts)

@app.route('/post/<post_id>')
def enter_post(post_id):
    post_json = post[int(post_id)-1]
    
    return render_template('post.html', post_json=post_json)

if __name__ == "__main__":
    app.run(debug=True)
