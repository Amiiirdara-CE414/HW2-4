#!/bin/bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 0 -j REDIRECT --to-port 80
python3 app.py
