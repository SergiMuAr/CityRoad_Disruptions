/home/sergi/kafka_2.12-2.1.1/bin/zookeeper-server-start.sh /home/sergi/kafka_2.12-2.1.1/config/zookeeper.properties &
/home/sergi/kafka_2.12-2.1.1/bin/kafka-server-start.sh /home/sergi/kafka_2.12-2.1.1/config/server.properties &
sleep 5s
python3 main.py &
python3 Twitter.py


