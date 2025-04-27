#!/bin/bash

dns_server="8.8.8.8"

nslookup $dns_server
if [ $? -ne 0 ]; then
  echo "DNS is down!"
else
  echo "DNS is up!"
fi

