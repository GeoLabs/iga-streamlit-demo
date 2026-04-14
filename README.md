# EOEPCA ApplicationHub — Sample Streamlit App

A minimal sample application demonstrating how to build and publish a custom app to the [EOEPCA ApplicationHub](https://github.com/EOEPCA/application-hub-context).

Used as the sample application for the [ApplicationHub tutorial](https://eoepca.github.io/application-hub-context/tutorial/).

## Overview

The app runs [Streamlit](https://streamlit.io/) inside a JupyterHub-managed pod, served via [`jhsingle-native-proxy`](https://github.com/ideonate/jhsingle-native-proxy) so that it integrates seamlessly with the Hub's authentication and routing.

## Image

```text
ghcr.io/eoepca/iga-streamlit-demo:latest
```

| Tag           | Source branch    | Purpose            |
| ------------- | ---------------- | ------------------ |
| `latest`      | `main`           | Stable builds      |
| `latest-dev`  | `develop`        | Development builds |
| `X.Y.Z`       | Git tag `vX.Y.Z` | Immutable release  |

## Local development

### Build

```bash
docker build -t iga-streamlit-demo:local .
```

### Run

```bash
docker run --rm -p 8888:8888 iga-streamlit-demo:local
```

Open <http://localhost:8888> in your browser.

### Customise

Edit `app.py` with your own Streamlit content, then rebuild.

## Publishing to ApplicationHub

1. Push the image to a container registry:

   ```bash
   docker tag iga-streamlit-demo:local ghcr.io/<org>/my-app:latest
   docker push ghcr.io/<org>/my-app:latest
   ```

2. Create a profile entry in your ApplicationHub `config.yml`:

   ```bash
   dump-config
        --profiles-dir ./profile
        --profiles sample_app_slug
        --groups group-a,group-b,group-c
        --output sample-app-config.yml
   ```

3. Deploy with skaffold:

   ```bash
   skaffold run -p custom
   ```

For a full walkthrough, see the [ApplicationHub tutorial](https://eoepca.github.io/application-hub-context/tutorial/).
