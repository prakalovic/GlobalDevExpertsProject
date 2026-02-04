# Requirements

## Functional Requirements

- **FR-1**: The system should receive malware detection alerts and file scanning reports from the File Analysis Sensor via REST API. Each alert should include file path, threat type, and timestamp.
- **FR-2**: The system should receive suspicious activity alerts from the Malware Command and Control (C&C) Sensor based on ML algorithm analysis of outbound traffic. Each alert should include relevant network metadata and threat indicators.
- **FR-3**: The system should collect inbound and outbound netflow (_timestamp, Source+Dest IP, Source+Dest Port, protocol (tcp/udp), message length_) for Network Forensics.
- **FR-4**: The Automatic Cyber Investigator (ACI) should continuously query information from all sensors (File Analysis, Command and Control, Network Forensics) to correlate events and generate alerts with automatic investigations for SOC analysts.
- **FR-5**: Investigation Portal should represent automatic investigations and alerts on the dashboard.
- **FR-6**: Investigation Portal must have access to alerts produced by sensors (File Analysis and C&C) and to Network Forensics.
- **FR-7**: System Administrators should be able to create accounts for SOC Analysts and manage permissions.
- **FR-8**: SOC Analysts should be able to log into the Investigation Portal.
- **FR-9**: SOC Analyst should be able to create and do their own investigations through Investigation Portal.

## Non Functional Requirements

- **NFR-1**: Data collection by sensors should not affect network traffic during peak hours (< 10ms added latency).
- **NFR-2**: Sizing should be for 3 sizes of company networks:
  - Small – 200 endpoints (laptops/devices), 1 Gbps IP traffic peak
  - Medium – 1,000 endpoints, 5 Gbps IP traffic
  - XLarge – 10,000 endpoints, 50 Gbps IP traffic
- **NFR-3**: Network Forensics should not be stored longer than 3 months.
- **NFR-4**: Network Forensics should be able to log 100 IP flows per minute per endpoint on average and handle the load in peak hours by scaling out horizontally.
- **NFR-5**: A SOC Analyst cannot see other SOC Analysts' investigations.
- **NFR-6**: Investigation Portal must have 2-factor authentication.
- **NFR-7**: The organization may define up to 50 different users in the system.
- **NFR-8**: The solution should be installed on-premises at the company site.
- **NFR-9**: The solution should be 99.9% available (sensors, databases, ACI, Investigation Portal).
- **NFR-10**: All components should report health status to a central log collection service.
- **NFR-11**: System administrators should receive alerts when components are overloaded or unhealthy.
- **NFR-12**: Components should scale out horizontally when load increases and scale in when load decreases.
- **NFR-13**: Solution deployment should be Container-based (Cloud Native).
