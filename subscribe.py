import requests

STREAM_URL = "http://127.0.0.1:5000/"  # Replace with the URL of the JSON stream
WINDOW_SIZE = 3  # Maximum number of events in the sliding window


def subscribe_to_stream():
    response = requests.get(STREAM_URL, stream=True)

    if response.status_code == 200:
        event_buffer = []
        for line in response.iter_lines():
            if line:
                event = line.decode("utf-8")
                event_buffer.append(event)
                event_buffer = event_buffer[-WINDOW_SIZE:]  # Truncate the list to maintain the sliding window
                process_event(event, event_buffer)  # Replace with your logic to handle each event and sliding window

                # Add your own logic to stop the subscription if needed
    else:
        print("Failed to connect to the stream. Status code:", response.status_code)


def process_event(event, event_buffer):
    # Replace this with your logic to handle each event and sliding window
    print("Received event:", event)
    # print("Sliding window:", event_buffer)


if __name__ == "__main__":
    subscribe_to_stream()
