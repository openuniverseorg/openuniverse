#!/bin/bash
set -xe

if [ $TRAVIS_BRANCH == 'master' ] ; then
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa

  echo "Updating repository."
  cd /home/debian/continuousdeployment.git
  git remote add deploy openuniverse@206.189.177.194:/home/debian/continuousdeployment.git
  git config user.name "Travis CI"
  git config user.email "fronchetti@usp.br"

  git add .
  git commit -m "Deploy"
  git push --force deploy master
else
  echo "Not deploying, since this branch isn't master."
fi
