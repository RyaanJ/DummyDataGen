import random
import time


# Function to generate hardware logs
def generate_hardware_logs():
    # List of hardware log levels
    log_levels = [
        "UTILIZATION - CPU 50%",
        "UTILIZATION - CPU 60%",
        "UTILIZATION - CPU 70%",
        "UTLIZATION - GPU 50%",
        "UTILIZATION - GPU 60%",
        "UTILIZATION - GPU 70%",
        "UTILIZATION - RAM 50%",
        "UTILIZATION - RAM 60%",
        "UTILIZATION - RAM 70%",
        "UTILIZATION - STORAGE 50%",
        "UTILIZATION - STORAGE 60%",
        "UTILIZATION - STORAGE 70%",
        "WARNING - High CPU Usage - 80%",
        "WARNING - High GPU Usage - 80%",
        "WARNING - High RAM Usage - 80%",
        "WARNING - High Storage Usage - 80%",
        "WARNING - High CPU Usage - 90%",
        "WARNING - High GPU Usage - 90%",
        "WARNING - High RAM Usage - 90%",
        "WARNING - High Storage Usage - 90%",
    ]
    # Infinite loop to generate hardware logs every 2 to 8 seconds
    while True:
        log_level = random.choice(log_levels)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        message = f"{log_level} - {timestamp}"

        # Print the hardware log message
        print(message)

        # Rest log gen for a random interval between 2 to 8 seconds
        time.sleep(random.randint(2, 7))


# Call the function to start generating hardware logs
generate_hardware_logs()
# Ctrl + C to stop the program
# End of file
