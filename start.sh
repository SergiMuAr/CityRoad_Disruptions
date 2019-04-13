#!/bin/bash

# Kill the remaining kafka in the system
#pids=$(ps aux | grep "[k]afka" | cut -d" " -f3)
pids=$(ps aux | grep "[k]afka" | awk '{print $2}')
for pid in $pids;
do
	kill -9 $pid
done

#Start zookeper
kafka_2.12-2.1.1/bin/zookeeper-server-start.sh kafka_2.12-2.1.1/config/zookeeper.properties &
#Start kafka Server
kafka_2.12-2.1.1/bin/kafka-server-start.sh kafka_2.12-2.1.1/config/server.properties &

#Create Topic "Test"
#kafka_2.11-1.1.0 kafka_2.12-2.1.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

#List topics
#kafka_2.11-1.1.0 kafka_2.12-2.1.1/bin/kafka-topics.sh --list --zookeeper localhost:2181
sleep 20
python3 main.py &
python3 Twitter.py

#pids=$(ps aux | grep "[k]afka" | cut -d" " -f3)
pids=$(ps aux | grep "[k]afka" | awk '{print $2}')
for pid in $pids;
do
	kill -9 $pid
done

#pids=$(ps aux | grep "[m]ain.py" | cut -d" " -f3)
pids=$(ps aux | grep "[m]ain.py" | awk '{print $2}')
for pid in $pids;
do
	kill -9 $pid
done

