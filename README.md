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

### mongodb and pymongo usage
[installation link](https://docs.mongodb.com/manual/installation/)

[tutorial link](http://api.mongodb.com/python/current/tutorial.html)

1. Install mongodb Community Edition (use installation link for instructions)
    - this will be the most difficult part of the process
    - *Important* make sure you can start mongo server through mongod.exe
        - control c will stop the server
    - and then connect to server through mongo.exe
    - once connected you should see a prompt that reads something like
        ```
        MongoDB shell version: 3.0.4
        connecting to: test
        >
        ```
    - create a new db -> `use nhl_ml`
        - you have to name it "nhl_ml" because our python file looks for that exact db
    - make sure your in the nhl_ml db -> `db`
        - should output name of db your using (should be nhl_ml)
        - if not simply write `use nhl_ml` again
    - then create collection `db.createCollection("first_test")`
        - again: python is looking for that exact collection
    - sweet your good to go! We'll only go into the mongo shell again to make new dbs and collections (or if there's issues)
    - type `exit` to get out of mongo shell
2. `pip install pymongo` -> installs python mongo package onto your local machine for access functionality
3. review mong_fns file and [pymong and mongodb docs](https://docs.mongodb.com/getting-started/python/client/) to get a feel for what's happening
4. First run access.py with `Data_dbImport` uncommented and `Data_dbRead` commented out
5. Comment out `Data_dbImport` and Api lines to read newly imported data
6. Remove Data -> Comment out everything except `Data_Remove` and imports

### Next Steps
1. Play with api and see what data we can get
2. Learn the structure of mongoDB (Collections, Documents, Schemas, ex cetera)
2. Plan out structure of data we want for test, train, and learn data sets
    - the three sets will be identically structured just with different data
    - I'm going to look into the best ways we can structure data for algorithm which finds classifications for best prediction results


Call, Email, or text if ya got any questions :smiley:
