https://backdoor.sdslabs.co/challenges/LOST-FOUND

```
$ wget http://hack.bckdr.in/LOST-FOUND/lost_found.zip
$ file lost_found.zip
lost_found.zip: Zip archive data, at least v1.0 to extract
$ unzip lost_found.zip
Archive:  lost_found.zip
   creating: .git/
  inflating: .git/packed-refs
 extracting: .git/ORIG_HEAD
   creating: .git/hooks/
  inflating: .git/hooks/update.sample
  inflating: .git/hooks/commit-msg.sample
  inflating: .git/hooks/applypatch-msg.sample
  inflating: .git/hooks/pre-commit.sample
  inflating: .git/hooks/pre-rebase.sample
  inflating: .git/hooks/pre-applypatch.sample
  inflating: .git/hooks/pre-push.sample
  inflating: .git/hooks/prepare-commit-msg.sample
  inflating: .git/hooks/post-update.sample
   creating: .git/lost-found/
   creating: .git/lost-found/commit/
 extracting: .git/lost-found/commit/f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
   creating: .git/branches/
   creating: .git/refs/
   creating: .git/refs/remotes/
   creating: .git/refs/remotes/origin/
 extracting: .git/refs/remotes/origin/HEAD
   creating: .git/refs/tags/
   creating: .git/refs/heads/
 extracting: .git/refs/heads/master
   creating: .git/info/
  inflating: .git/info/exclude
   creating: .git/logs/
   creating: .git/logs/refs/
   creating: .git/logs/refs/remotes/
   creating: .git/logs/refs/remotes/origin/
  inflating: .git/logs/refs/remotes/origin/HEAD
   creating: .git/logs/refs/heads/
 extracting: .git/logs/refs/heads/master
  inflating: .git/config
  inflating: .git/COMMIT_EDITMSG
   creating: .git/objects/
   creating: .git/objects/53/
 extracting: .git/objects/53/18b5ac7a2fda718b2353ac068aa816398fa3e5
   creating: .git/objects/pack/
  inflating: .git/objects/pack/pack-ae01a765b19fb088d98519e7105a67e3cadc4582.pack
  inflating: .git/objects/pack/pack-ae01a765b19fb088d98519e7105a67e3cadc4582.idx
   creating: .git/objects/f9/
 extracting: .git/objects/f9/943c7fc5d4335746389f9955841666a3801661
   creating: .git/objects/info/
   creating: .git/objects/f7/
 extracting: .git/objects/f7/cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
 extracting: .git/HEAD
  inflating: .git/description
  inflating: .git/index
```

Hmm, looks like a git repo.

```
$ grep -rn flag .git/
.git/COMMIT_EDITMSG:10:#    new file:   flag.txt
$ cat .git/COMMIT_EDITMSG
Updates API token instructions
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# rebase in progress; onto 16b2048
# You are currently editing a commit during a rebase.
#
# Changes to be committed:
#   modified:   README.md
#   new file:   flag.txt
#
```

Looks like we're looking for the contents of this `flag.txt` file.

```
$ git log -n1
commit 3b161f0d331a45e48b8866fc4fb85ade0d4fa0f6
Author: Abhay Rana <capt.n3m0@gmail.com>
Date:   Tue Feb 10 22:05:37 2015 +0530
    Updates API token instructions
$ git show 3b161f0d331a45e48b8866fc4fb85ade0d4fa0f6
commit 3b161f0d331a45e48b8866fc4fb85ade0d4fa0f6
Author: Abhay Rana <capt.n3m0@gmail.com>
Date:   Tue Feb 10 22:05:37 2015 +0530
    Updates API token instructions
diff --git a/README.md b/README.md
index cd30cd9..07c3fab 100644
--- a/README.md
+++ b/README.md
@@ -26,7 +26,7 @@ Configuration Options:
 - **INCOMING_TOKEN** Service Token from Slack's incoming webhook
 - **TEAM_DOMAIN** Domain name of your slack team (just sdslabs, not sdslabs.slack.com)
 - **SESSION_SECRET** Session secret key
-- **API_TOKEN** API Token for the slack team. Generated at <https://api.slack.com> (scroll to bottom).
+- **API_TOKEN** API Token for the slack team. Generated at <https://api.slack.com/web> (scroll to bottom).

 These configuration options can either be provided via a `.env` file in development, or via Heroku config variables, if you are deploying to Heroku. A sample env file is provided in `.env.sample`. You can see service tokens on the left sidebar in Slack configuration.
```

This looks like part of it, maybe we lost something...

```
$ ls .git/lost-found/commit/
f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
$ cat .git/lost-found/commit/f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
$ git show f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
commit f7cee847b02a589cd3d0fa4e2c32cf9a0ccd94a6
Author: Abhay Rana <capt.n3m0@gmail.com>
Date:   Tue Feb 10 22:05:37 2015 +0530
    Updates API token instructions
diff --git a/README.md b/README.md
index cd30cd9..07c3fab 100644
--- a/README.md
+++ b/README.md
@@ -26,7 +26,7 @@ Configuration Options:
 - **INCOMING_TOKEN** Service Token from Slack's incoming webhook
 - **TEAM_DOMAIN** Domain name of your slack team (just sdslabs, not sdslabs.slack.com)
 - **SESSION_SECRET** Session secret key
-- **API_TOKEN** API Token for the slack team. Generated at <https://api.slack.com> (scroll to bottom).
+- **API_TOKEN** API Token for the slack team. Generated at <https://api.slack.com/web> (scroll to bottom).

 These configuration options can either be provided via a `.env` file in development, or via Heroku config variables, if you are deploying to Heroku. A sample env file is provided in `.env.sample`. You can see service tokens on the left sidebar in Slack configuration.

diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..5318b5a
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
+FLAG IS 676a0b9e546e1920c0ff6631f4aac3a9646d843c6bd6d333dda542987570c1b6
```

Lost, and found.
