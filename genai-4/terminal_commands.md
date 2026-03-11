# Developer Terminal Commands Guide

A practical guide to the **most important terminal commands every developer should know**.  
These commands help with **navigation, file management, searching, system monitoring, and development workflows**.

---

# 1. Navigation Commands

Commands used to move around the file system.

### `pwd`
Shows the current working directory.

```bash
pwd
```

Example Output

```
/Users/ashish/projects
```

---

### `ls`
Lists files and directories.

```bash
ls
```

Common options:

```bash
ls -l      # detailed list
ls -a      # show hidden files
ls -lh     # human readable file sizes
```

---

### `cd`
Changes the directory.

```bash
cd folder_name
```

Examples:

```bash
cd ..
cd ~
cd /usr/local
```

---

# 2. File and Directory Management

### `mkdir`
Creates a new directory.

```bash
mkdir project
```

Create nested directories:

```bash
mkdir -p project/src/components
```

---

### `touch`
Creates a new empty file.

```bash
touch file.txt
```

Create multiple files:

```bash
touch file1.txt file2.txt
```

---

### `cp`
Copies files or directories.

```bash
cp file.txt backup.txt
```

Copy directories:

```bash
cp -r folder1 folder2
```

---

### `mv`
Moves or renames files.

```bash
mv old.txt new.txt
```

Move file to directory:

```bash
mv file.txt folder/
```

---

### `rm`
Removes files or directories.

Delete file:

```bash
rm file.txt
```

Delete directory:

```bash
rm -r folder
```

Force delete:

```bash
rm -rf folder
```

---

# 3. File Viewing Commands

### `cat`
Displays file content.

```bash
cat file.txt
```

---

### `less`
Views large files interactively.

```bash
less file.txt
```

Controls:

```
q  → quit
space → next page
```

---

### `head`
Shows first lines of a file.

```bash
head file.txt
```

Specify number of lines:

```bash
head -n 20 file.txt
```

---

### `tail`
Shows last lines of a file.

```bash
tail file.txt
```

Live monitoring:

```bash
tail -f log.txt
```

---

# 4. Search and Filtering

### `grep`
Searches text inside files.

```bash
grep "error" log.txt
```

Ignore case:

```bash
grep -i "error" log.txt
```

Recursive search:

```bash
grep -r "function" .
```

---

### `find`
Finds files in directories.

```bash
find . -name "app.py"
```

Find by type:

```bash
find . -type d
```

---

# 5. System Monitoring

### `top`
Shows running processes.

```bash
top
```

---

### `ps`
Displays process information.

```bash
ps aux
```

---

### `df`
Shows disk space usage.

```bash
df -h
```

---

### `du`
Shows directory size.

```bash
du -sh folder
```

---

# 6. Permissions and Ownership

### `chmod`
Changes file permissions.

```bash
chmod +x script.sh
```

Numeric permission example:

```bash
chmod 755 script.sh
```

---

### `chown`
Changes file ownership.

```bash
chown user:group file.txt
```

---

# 7. Networking Commands

### `ping`
Tests network connectivity.

```bash
ping google.com
```

---

### `curl`
Transfers data from URLs.

```bash
curl https://example.com
```

Download file:

```bash
curl -O https://example.com/file.zip
```

---

# 8. Development Commands

### `git`
Version control system.

Clone repository:

```bash
git clone repo_url
```

Check status:

```bash
git status
```

Commit changes:

```bash
git commit -m "message"
```

---

### `python`
Runs Python programs.

```bash
python app.py
```

---

### `pip`
Installs Python packages.

```bash
pip install pandas
```

---

### `node`
Runs JavaScript runtime.

```bash
node app.js
```

---

### `npm`
Manages Node.js packages.

```bash
npm install
```

Install package:

```bash
npm install express
```

---

# 9. Productivity Commands

### `history`
Shows command history.

```bash
history
```

---

### `clear`
Clears terminal screen.

```bash
clear
```

---

### `alias`
Creates command shortcuts.

```bash
alias ll="ls -la"
```

---

# 10. Helpful Keyboard Shortcuts

| Shortcut | Action |
|--------|--------|
| `Ctrl + C` | Stop running command |
| `Ctrl + L` | Clear screen |
| `Ctrl + R` | Search command history |
| `Ctrl + A` | Move cursor to start |
| `Ctrl + E` | Move cursor to end |

---

# Summary

These commands form the **foundation of working efficiently in the terminal**.

Core commands developers use daily:

```
cd
ls
pwd
mkdir
rm
cp
mv
cat
grep
find
git
python
pip
```

Mastering these commands greatly improves **productivity, debugging speed, and system understanding**.
