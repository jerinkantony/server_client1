import os
import json
import cv2
import numpy as np
from kafka import KafkaAdminClient, KafkaConsumer
from kafka.admin import NewTopic


def subscribe():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000)
    consumer.subscribe(['outputframes'])
    os.chdir("..")
    path = os.path.abspath(os.curdir)
    if not os.path.exists('rail-inference'):
        os.makedirs('rail-inference')

    while True:
        # Response format is {TopicPartiton('topic1', 1): [msg1, msg2]}
        msg_pack = consumer.poll(timeout_ms=500)
        for tp, messages in msg_pack.items():
            for message in messages:
                # print("%s:%d:%d: key=%s value=%s" % (tp.topic, tp.partition,
                #                                      message.offset, message.key,
                #                                      message.value))
                imagedata = json.loads(message.value)
                narray = np.array(imagedata['data'])
                title = imagedata['title']
                frameno = imagedata['frameno']
                filepath = path + "/rail-inference/" + title
                try:
                    os.mkdir(filepath)
                except OSError:
                    print("Creation of the directory %s failed" % path)
                else:
                    print("Successfully created the directory %s " % path)

                flename = filepath + "/" + title + "_" + str(frameno) + ".jpg"
                print(flename)
                cv2.imwrite(flename, narray)

                # print(imagedata['data'])
                print("======================")


def main():
    # Create 'my-topic' Kafka topic
    try:
        admin = KafkaAdminClient(bootstrap_servers='localhost:9092')

        topic = NewTopic(name='outputframes',
                         num_partitions=1,
                         replication_factor=1)
        admin.create_topics([topic])
    except Exception:
        pass

    subscribe()


if __name__ == "__main__":
    main()
