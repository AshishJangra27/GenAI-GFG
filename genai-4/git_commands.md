# Git Commands Guide for Developers

This guide covers **important Git commands every developer should know**.  
Git is a **distributed version control system** used to track changes in code, collaborate with teams, and manage project history.

---

# 1. Git Configuration

Before using Git, configure your identity.

### Set Username

```bash
git config --global user.name "Your Name"
```

---

### Set Email

```bash
git config --global user.email "your@email.com"
```

---

### Check Git Configuration

```bash
git config --list
```

---

# 2. Creating a Repository

### Initialize a Git Repository

Creates a new Git repository in the current directory.

```bash
git init
```

After initialization, Git starts tracking changes.

---

# 3. Cloning a Repository

Downloads an existing repository from a remote server.

```bash
git clone repository_url
```

Example

```bash
git clone https://github.com/user/project.git
```

This creates a local copy of the repository.

---

# 4. Checking Repository Status

Shows the current state of the repository.

```bash
git status
```

It displays:

- modified files
- staged files
- untracked files

---

# 5. Adding Files to Staging Area

Git uses a **staging area** before committing changes.

### Add Single File

```bash
git add file.py
```

---

### Add Multiple Files

```bash
git add file1.py file2.py
```

---

### Add All Files

```bash
git add .
```

---

# 6. Committing Changes

A commit records changes to the repository history.

### Commit Changes

```bash
git commit -m "Add new feature"
```

---

### Commit All Modified Files

```bash
git commit -am "Update code"
```

Note: This does **not include new untracked files**.

---

# 7. Viewing Commit History

### View Commit Log

```bash
git log
```

---

### Compact Commit History

```bash
git log --oneline
```

Example Output

```
a32fd21 Add login feature
b41c9a2 Fix bug
```

---

# 8. Working with Branches

Branches allow parallel development.

---

### List Branches

```bash
git branch
```

---

### Create New Branch

```bash
git branch feature-login
```

---

### Switch Branch

```bash
git checkout feature-login
```

---

### Create and Switch Branch

```bash
git checkout -b feature-login
```

---

### Delete Branch

```bash
git branch -d feature-login
```

---

# 9. Merging Branches

Combines changes from one branch into another.

Switch to the target branch:

```bash
git checkout main
```

Merge another branch:

```bash
git merge feature-login
```

---

# 10. Remote Repositories

Remote repositories are hosted online.

---

### View Remote Repositories

```bash
git remote -v
```

---

### Add Remote Repository

```bash
git remote add origin repository_url
```

Example

```bash
git remote add origin https://github.com/user/project.git
```

---

# 11. Pushing Code

Uploads local commits to a remote repository.

### Push to Remote

```bash
git push origin main
```

---

### Push New Branch

```bash
git push -u origin feature-login
```

The `-u` flag sets upstream tracking.

---

# 12. Pulling Updates

Downloads changes from a remote repository.

```bash
git pull origin main
```

This performs:

```
fetch + merge
```

---

# 13. Fetching Updates

Downloads remote changes **without merging**.

```bash
git fetch
```

---

# 14. Undoing Changes

### Undo Unstaged Changes

```bash
git checkout -- file.py
```

---

### Unstage File

```bash
git reset file.py
```

---

### Undo Last Commit

```bash
git reset --soft HEAD~1
```

---

# 15. Removing Files

Remove file from Git tracking.

```bash
git rm file.py
```

Remove from repository but keep locally.

```bash
git rm --cached file.py
```

---

# 16. Checking Differences

Shows differences between file versions.

### Show File Changes

```bash
git diff
```

---

### Show Staged Changes

```bash
git diff --staged
```

---

# 17. Stashing Changes

Temporarily saves uncommitted work.

### Save Changes

```bash
git stash
```

---

### View Stashes

```bash
git stash list
```

---

### Apply Stash

```bash
git stash apply
```

---

### Remove Stash

```bash
git stash drop
```

---

# Summary

Important Git commands developers use daily:

```
git init
git clone
git status
git add
git commit
git log
git branch
git checkout
git merge
git push
git pull
git fetch
git diff
git stash
```

Understanding these commands helps developers **track changes, collaborate with teams, and maintain clean project history**.
