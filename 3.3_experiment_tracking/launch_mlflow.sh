#!/usr/bin/env bash

declare -xr REVERSE_PROXY_FQDN='expanse-user-content.sdsc.edu'

declare -xir LOWEST_EPHEMERAL_PORT=49152
declare -i random_ephemeral_port=-1

declare -xr MLFLOW_HOST="$(hostname -s).eth.cluster"
declare -xi MLFLOW_PORT=-1
while (( "${MLFLOW_PORT}" < 0 )); do
  while (( "${random_ephemeral_port}" < "${LOWEST_EPHEMERAL_PORT}" )); do
    random_ephemeral_port="$(od -An -N 2 -t u2 -v < /dev/urandom)"
  done
  ss -nutlp | cut -d : -f2 | grep "^${random_ephemeral_port})" > /dev/null
  if [[ "${?}" -ne 0 ]]; then
    MLFLOW_PORT="${random_ephemeral_port}"
  fi
done


http_response="$(curl -s -w %{http_code} https://manage.${REVERSE_PROXY_FQDN}/getlink.cgi -o -)"
http_status_code="$(echo ${http_response} | awk '{print $NF}')"
if (( "${http_status_code}" != 200 )); then
  echo "Unable to connect to the Satellite reverse proxy service: ${http_status_code}"
  return 1
fi

declare -xr REVERSE_PROXY_TOKEN="$(echo ${http_response} | awk 'NF>1{printf $((NF-1))}' -)"

mlflow server --backend-store-uri "sqlite:///${HOME}/mlops/mlruns.db" --default-artifact-root ./mlruns --host "${MLFLOW_HOST}" --port "${MLFLOW_PORT}" --cors-allowed-origins "https://${REVERSE_PROXY_TOKEN}.${REVERSE_PROXY_FQDN}" &
if [[ "${?}" -ne 0 ]]; then
  echo 'ERROR: Failed to launch mlflow server.'
  exit 1
fi

curl "https://manage.${REVERSE_PROXY_FQDN}/redeemtoken.cgi?token=${REVERSE_PROXY_TOKEN}&port=${MLFLOW_PORT}"
echo "https://${REVERSE_PROXY_TOKEN}.${REVERSE_PROXY_FQDN}"

wait

curl "https://manage.${REVERSE_PROXY_FQDN}/destroytoken.cgi?token=${REVERSE_PROXY_TOKEN}"