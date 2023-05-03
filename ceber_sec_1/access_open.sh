#!/bin/bash
# Сброс правил iptables
sudo iptables -F
sudo iptables -X
sudo iptables -Z
# Разрешение всего входящего и исходящего трафика
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
# Сохранение правил iptables
sudo iptables-save > /etc/iptables/rules.v4
