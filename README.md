# Real-Time Chat Application

A lightweight, real-time command-line chat application built using Python's native `socket` and `threading` libraries. This project satisfies the requirements for the **Oasis Infobyte SIP Task 5**.

---

## 🚀 Features (Beginner Tier)
* **Multi-Client Support**: Handles bidirectional messaging concurrently using multithreading.
* **Timestamp Prefixes**: Every message is prefixed with a real-time timestamp (e.g., `[14:35] Alice: Hello`).
* **Graceful Disconnection**: Clients can type `exit` to disconnect cleanly, which safely removes them from the server's tracking list.
* **Localhost Execution**: Runs completely on a local machine using the loopback IP `127.0.0.1`.

---

## 🔒 Security & Storage Transparency
As required by the project guidelines, here is how data and privacy are handled in this tier:

* **Message Storage**: Currently, this application does **NOT** store messages in a persistent database (like SQLite). Messages exist solely in volatile system memory (`RAM`) while active streams are running. Once the server or client terminal is closed, the chat logs are permanently cleared.
* **Encryption Status**: Messages sent through this application are **NOT encrypted**. They are transmitted across standard TCP sockets as plaintext bytecode strings (`utf-8`). This means anyone capturing or sniffing network packets on the local network could easily read the chat conversations.

---

## 🛠️ How to Run and Test

Follow these steps to run the application on your local machine using PowerShell or terminal:

### 1. Start the Server
Open a terminal panel inside the project folder and run:
```bash
python server.py
