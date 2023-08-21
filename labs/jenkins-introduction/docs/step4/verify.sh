#!/bin/sh

fail() {
  echo "fail"
  exit 1
}

success() {
  echo "success"
  exit 0
}

JENKINS_USER="admin"
JENKINS_PASS="admin"
JENKINS_URL="http://jenkins.onlylabs.io/job/Test-2/api/json"


if curl -XGET -I $JENKINS_URL --user $JENKINS_USER:$JENKINS_PASS | grep "200 OK"; then
    success
fi

fail
