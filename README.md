# The Fuck

Magnificent app which corrects your previous console command.

Few examples:

```bash
➜ apt-get install vim
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?

➜ fuck
[sudo] password for nvbn: 
Reading package lists... Done
...

➜ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master


➜ fuck
Counting objects: 9, done.
...
```

## Installation

Install `The Fuck`:

```bash
sudo pip3 install thefuck
```

And add to `.bashrc` or `.zshrc`:

```bash
alias fuck='$(thefuck $(fc -ln -1))'
```

## Developing

Install `The Fuck` for development:

```bash
pip3 install -r requirements.txt
python3 setup.py develop
```

Run tests:

```bash
py.test
```