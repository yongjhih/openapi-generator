#!/usr/bin/env bash

declare -A menders=(
    ["inventory"]="https://github.com/mendersoftware/inventory/raw/master/docs/management_api.yml"
    ["useradm"]="https://github.com/mendersoftware/useradm/raw/master/docs/management_api.yml"
    ["deviceadm"]="https://github.com/mendersoftware/deviceadm/raw/master/docs/management_api.yml"
    ["deployments"]="https://github.com/mendersoftware/deployments/raw/master/docs/management_api.yml"
    ["deviceauth"]="https://github.com/mendersoftware/deviceauth/raw/master/docs/management_api.yml"
)

SCRIPT="$0"

while [ -h "$SCRIPT" ] ; do
  ls=$(ls -ld "$SCRIPT")
  link=$(expr "$ls" : '.*-> \(.*\)$')
  if expr "$link" : '/.*' > /dev/null; then
    SCRIPT="$link"
  else
    SCRIPT=$(dirname "$SCRIPT")/"$link"
  fi
done

if [ ! -d "${APP_DIR}" ]; then
  APP_DIR=$(dirname "$SCRIPT")/..
  APP_DIR=$(cd "${APP_DIR}"; pwd)
fi

executable="./modules/openapi-generator-cli/target/openapi-generator-cli.jar"

if [ ! -f "$executable" ]
then
  mvn clean package
fi

# if you've executed sbt assembly previously it will use that instead.
export JAVA_OPTS="${JAVA_OPTS} -XX:MaxPermSize=256M -Xmx1024M -DloggerPath=conf/log4j.properties"

for mender in "${!menders[@]}"; do
    ags="$@ generate -i ${menders[$mender]} -g python-typing -o samples/client/${mender}/python-typing"
    java ${JAVA_OPTS} -jar ${executable} ${ags}
done
