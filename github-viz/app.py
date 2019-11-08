from flask import Flask, request
from flask import render_template
import sys
from commits_drill import CommitsDrill
from issues_drill import IssuesDrill


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def select_usecases():
    return render_template("select_usecases.html")


@app.route('/select_repo', methods=['GET', 'POST'])
def select_repo():
    global user_usecase
    user_usecase = request.form.get('uc_select_button')
    return render_template("select_repo.html", user_repo=user_usecase)


@app.route('/usecases', methods=['GET', 'POST'])
def usecases():
    user_repos = request.form.getlist('repositories[]')
    print(user_repos, sys.stderr)
    if user_usecase == 'Commits':
        cd = CommitsDrill()
        cd.commits(user_repos)
        return render_template('embed_links/usecase_commits.html')
    elif user_usecase == 'Issues':
        i = IssuesDrill()
        i.list_all_issues(user_repos)
        return render_template('embed_links/usecase_issues.html')
    else:
        return render_template('embed_links/usecase_libraries.html')
    return render_template("usecases.html", input=user_repos, ip2=user_usecase)


if __name__ == '__main__':
    app.run()
