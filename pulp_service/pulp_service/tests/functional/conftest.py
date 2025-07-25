import pytest

from pulpcore.tests.functional.utils import BindingsNamespace

# Bindings API Fixtures


@pytest.fixture(scope="session")
def service_bindings(_api_client_set, bindings_cfg):
    """
    A namespace providing preconfigured pulp_service api clients.
    """
    from pulpcore.client import pulp_service as service_bindings_module

    api_client = service_bindings_module.ApiClient(bindings_cfg)
    _api_client_set.add(api_client)
    yield BindingsNamespace(service_bindings_module, api_client)
    _api_client_set.remove(api_client)


@pytest.fixture(scope="session")
def vuln_report_api(service_bindings):
    """Vulnerability Report API fixture."""
    return service_bindings.VulnReportApi


@pytest.fixture(scope="session")
def service_content_guards_api_client(service_bindings):
    """Api for service content guards."""
    return service_bindings.ContentguardsFeatureApi
