def print_git():
    print(f'From Git Bash: ')
    print(f'ssh-keygen -o')
    for _ in range(10):
        print(f'==', end="")
    print()

    print(f'Add pub key to Github, create remote repo on Github, create branches, copy git repo')
    print(f'From Pycharm/Git Bash: ')
    print(f'git init')
    print(f'git config --global user.email "wangyiwenau@gmail.com"')
    print(f'git config --global user.name "yiwen"')
    print(f'git remote add test git@github.com:yiwenwangANU/test.git')
    print(f'git add .')
    print(f'git commit -m "commits"')
    print(f'git push --set-upstream test master')
    print(f'git branch dev')
    print(f'git checkout dev')
    print(f'git push --set-upstream test dev')
    print(f'git checkout master')
    print(f'git merge dev')


if __name__ == '__main__':
    print_git()