#!/bin/bash

gateway="192.168.1.1"

ping -c 4 $gateway
if [ $? -ne 0 ]; then
  echo "Gateway is down!"
else
  echo "Gateway is up!"
fi
