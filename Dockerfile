FROM python:3.12-slim

RUN pip install --no-cache-dir \
    "jhsingle-native-proxy>=0.0.9" \
    streamlit \
    requests

# uid 1001 matches the KubeSpawner runAsUser set by ApplicationHub
RUN useradd -m -u 1001 -g users jovyan && chmod 755 /home/jovyan
ENV HOME=/home/jovyan
WORKDIR $HOME

COPY --chown=jovyan:users entrypoint.sh /home/jovyan/entrypoint.sh
COPY --chown=jovyan:users app.py /home/jovyan/app.py
RUN chmod +x /home/jovyan/entrypoint.sh

USER jovyan

EXPOSE 8888

ENTRYPOINT ["/home/jovyan/entrypoint.sh"]

CMD ["jhsingle-native-proxy", \
     "--destport", "8505", \
     "streamlit", "run", "app.py", \
     "{--}server.port", "{port}", \
     "{--}server.headless", "True", \
     "{--}server.enableCORS", "False", \
     "--port", "8888"]
