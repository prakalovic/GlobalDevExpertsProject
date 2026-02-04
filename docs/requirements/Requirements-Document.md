# Requirements

## Functional Requirements

- **FR-1**: The system should receive malware detection alerts and file scanning report from the File Analysis Sensor. Alert should include file path, threat type and timestamp via REST API.
- **FR-2**: The system should receive suspicious activity alerts from Malware Command and Control (C&C) Sensor. Alerts should be based on ML algorithm analysis of outbound activity.
- **FR-3**: The system should collect inbound and outbound netflow (_timestamp, Source+Dest IP, Source+Dest Port, protocol (tcp/udp), message length_) for Network Forensics.
- **FR-4**: Automatic Cyber Investigator (ACI) should automatically query information from sensors (File Analysis, Command and Control, Network Forensics) and generate alerts and automatic investigations for SOC analysts.
- **FR-5**: Investigation Portal should represent automatic investigations and alerts on the dashboard.
- **FR-6**: Investigation Portal must have access to alerts produced by sensors (File Analysis and C&C) and to Network Forensics.
- **FR-7**: System Administrators should be able to create accounts for SOC Analysts and manage permissions.
- **FR-8**: SOC Analyst should be able to authenticate into Investigation Portal.
- **FR-9**: SOC Analyst should be able to create and do own investigations through Investigation Portal.
- **FR-10**: Network Forensics should be cleaned up after 3 months.

## Non Functional Requirements

- **NFR-1**: File Analysis Sensor should not interrupt traffic.
- **NFR-2**: Network Forensics should not be stored longer than 3 months.
- **NFR-3**: Network Forensics should be able to log 100 IP flows per minute per endpoint on average and handle load in peak hours by scaling out horizontally.
- **NFR-4**: Data Collection to sensors should not affect traffic during peak hours.
- **NFR-5**: SOC Analyst cannot see other SOC Analyst investigations.
- **NFR-6**: Investigation Portal must have 2-factor authentication.
- **NFR-7**: The organization may define up to 50 different users in the system.
- **NFR-8**: The solution is installed on premises of the company.
- **NFR-9**: The solution should be 99.9% available.
- **NFR-10**: Sizing should be for 3 sizes of company networks:
  - Small – 200 endpoints (laptops/devices), 1 Gbps IP traffic peak
  - Medium – 1,000 endpoints, 5 Gbps IP traffic
  - XLarge – 10,000 endpoints, 50 Gbps IP traffic
- **NFR-11**: All components should report health status to central log collection service.
- **NFR-12**: System administrators should receive alerts when components are overloaded or unhealthy.
- **NFR-13**: Components should scale out horizontally when load increases and scale in when load decreases.
