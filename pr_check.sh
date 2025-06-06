#!/bin/bash

APP_NAME="pulp"       # name of app-sre "application" folder this component lives in
COMPONENT_NAME="pulp" # name of app-sre "resourceTemplate" in deploy.yaml for this component
IMAGE="quay.io/cloudservices/pulp-ubi"

# be explicit about what to build
DOCKERFILE=Dockerfile

IQE_PLUGINS="content-sources"
IQE_MARKER_EXPRESSION="api"
IQE_FILTER_EXPRESSION="not test_introspection_of_persistent_user"
IQE_CJI_TIMEOUT="30m"
COMPONENTS_W_RESOURCES="pulp content-sources-backend"
REF_ENV="insights-stage"

# Install bonfire repo/initialize
CICD_URL=https://raw.githubusercontent.com/RedHatInsights/cicd-tools/main
curl -s $CICD_URL/bootstrap.sh >.cicd_bootstrap.sh && source .cicd_bootstrap.sh

# Include all impacted HMS apps for deployment
EXTRA_DEPLOY_ARGS="--set-parameter pulp/PULP_API_MEMORY_LIMIT=4096Mi --set-parameter pulp/PULP_API_MEMORY_REQUEST=2048Mi --timeout=1400 content-sources"

source $CICD_ROOT/build.sh
source $CICD_ROOT/deploy_ephemeral_env.sh
source $APP_ROOT/unit_test.sh
# source $CICD_ROOT/cji_smoke_test.sh
source $CICD_ROOT/post_test_results.sh
