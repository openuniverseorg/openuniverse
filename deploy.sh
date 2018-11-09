#!/bin/bash
set -xe

if [ $TRAVIS_BRANCH == 'master' ] ; then
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa

  echo "[Travis CI] Deploying repository."
  git remote add deploy "openuniverse@206.189.177.194:/home/debian/continuousdeployment.git"
  git config user.name "Travis CI"
  git config user.email "fronchetti@usp.br"
  git push --force deploy master

else
  echo "[Travis CI] Not deploying, since this branch is not master."
fi
