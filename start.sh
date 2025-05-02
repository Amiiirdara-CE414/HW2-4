#!/bin/bash
echo "setup redirection..."
iptables -t nat -A PREROUTING -p tcp --dport 0 -j REDIRECT --to-port 80
echo "setup app..."
python app.py
