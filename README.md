# Court Reservation Bot

A Python-based automation script that automatically books court reservations at NJAC using Selenium WebDriver.

## Prerequisites

1. **Python 3.8 or higher**
   - Download and install from [Python's official website](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"

## Installation

1. **Clone the repository**
   ```powershell
   git clone https://github.com/yourusername/njac-court-reservation.git
   cd njac-court-reservation
   ```

2. **Install required Python packages**
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

1. **Basic usage (with default values)**
   ```powershell
   python selenim.py
   ```

2. **With custom parameters**
   ```powershell
   python selenim.py --username "YourUsername" --password "YourPassword" --guest "Guest Name" --date "04/02/2025" --first-time "8:00am" --second-time "9:00am"
   ```

### Available Parameters

- `--username`: Your NJAC login username (default: "Vtata")
- `--password`: Your NJAC login password (default: "******")
- `--guest`: Guest name for the reservation (default: "Ripudaman Nanda")
- `--date`: Reservation date in MM/DD/YYYY format (default: "03/31/2025")
- `--first-time`: First preferred time slot (default: "7:00am")
- `--second-time`: Second preferred time slot (default: "8:00am")

## Scheduling with Windows Task Scheduler

1. **Open Task Scheduler**
   - Press `Windows + R`
   - Type `taskschd.msc` and press Enter

2. **Create Basic Task**
   - Click "Create Basic Task" in the right panel
   - Name: "NJAC Court Reservation"
   - Description: "Automated court reservation script"
   - Trigger: Choose "Daily" or "Weekly" based on your needs
   - Action: Start a program
   - Program/script: `python`
   - Add arguments: `"C:\path\to\your\script\selenim.py" --date "04/02/2025" --first-time "7:00am"`
   - Start in: `C:\path\to\your\script\directory`

3. **Advanced Settings**
   - In the task properties:
     - Check "Run with highest privileges"
     - Configure for: Windows 10
     - Set "Stop task if it runs longer than" to 5 minutes
     - In "Settings" tab, check "Allow task to be run on demand"

## Troubleshooting

1. **ChromeDriver Issues**
   - Ensure ChromeDriver version matches your Chrome browser version
   - Verify ChromeDriver is in your system PATH

2. **Python Path Issues**
   - Verify Python is added to PATH during installation
   - Try using full path to Python executable in Task Scheduler

3. **Script Execution Issues**
   - Check if all required packages are installed
   - Verify file paths in Task Scheduler are correct
   - Check Windows Event Viewer for detailed error messages

## Security Notes

- Store sensitive information (username, password) securely
- Consider using environment variables or a configuration file
- Never commit credentials to version control

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 