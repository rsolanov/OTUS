from confluent_kafka import Consumer
import clickhouse_connect
import json


def main():
    consumer = Consumer({
        'bootstrap.servers': 'host.docker.internal:9092',
        'group.id': 'python_consumer_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['test_topic'])

    clickhouse_client = clickhouse_connect.get_client(host='host.docker.internal', port=8123, username='default', password='default')

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Ошибка потребителя: {msg.error()}")
            continue

        data = json.loads(msg.value().decode('utf-8'))
        print(json.dumps(data, indent=2))
        clickhouse_client.command(f"INSERT INTO mergetree_table FORMAT JSONEachRow {json.dumps(data)}")

    consumer.close()

if __name__ == '__main__':
    main()