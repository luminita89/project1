## Take away from git sesion 
*locals- creat a git repository : creat a folder, initiaizing git (tracking)
'''''git init
## add some files (text, python etc.) or update , add all files to tracking system (git)
git add .
git commint -m 'meaningful message that summirezes your changes'
# if you want to publish : creat repo in github, copy the url that ends with .git
git set-upstream original url
git push

#add files to '.gitignore' > exclude from tracking and publishing to the cloud repository
cat >> .gitignore
data/
mynotest.txt
## publish ignoring files or directories 
git push 

* Branching 
-git branch  # listing all existing branches 
-git branch new branch ## creat new branch
git checkout -b new branch # creating and switching to new branch
git checkout branch ## switching to the new branch


* working with git hub
- git clone url.git # clone brand new project from the cloud
- git push $ publish the changes from your local to the cloud
-git pull # get the updates from the cloud to the repository
