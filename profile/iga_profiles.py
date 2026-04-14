"""
EOEPCA sample application profiles for app-hub-configurator.

Registered profiles:
  - sample_app_slug: IGA Streamlit Demo (default profile)

Usage with dump-config:
    dump-config --profiles-dir scripts/profiles \
                --profiles sample_app_slug,...
"""

from configurator.apps import profile_registry
from configurator.apps.base import BaseAppProfile


class _SampleAppBase(BaseAppProfile):
    """Base with id / default overrides not exposed by BaseAppProfile."""

    # class-level overrides
    profile_id: str = ""   # overrides the default "profile_{slug}"
    profile_default: bool = False

    def build(self):
        profile = super().build()
        if self.profile_id:
            profile.id = self.profile_id
        profile.definition.default = self.profile_default
        return profile


class IgaStreamlitDemoProfile(_SampleAppBase):
    slug = "sample_app_slug"
    profile_id = "sample_app"
    profile_default = True

    display_name = "Sample Streamlit App"
    description = (
        "A minimal sample application — use this as a starting point "
        "to build your own ApplicationHub app."
    )
    image = "ghcr.io/eoepca/iga-streamlit-demo:latest"

    cpu_limit = 1
    cpu_guarantee = None
    mem_limit = "2G"
    mem_guarantee = None

    pod_env_vars = {"HOME": "/home/jovyan"}

    def get_default_volumes(self):
        return []


profile_registry.register(IgaStreamlitDemoProfile)
