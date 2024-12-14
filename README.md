# Face-Recognition-Based-File-Security-System

## Overview
The **Face Recognition File Security System** is a robust solution for securing files using face recognition as the primary authentication mechanism. The system employs a webcam to capture a user's face and verifies it against pre-stored encodings to grant or deny access to sensitive files. It ensures that files remain encrypted and inaccessible without proper authentication, adding an additional layer of security.

## System Components

### 1. User Interface (GUI)
- Built using **Tkinter**, the GUI allows users to interact with the system.
- Features include:
  - A main window for navigating the system.
  - Buttons to trigger key actions like creating and opening secure files.

### 2. Authentication
- Utilizes **Face Recognition** for user authentication.
- Components:
  - **Face Capture:** Captures the user’s face using the webcam.
  - **Face Recognition:** Compares the captured face with stored face encodings.

### 3. File Management
- Ensures secure file creation and editing.
- Features include:
  - Encryption and decryption of files using the **Fernet encryption algorithm**.
  - Securely stores files after encryption.

### 4. Storage
- Stores user data and files in separate directories:
  - **User Face Encodings:** Stores face data for each user.
  - **Secure Files:** Encrypted files are securely stored.
  - **Encryption Key:** A unique key file used for encrypting and decrypting data.

### 5. System Services
- Accesses essential system functionalities:
  - **Webcam Access:** Captures live video for face recognition.
  - **Notepad Integration:** Opens secure files for editing and monitors user presence during the session.

## Workflow

1. **Create a Secure File**:
   - User provides their username.
   - The system captures and stores their face encoding.
   - A new file is created and encrypted before saving.

2. **Open a Secure File**:
   - User selects a file to open.
   - The system authenticates the user by verifying their face.
   - Upon successful authentication:
     - The file is decrypted and opened for editing.
     - User presence is monitored to ensure continued security.
   - After editing, the file is re-encrypted and securely stored.

3. **Authentication**:
   - Captures the user's face using the webcam.
   - Matches the captured face with stored encodings.
   - Grants or denies access based on the match result.

## Key Features
- **Face Recognition-Based Security:** Leverages advanced facial recognition for secure and seamless authentication.
- **File Encryption:** Uses state-of-the-art encryption algorithms to ensure data privacy.
- **User Presence Monitoring:** Continuously monitors for authorized users during file access sessions.
- **Simple Interface:** Intuitive GUI for easy interaction with the system.

## Architectural Design
The system’s architecture integrates various modules, including user interaction, authentication, file management, and storage, to ensure a cohesive and secure workflow. Refer to the **Data Flow Diagram (DFD)** and **System Architecture Diagram** for a detailed representation of component interactions.
