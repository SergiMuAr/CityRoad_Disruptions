#!/bin/bash

# Kill the remaining kafka in the system
#pids=$(ps aux | grep "[k]afka" | cut -d" " -f3)
# pids=$(ps aux | grep "[k]afka" | awk '{print $2}')
# for pid in $pids;
# do
# 	kill -9 $pid
# done


#Start zookeper
kafka_2.12-2.1.1/bin/zookeeper-server-start.sh kafka_2.12-2.1.1/config/zookeeper.properties &
sleep 5
#Start kafka Server
kafka_2.12-2.1.1/bin/kafka-server-start.sh kafka_2.12-2.1.1/config/server.properties &
sleep 15
python3 Utils/PreprocessDataSet.py
python3 Twitter.py &
python3 main.py

# Stop kafka
kafka_2.12-2.1.1/bin/kafka-server-stop.sh
sleep 5

# Stop zookeper
kafka_2.12-2.1.1/bin/zookeeper-server-stop.sh
sleep 5

# #pids=$(ps aux | grep "[k]afka" | cut -d" " -f3)
# pids=$(ps aux | grep "[k]afka" | awk '{print $2}')
# for pid in $pids;
# do
# 	kill -9 $pid
# done

# #pids=$(ps aux | grep "[m]ain.py" | cut -d" " -f3)
# pids=$(ps aux | grep "[m]ain.py" | awk '{print $2}')
# for pid in $pids;
# do
# 	kill -9 $pid
# done

