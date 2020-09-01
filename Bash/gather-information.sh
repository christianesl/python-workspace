#!/bin/bash
echo "Staring at: $(date)"
echo

echo "UPTIME"
UPTIME
echo

echo "Free"
Free
echo

echo "who"
who
echo

echo "Finishing at: $(date)"


----
line="----------------------------------------"
echo "Staring at: $(date)" ; echo $line
echo "UPTIME" ; UPTIME ; echo $line
echo "Free" ; Free ; echo $line
echo "who" ; who ; echo $line
echo "Finishing at: $(date)