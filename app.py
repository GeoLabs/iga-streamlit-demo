"""
EOEPCA ApplicationHub — Sample Streamlit Application

This is a minimal sample app demonstrating how to build and publish a custom
application to the EOEPCA ApplicationHub. Use it as a starting point for your
own dashboards, EO data visualisation tools, or analysis notebooks.

To customise:
  1. Edit this file with your own Streamlit content
  2. Add dependencies to the Dockerfile (pip install ...)
  3. Rebuild the image and publish it to a container registry
  4. Add a profile entry in your ApplicationHub config.yml
"""

import os

import streamlit as st

st.set_page_config(
    page_title="EOEPCA Sample App",
    layout="centered",
)

st.title("EOEPCA ApplicationHub — Sample App")

st.markdown(
    """
Welcome to the **EOEPCA ApplicationHub** sample application.

This Streamlit app is a minimal starting point for building and publishing your
own tools inside the ApplicationHub. It demonstrates:

- How a JupyterHub-managed application is served via `jhsingle-native-proxy`
- How to read runtime information injected by the Hub (user name, namespace, …)
- How to structure a `Dockerfile` and `entrypoint.sh` for Hub-compatible apps

---
"""
)

# Runtime info injected by JupyterHub / KubeSpawner
hub_user = os.environ.get("JUPYTERHUB_USER", "unknown")
hub_server = os.environ.get("JUPYTERHUB_SERVER_NAME", "default")
hub_base_url = os.environ.get("JUPYTERHUB_SERVICE_PREFIX", "/")

col1, col2 = st.columns(2)
with col1:
    st.metric("Hub user", hub_user)
    st.metric("Server name", hub_server or "default")
with col2:
    st.metric("Service prefix", hub_base_url)
    st.metric("Python", os.popen("python --version").read().strip())

st.markdown("---")
st.subheader("Next steps")
st.markdown(
    """
1. **Customise `app.py`** — replace this content with your own Streamlit application.
2. **Add Python dependencies** in the `Dockerfile` (`pip install mypackage`).
3. **Build and push** the image to your container registry:
   ```bash
   docker build -t ghcr.io/<org>/my-app:latest .
   docker push ghcr.io/<org>/my-app:latest
   ```
4. **Add a profile** in your ApplicationHub `config.yml` referencing your new image.
5. **Deploy** with skaffold:
   ```bash
   skaffold run -p custom
   ```

For a full walkthrough, see the
[ApplicationHub tutorial](https://eoepca.github.io/application-hub-context/tutorial/).
"""
)
