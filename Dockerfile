FROM alpine:3
LABEL org.opencontainers.image.source="https://github.com/zebbra/netbox-init"
LABEL org.opencontainers.image.description="NetBox fixture loader"

RUN apk add --no-cache \
  ansible \
  bash \
  ca-certificates \
  curl \
  git \
  make \
  openssh \
  py3-dnspython \
  py3-passlib \
  py3-pip \
  py3-tz \
  python3 \
  vim

RUN pip install --break-system-packages pynetbox

ENV INIT_DIR=/srv/init
ENV DEVICE_TYPE_FILES_DIR=${INIT_DIR}/device_types
ENV INIT_GENERATOR_DIR=${INIT_DIR}/gen
ENV VAR_FILES_DIR=${INIT_DIR}/vars
RUN mkdir -p $DEVICE_TYPE_FILES_DIR $INIT_GENERATOR_DIR $VAR_FILES_DIR

ENV HOME=/home
RUN adduser -D -h ${HOME} ansible

COPY init/generator ${HOME}/generator
COPY init/ansible/ansible.cfg ${HOME}/.ansible.cfg
RUN chown -R ansible:ansible ${HOME}

USER ansible
RUN ansible-galaxy collection install --force netbox.netbox

WORKDIR ${HOME}

ENV NETBOX_URL=""
ENV NETBOX_TOKEN=""
CMD ["${HOME}/generator/init.sh"]
