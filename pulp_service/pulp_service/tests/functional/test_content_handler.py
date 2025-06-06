import json

import pytest
import requests

from pulp_npm.tests.functional.constants import NPM_FIXTURE_URL


# @pytest.mark.xfail
def test_artifact_size_header_on_pull_through_cache(
    npm_bindings, npm_remote_factory, npm_distribution_factory, http_get, delete_orphans_pre
):
    """Test that a pull-through distro can be installed from."""
    remote = npm_remote_factory(url=NPM_FIXTURE_URL)
    distro = npm_distribution_factory(remote=remote.pulp_href)
    PACKAGE = "react"

    package_metadata = json.loads(http_get(f"{distro.base_url}{PACKAGE}"))
    assert package_metadata["name"] == PACKAGE

    latest_package_version = package_metadata["dist-tags"]["latest"]
    latest_package_metadata = package_metadata["versions"][latest_package_version]
    package_filename = latest_package_metadata["dist"]["tarball"].removeprefix(NPM_FIXTURE_URL)

    response = requests.get(f"{distro.base_url}{package_filename}")

    assert response.headers.get("X-PULP-ARTIFACT-SIZE")
