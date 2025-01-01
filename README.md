### Sherlock username Scanner

A web-based interface for the powerful [Sherlock Project](https://github.com/sherlock-project/sherlock). This application allows users to input one or more usernames and search for their presence across various social networks, generating detailed reports in CSV or XLSX format.

![Screenshot 2024-12-31 at 12 35 45](https://github.com/user-attachments/assets/29f85e0b-135a-4dd6-be99-f828c1293d57)

---

## **Features**
- **Web Interface**: Access Sherlock's functionality via an easy-to-use web interface.
- **Multiple Output Formats**: Generate results in `.txt`, `.csv`, or `.xlsx` formats.
- **Real-Time Feedback**: Displays scan progress with a loading spinner and status messages.
- **Customizable Options**: Users can choose which outputs they want (e.g., print all sites or found sites).
- **Downloadable Reports**: Reports are automatically generated and downloadable from the interface.
- **Built-In Error Handling**: Provides clear error messages for invalid input or failed scans.

---

## **Technologies Used**
- **Flask**: Backend web framework to manage requests and run the Sherlock scanning logic.
- **HTML/CSS/JavaScript**: Frontend for user interaction, designed with Bootstrap for responsive styling.
- **Python**: Sherlock integration and system management.
- **jQuery**: Simplified AJAX requests and DOM manipulation.

---

## **Getting Started**

You can run this locally or using docker. For docker instructions skip to [the docker section](#docker-install-instructions)

* First step, Clone the repository
```bash
   git clone https://github.com/your-username/sherlock-web-app.git
   cd sherlock-web-app
```

## **Local Install Instructions**

### **Prerequisites**
- Python 3.9 or later
- Virtual environment (`venv`) for Python package management
- [Sherlock Project](https://github.com/sherlock-project/sherlock)
- A modern web browser

---

### **Installation**
1. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Set up directories:
```bash
   mkdir output
```

---

### **Starting the application locally**
1. Start the Flask server:
```bash
   python app.py
```

---

## **Docker Install Instructions**
There is some make recipes to make this easier if you are using a posix terminal. This way you don't have to reference the docker compose commands.

### **Prerequisites**
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/) (Most new docker installations have docker compose)
- A modern web browser

---

### **Starting the application in docker**

1. Create your environment file
   ```bash
   cp .env.example .env
   ```

2. Run the make or docker compose command
```bash
   (make)      make up
   (no make)   docker-compose up -d
```

---

## **Using the Application**
Open your browser and navigate to:
   ```
   http://127.0.0.1:5001
   ```
![Screenshot 2024-12-31 at 12 37 51](https://github.com/user-attachments/assets/52fdc8d7-89d3-4510-9079-6238bb1b5c8f)

![Screenshot 2024-12-31 at 12 38 15](https://github.com/user-attachments/assets/522bf71b-9726-418e-86f7-c00cfe2c005c)

---

## **Usage**

1. **Enter a Username**: On the homepage, enter the username(s) you want to search for. You can input multiple usernames separated by spaces.
2. **Select Options**: Choose the desired output formats or additional scan settings:
   - Generate CSV Report
   - Generate XLSX Report
   - Print All Sites
   - Print Found Sites
3. **Run the Scan**: Click the "Run Scan" button to start the process. A spinner and progress message will appear.
4. **Download Results**: Once the scan is complete, download the generated reports directly from the interface.

---

## **Project Structure**
```plaintext
sherlock-web-app/
├── sherlock_app.py              # Main Flask application
├── requirements.txt             # Python dependencies
├── Makefile                     # Make recipes for docker commands
├── .env.example                 # env file for secrets (currently only used for docker)
├── templates/
│   └── index.html               # Frontend HTML template
├── static/
│   ├── style.css                # Custom CSS
│   └── lcnr.jpg                 # Logo file (optional, replace if needed)
├── docker/
│   ├── docker-compose.yml
│   └── Dockerfile
├── output/                      # Directory for output files
├── venv/                        # Python virtual environment
└── sherlock/                    # Cloned Sherlock repository
```

---

## **Customizing Sherlock Commands**
Modify `app.py` to add or remove options passed to Sherlock. For example, you can add specific sites to search by updating the `command` list in the `run_sherlock` function:
```python
command.extend(["--site", "twitter", "--site", "instagram"])
```

---

## **Acknowledgments**
This project leverages the amazing [Sherlock Project](https://github.com/sherlock-project/sherlock), an open-source tool for finding usernames across social networks. Special thanks to the Sherlock developers for their invaluable contributions to the open-source community.

---

## **Future Enhancements**
- Add authentication for secure access.
- Implement a database for scan history and user management.
- ~~Dockerize the application for simplified deployment.~~
- Allow more customizable scan options directly from the frontend.

---

## **License**
This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contributing**
We welcome contributions! Please submit issues or feature requests via the [GitHub Issues](https://github.com/your-username/sherlock-web-app/issues) page, or create pull requests for improvements.

---

**Happy Scanning!**
