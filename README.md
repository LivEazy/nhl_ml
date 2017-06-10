# nhl_ml
practicing machine learning

### api access setup
- create file called "api_acess.py"
```python
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"
```

Then access.py already imports those variables from that file,
so you should be good to go :thumbsup:

Also the .gitignore file is set to hide that file and .pyc files which are created from the import usage :thumbsup:

### helpful git tips
1. add files
2. commit files
3. push files

`git add -A` -> adds all files to be committed

`git commit -m` -> commits files with message

`git push -u origin master` -> on first time pushing to repo, then just use `git push`.

If i've pushed something up and you want those changes:
1. Make sure you have a clean repo meaning
    - All your uncommitted changes are added, committed, and pushed
2. run `git pull` -> pulls github repo files to your local machine git repository

We'll talk more git details as the project grows (branches and etc)
