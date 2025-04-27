#!/bin/bash

./check_gateway.sh
if [ $? -ne 0 ]; then
  echo "Repairing gateway..."
  systemctl restart network.service
fi

./check_dns.sh
if [ $? -ne 0 ]; then
  echo "Repairing DNS..."
  systemctl restart systemd-resolved
fi

