import json
from gash import get_project_branches
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def gash():
    projects = get_project_branches()
    enviros_header = set([i for s in [list(v.keys()) for k,v in projects.items()] for i in s])
    return render_template('gash.html', enviros_header=enviros_header, projects=projects)
    #return json.dumps(project_branches)

if __name__ == "__main__":
    app.run()
