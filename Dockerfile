FROM python:3.8

ADD https://releases.hashicorp.com/consul-template/0.25.0/consul-template_0.25.0_linux_amd64.tgz consul-template.tgz
RUN tar -C /bin -xvf consul-template.tgz && rm consul-template.tgz

COPY --from=consul:1.8 /bin/consul /bin/

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY ./backend /app
COPY ./deploy /opt/deploy

ENTRYPOINT ["/opt/deploy/entrypoint.sh"]
