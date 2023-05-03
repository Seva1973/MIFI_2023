#!/bin/bash
# Сброс правил iptables
sudo iptables -F
sudo iptables -X
sudo iptables -Z
# Блокировка всего входящего и исходящего трафика
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
sudo iptables -P FORWARD DROP
# Сохранение правил iptables
sudo iptables-save > /etc/iptables/rules.v4
