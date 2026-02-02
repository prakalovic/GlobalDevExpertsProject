# Requirements

## Functional Requirements

- **FR-1**: The system should receive malware detection alerts and file scanning report from the File Analysis Sensor. Alert should include file path, threat type and timestamp via REST API.
- **FR-2**: The system should receive suspicious activity alerts from Malware Command and Control (C&C) Sensor. Alerts should be based on ML algorythm analysis of outbound activity.
- **FR-3**: The system should collect inbound and outbound netflow for Network Forensics.
- **FR-4**: Automatic Cyber Investigator (ACI) should automatically query information from sensors (File Analysis, Command and Control, Network Forensics) and generate alerts and automatic investigations for SOC analysts.
- **FR-5**: Investigation Portal should represent automatic investigations and alerts on the dashboard. It must have access to alerts produced by sensors (File Analysis and C&C) and to Network Forensics
- **FR-6**: SOC Analyst should be able to log in into Investigation Portal, see automatic investigations created by ACI and do their own investigations by accessing data from sensors (alerts and Network Forensics)

## Non Functional Requirements

- **NFR-1**: File Analysis Sensor should not interrupt traffic.
- **NFR-2**: Network Forensics should not be stored longer than 3 months.
- **NFR-3**: Data Collection to sensors should not affect traffic during peak hours.
- **NFR-4**: SOC Analyst cannot see other SOC Analyst investigations.
- **NFR-5**: The organization may define up to 50 different users in the system.
- **NFR-6**: The solution is installed on premises of the company.
- **NFR-7**: The solution should be 99.9% available.
- **NFR-8**: Sizing should be for 3 sizes of company networks:
  - Small – 200 endpoints (laptops/devices), 1 Gbps IP traffic peak
  - Medium – 1,000 endpoints, 5 Gbps IP traffic
  - XLarge – 10,000 endpoints, 50 Gbps IP traffic
