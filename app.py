from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/audios")
def audios():
    return render_template("audios.html")

@app.route("/blogs")
def blogs():
    # Sample data to populate the blogs page (Latest article is displayed first via Jinja reverse filter)
    blog_posts = [
        {
            'title': 'The Light of Guidance',
            'description': 'Understanding how divine guidance leads to inner peace and truth...',
            'url': '#'
        },
        {
            'title': 'Spiritual Healing',
            'description': 'Exploring the power of words, prayers, and remembrance in healing the soul...',
            'url': '#'
        },
        {
            'title': 'The Secret of the Self',
            'description': 'A journey into recognizing the divine essence within, as taught in Sufi wisdom.',
            'url': '#'
        }
    ]
    return render_template('blogs.html', posts=blog_posts, section_title='Our Spiritual Blogs')

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)