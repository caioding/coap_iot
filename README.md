# CoAP IoT Monitoring and Actuation System

This project is a comprehensive implementation of a CoAP (Constrained Application Protocol) ecosystem, featuring a Python-based server and an Android client application. It demonstrates remote monitoring of system resources and remote actuation over a network, specifically designed for IoT (Internet of Things) environments.

## Project Architecture

The system is divided into two main components:

1.  **CoAP Server (Python):** Runs on a host computer, exposing system metrics (CPU, Memory, Disk) and simulated sensors as CoAP resources.
2.  **Android Client (Kotlin):** A mobile application that discovers available resources, performs GET/POST requests, and uses the Observe mechanism for real-time updates.

## Features

-   **Resource Discovery:** Implements `/.well-known/core` for automatic client-side resource identification.
-   **Real-time Monitoring:** Uses the CoAP **Observe** mechanism to stream CPU usage updates without constant polling.
-   **Remote Actuation:** Send messages to the server's display or logs via JSON payloads over POST requests.
-   **System Metrics:** Access real-time data from the host machine (Uptime, Hostname, Memory, Disk).
-   **Environment Simulation:** Includes simulated sensors like random temperature for testing purposes.

## Repository Structure

```text
coap_iot/
├── app/                  # Android Studio Project (Kotlin)
│   ├── src/main/java     # Logic and CoAP Repository (Californium)
│   └── src/main/res      # UI Layout and Resources
├── coap_iot_lab/         # CoAP Server (Python)
│   ├── app/              # Resource and Service logic
│   ├── run_server.py     # Main entry point
│   └── requirements.txt  # Python dependencies
└── README.md
```

## Setup Instructions

### 1. Server Setup (Python)
Navigate to the `coap_iot_lab` directory:
```bash
cd coap_iot_lab
python3 -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```
Update the `HOST` IP in `app/config.py` to match your local network address, then run:
```bash
python run_server.py
```

### 2. Android Client Setup
1.  Open the `coap_iot` project in Android Studio.
2.  Ensure you have the `Californium` library dependency synced via Gradle.
3.  Deploy the app to your Android device (e.g., Raspberry Pi with Android or a standard smartphone).
4.  Enter the Server IP in the application UI.
5.  Click **"Descobrir Recursos"** (Discover Resources) to start interacting.

## Technologies Used

-   **CoAP Protocol:** RFC 7252 / RFC 7641 (Observe).
-   **Server:** [aiocoap](https://aiocoap.readthedocs.io/) (Asynchronous Python CoAP library).
-   **Client:** [Eclipse Californium](https://www.eclipse.org/californium/) (Java/Android CoAP framework).
-   **Android:** Kotlin, ViewBinding, and Coroutines.

## License
This project was developed for educational purposes as part of an IoT laboratory practice.
