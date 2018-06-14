#!/bin/bash 
source utils/bash_includes.sh 

git remote -v update


UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "Need to pull"
	msg_squealer "Pulling from github to update squealer"
    git pull 
elif [ $REMOTE = $BASE ]; then
	msg_squealer "Squealer has changes that need to be pushed to github"
    echo "Need to push"
else
	msg_squealer "Squealer has divered from github main branch, merge then commit"
    echo "Diverged"
fi




