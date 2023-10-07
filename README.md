# Attendance System

## Overview

This is an advanced attendance system designed to streamline the attendance tracking process for classrooms, meetings, or events. It provides the following features:

- Add new students or attendees by providing their name, ID, and a photo.
- Take attendance through a camera using facial recognition.
- Track which students or attendees are present and which are not.
- Manually add or remove students or attendees as needed.
- Download the attendance sheet for the classroom or event.

## Features

### Adding New Students/Attendees

- To add a new student or attendee, provide their name, unique ID, and a photo.
- The system will store this information for future attendance tracking.

### Taking Attendance through a Camera

- Use the camera feature to take attendance automatically through facial recognition.
- The system will identify registered students/attendees and mark them as present.
- Records will be created for attendance history.

### Tracking Attendance

- The system keeps track of attendance records, indicating which students/attendees are present and which are absent.
- View real-time attendance status during the session.

### Manual Student/Attendee Management

- Manually add or remove students/attendees as needed.
- This feature is useful for accommodating last-minute additions or exclusions.

### Downloading Attendance Sheets

- Download the attendance sheet for the classroom or event in various formats (e.g., CSV, Excel).
- Use these sheets for record-keeping or reporting purposes.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/attendance-system.git
   ```
2. Install the necessary dependencies.

   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:

   ```bash
   python flask_app.py
   ```
4. Access the system via a web browser at http://localhost:5000.