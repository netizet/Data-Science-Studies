from flask import Flask, render_template

Dashboard_Final_Project = Flask(__name__)

@Dashboard_Final_Project.route('/')
def home():
    return render_template('Final Project.html')

if __name__ == '__main__':
    Dashboard_Final_Project.run(debug=True)