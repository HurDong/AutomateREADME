# library install(pip install gitpython)
import git

# write your information
userName = 'HurDong'
repository = 'Algorithm'

# config remote repo
branch = 'tree/main'
url = f'https://github.com/{userName}/{repository}'
link = f'{url}/{branch}'

# config local repo
localDir = 'C:\Users\ehd_a\Desktop\PROGRAMMING\ALGORITHM\' + repository
repo = git.Repo(localDir)

def pull():
    # Pull repo
    print('...pull')
    repo.remotes.origin.pull()

def push():
    print('...push')
    repo.index.add('README.md')
    repo.index.commit('Update README.md')
    repo.remotes.origin.push()
