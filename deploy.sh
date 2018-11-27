#!/bin/bash
set -xe

if [ $TRAVIS_BRANCH == 'master' ] ; then
  echo "[Travis CI] Transferring the repository."
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa
  git remote add deploy "openuniverse@206.189.177.194:/home/debian/continuousdeployment.git"
  git config user.name "Travis CI"
  git config user.email "travis@openuniverse.me"
  git push --force deploy master

else
  echo "[Travis CI] Not Transferring, since this branch is not master."
fi
