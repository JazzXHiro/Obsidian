**When you initialize a git project it creates a hidden git directory in your folder if you want to completely remove the git you can use:** **rm -rf .git**
 
**gitignore file -** **basically you don't want everything in source control, you definitely wanna keep out some sensitive private api keys, source code for your dependencies like the source code for node modules and any unnecessary log files. git will automatically look at this git ignore file and filter out anything that matches the file path or pattern.**
 
**git add .**  
**git remove.**  
**git remove --hard** **- removes the file and deletes everything**  
**git commit -m "your message"**
 
**git branch** **- to check the current branch**  
**git checkout -b feature** **- git checkout switches to a mentioned branch and -b creates a new branch named 'feature'**  
**git stash -u** **- if you are working on something that's half finished or experimental and you don't wanna commit them you can just save them using git stash**  
**git stash pop/apply** **- to delete or apply the changes stored in the stash**
 
**To merge a branch with another branch:****￼****a) checkout the master branch or whatever branch you want**

1. **git merge** **namoofthebranchtomerge**

**commit id becomes the same for both of the branches after merging**  
**Merge conflicts - merging is most likely where you will run into problems because you might be working on a feature branch and then master branch has changes that eventually lead to merge conflicts**

![Exported image](7%20-%20Attachments/Exported%20image%2020250526133508-0.png)

**On the left we have a line of code that we implemented in the feature branch and on the right we have a line of code that happened in the master branch while we were working that affected the same line of code so merging these files is not possible out of the box because git doesn't know which change to use. VS Code will give you some options to resolve these conflicts. You will need to fix the file manually**
 
**Always make small commits**
 
**A lot of times on a feature branch you will create a lot of commits and these commits are kinda irrelevant to what's going on in the master branch. You can see that our feature branch is 3 commits ahead of our master branch and it has a bunch of comments about including a bunch of useless emotes. Instead of merging all these commits into the master branch you can use the squash flag** **git merge feature --squash** **to squash them down into a single commit when you do your merge. This will keep the master branch nice and concise while also preserve all of the commits in the feature branch itself.**

![Exported image](7%20-%20Attachments/Exported%20image%2020250526133513-1.png)

**when you merge with the squash flag it won't really change the head commit in the master branch so you will need to add in an additional commit that says something like "merged in feature branch".**
 
**git remote** **- that will connect our local code to the remote repository**  
**git push -u origin master -** **this will push the files to remote repository**
 
**How to take someone's existing code, fork it, create some changes and create a pull request to merge your code into another person's project.**
 
**Forking** **will copy the code and make it a repo under your own github account. After you fork it, you would wanna clone your code to the local machine to start making changes to it.**  
**The git clone command** **just allows you to copy a code from a remote repository to your local computer. Once you have it on you have that cloned you can open it up in VS Code**  
**make a new branch**  
**npm run address** **when you are done it will print out an encrypted base 64 string. From their you will go into the directory and create a new file that's your github_username.txt and then you will copy and paste that encoded string into that file. Just a side note on security, your address is going into a public repo but it's encrypted with the RSA Algorithm. This means that someone is able to encrypt data with the public key but I am the only one with the private key that can decrypt it. Hacking the private key is essentially impossible unless someone physically steals your private key your address should be safe in this public format.****￼****Now we have all the necessary changes in our local machine now we will need to push this to the remote fork -** **git push origin** **branch_name.** **On github you will see an option to pull request. A pull request is just like a merge but it has the additional step of needing to pull the remote changes. In other words a pull request is saying I am pulling the remote changes and then merging them into the master branch.**