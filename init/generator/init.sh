#!/usr/bin/env bash
set \
  -o errexit \
  -o nounset \
  -o pipefail

~/generator/generator.py > $INIT_GENERATOR_DIR/init.yaml

# Wait for NetBox to be ready
echo "Waiting for NetBox to be ready at $NETBOX_URL..."
timeout=300  # 5 minutes timeout
counter=0
interval=5   # 5 seconds between retries

until curl -s -f "$NETBOX_URL" > /dev/null || [ $counter -eq $timeout ]; do
    echo "NetBox is not ready yet. Retrying in $interval seconds..."
    sleep $interval
    counter=$((counter + interval))
done

if [ $counter -eq $timeout ]; then
    echo "Timeout waiting for NetBox to be ready at $NETBOX_URL exceeded"
    exit 1
fi

exec ansible-playbook $INIT_GENERATOR_DIR/init.yaml
