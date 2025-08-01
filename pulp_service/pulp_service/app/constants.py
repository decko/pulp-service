from types import SimpleNamespace

OSV_QUERY_URL = "https://api.osv.dev/v1/query"
OSV_QUERY_BATCH_URL = "https://api.osv.dev/v1/querybatch"
RH_REPO_TO_CPE_URL = "https://www.redhat.com/security/data/metrics/repository-to-cpe.json"
PKG_ECOSYSTEM = SimpleNamespace(
    rpm="Red Hat", npm="npm", maven="Maven", python="PyPI", gem="RubyGems"
)

# Labels used in RPM repositories for vulnerability report tasks
OSV_RH_ECOSYSTEM_LABEL = "osv_dev ecosystem"
OSV_RH_ECOSYSTEM_CPES_LABEL = "osv_dev cpes"

# Define a basic schema for package-lock.json
# https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json#file-format
NPM_PACKAGE_LOCK_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "version": {"type": "string"},
        "lockfileVersion": {"type": "integer"},
        "requires": {"type": "boolean"},
        "packages": {"type": "object"},
        "dependencies": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "version": {"type": "string"},
                    "resolved": {"type": "string"},
                    "integrity": {"type": "string"},
                    "requires": {"type": "object"},
                },
            },
        },
    },
    "required": ["name", "lockfileVersion", "packages"],
}

# timeout when waiting on tasks scan thread queue to avoid indefinite blocking.
VULNERABILITY_TASK_THREAD_TIMEOUT = 60

CONTENT_SOURCES_LABEL_NAME = "contentsources"
RHEL_AI_DOMAIN_NAME = "rhel-ai"
