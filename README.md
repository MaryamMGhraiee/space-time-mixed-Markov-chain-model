# Getting Started
* Fork this repository to your personal Github's account (https://docs.github.com/en/get-started/quickstart/fork-a-repo)
* Go to the original repo and copy the `https` or `SSH` key that is displayed when you click on the `code` dropdown button
   * Github gives two options on how to push changes every time (i.e., using https or SSH). Pick the one you prefer.
* Clone the forked repo to your local machine (https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
* Open your command terminal and run the following command on your local repo: `git remote add upstream <the_https_url_you_copied_from_original_repo`
* In the root of your local repo you cloned (`.\GENERAL\`), create a folder and name it `<your_name-surname>`
* Create other folders inside this folder corresponding to the different projects you're working on, and move your source codes to these folders (e.g., `.\GENERAL\your_name-surname\My-Project-I`)
* Open local repo in terminal or command line and create a new branch using `git checkout -b <branch name>`
* Stage changes using `git add .`
* Commit changes using `git commit -m <name of commit`
* Push codes and changes to branch on github using `git push origin <branch name>`
* Open github on web browser and create a Pull Request (PR) to update original repo with your codes and changes
* Administrator will review your commits and then approve merging with the original repo

# Quick Tip
Having a forked repository (`User/GENERAL`) will allow you to manage your codes while commiting and pushing changes on your local repository. Then, from time to time, you can commit and push changes on the original repository.

