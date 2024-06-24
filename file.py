import random
import time

# Incident types
incident_types = ["Network Outage", "Data Breach", "Malware Outbreak", "DDoS Attack", "System Failure"]

# Incident severities
incident_severities = ["Low", "Medium", "High", "Critical"]

# Incident response teams
incident_response_teams = ["Network Team", "Security Team", "IT Team", "Management Team"]

# Incident response actions
incident_response_actions = ["Investigate", "Contain", "Eradicate", "Recover", "Post-Incident Activities"]

class Incident:
    def __init__(self, incident_type, incident_severity):
        self.incident_type = incident_type
        self.incident_severity = incident_severity
        self.response_team = random.choice(incident_response_teams)
        self.response_actions = []

    def respond(self):
        print(f"Incident Response Team: {self.response_team}")
        for i in range(random.randint(1, 5)):
            action = random.choice(incident_response_actions)
            self.response_actions.append(action)
            print(f"  - {action}")
        print()

def simulate_incident_response():
    print("Incident Response Simulation")
    print("---------------------------")
    while True:
        incident_type = random.choice(incident_types)
        incident_severity = random.choice(incident_severities)
        print(f"Incident Detected: {incident_type} ({incident_severity})")
        incident = Incident(incident_type, incident_severity)
        incident.respond()
        time.sleep(0)  # wait for 0 seconds before simulating the next incident

if __name__ == "__main__":
    simulate_incident_response()