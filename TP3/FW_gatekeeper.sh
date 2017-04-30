#inspirer de https://openclassrooms.com/courses/securiser-son-serveur-linux

#!/bin/sh

sudo su root

# Suppression des regles precedentes
iptables -t filter -F
iptables -t filter -X

#desactivation des regles par defaut
iptables -t filter -P INPUT DROP
iptables -t filter -P FORWARD DROP
iptables -t filter -P OUTPUT DROP

#on garde les connexions etablis
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

#autorisation loopback
iptables -t filter -A INPUT -i lo -j ACCEPT
iptables -t filter -A OUTPUT -o lo -j ACCEPT

#SSH
iptables -t filter -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -t filter -A OUTPUT -p tcp --dport 22 -j ACCEPT

# DNS
iptables -t filter -A OUTPUT -p tcp --dport 53 -j ACCEPT
iptables -t filter -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -t filter -A INPUT -p tcp --dport 53 -j ACCEPT
iptables -t filter -A INPUT -p udp --dport 53 -j ACCEPT

#connexion proxy
iptables -t filter -A INPUT -p tcp --dport 5001 -j ACCEPT
iptables -t filter -A OUTPUT -p tcp --dport 5001 -j ACCEPT





