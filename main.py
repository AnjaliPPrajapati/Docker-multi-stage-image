# region Imports

# Standard Libraries
import time
import traceback

# Third party libraries
import pika
import pika.exceptions

# endregion

# ---------------------------------------------------------------------------------------------------

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}",flush = True)

def create_connection(queue_name:str, username:str, password:str, host:str, port:int) -> None:
    """This will be used to create connection with RabbitMQ and start consuming msgs

    Args:
        queue_name (str): queue name from which data has to be consumed
        username (str): RabbitMQ username 
        password (str): RabbitMQ password
        host (str): RabbitMQ host name or IP
        port (int): RabbitMQ port number
    """

    while True:
        try:            
            print('Connecting...', flush=True)

            credentials = pika.PlainCredentials(username, password)
            connection = pika.BlockingConnection(
                parameters=pika.ConnectionParameters(
                    host=host,
                    port=port,
                    virtual_host='/',
                    credentials=credentials,
                ),
            )
    
            channel = connection.channel()

            print('Connected to channel...',flush=True)

            # Declare a queue (it will create if it doesn't exist)
            channel.queue_declare(queue=queue_name)

            # Set up the consumer to listen to the queue
            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

            print(f"Waiting for messages in {queue_name}. To exit press CTRL+C",flush = True)
            try:
                # Start receiving messages
                channel.start_consuming()
            except KeyboardInterrupt:
                # Graceful exit on interrupt
                print("Exiting...",flush = True)
                connection.close()

            break # if connected no need to loop

        except pika.exceptions.ConnectionClosedByBroker:
            print('connection closed by broker sleeping for 5 sec...',flush = True)

            time.sleep(5) # sleep for 5 sec then try connecting again
            continue

        except pika.exceptions.AMQPChannelError as err:
            print(f"Caught a channel error: sleeping for 5 sec... -> {err} -> {traceback.format_exc()}",flush = True)
            
            time.sleep(5) # sleep for 5 sec then try connecting again
            continue

        # Recover on all other connection errors
        except pika.exceptions.AMQPConnectionError as error:
            print(f"Connection was closed, retrying again after 5 seconds... -> {traceback.format_exc()}",flush = True)

            time.sleep(5) # sleep for 5 sec then try connecting again
            continue

print('Inside Python file...',flush=True)
create_connection('my_queue', 'your_username', 'your_password', 'localhost', 5672)

# FOR Publishing

# import pika
# import time

# try:
#     credentials = pika.PlainCredentials('your_username', 'your_password')
#     connection = pika.BlockingConnection(
#         parameters=pika.ConnectionParameters(
#             host='localhost',
#             port=5672,
#             virtual_host='/',
#             credentials=credentials,
#         ),
#     )

#     channel = connection.channel()

#     # Declare a queue
#     channel.queue_declare(queue='hello')

#     # Publish a message
#     channel.basic_publish(exchange='',
#                         routing_key='hello',
#                         body='Hello World!')

#     print(" [x] Sent 'Hello World!'", flush=True)
#     connection.close()

#     # Sleep for a while to simulate a long-running process
#     time.sleep(5)
# except:
#     print(22222222222222222,flush=True)