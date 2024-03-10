#!/usr/bin/python3
"""Flask app to start application"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():
    """Main route"""
    return render_template('index.html')

@app.route('/projects')
def project():
    """Project route"""
    return render_template('projects.html')

@app.route('/blogs')
def blog():
    """Blogs route"""
    return render_template('blogs.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
