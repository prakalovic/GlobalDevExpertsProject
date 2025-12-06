# GitHub Copilot Instructions for CyberFortNexus Project

## Communication Rules

- **CRITICAL**: Ask only ONE question at a time
- Wait for user response before proceeding to the next question
- Keep responses concise and focused
- Avoid overwhelming the user with multiple questions or options

## Project Overview

### Project Type

Software Architecture training project - High Level Design (HLD) document creation for an enterprise cybersecurity defense system.

### Project Name

**CyberFortNexus** - A comprehensive on-premises enterprise cyber defense solution

### Main Goal

Design and document a next-generation detection system that:

- Collects information from network sensors at the enterprise gateway
- Provides automated cyber investigation capabilities
- Enables SOC (Security Operations Center) analysts to detect, investigate, and analyze cyber attacks
- **NOTE**: System is detection-only, NOT mitigation

## System Architecture Components

### 1. Threat Detection Sensors (Gateway Level)

- **File Analysis Sensor** (Inbound Traffic)

  - 3rd party software component
  - Scans files and emails (POP3) for malware/viruses
  - REST API: sends file path in JSON, receives JSON report
  - Generates alerts on malware/virus detection

- **Command & Control (C&C) Detector** (Outbound Traffic)

  - Home-brew solution
  - ML-based detection of malware C&C traffic
  - Uses Python ML algorithm on raw packet metadata
  - Generates alerts on suspected C&C traffic

- **Network Forensics - Netflow Collector** (Duplex Traffic)
  - Indexes all gateway traffic (organization ↔ internet)
  - Captures IP metadata: timestamp, source/dest IP, source/dest ports, protocol (TCP/UDP)
  - 3-month data retention
  - Assumption: 100 IP flows per minute per endpoint (average)
  - Gateway switch mirrors all IP traffic to probe

### 2. ACI - Automatic Cyber Investigator

- The "brain" of the system
- Aggregates data from all detection engines
- Performs automatic queries to detect cyber incidents
- Sources:
  - File Analysis alerts
  - C&C detection alerts
  - Network Forensics data
- Outputs: Alerts for SOC analysts with investigation context

### 3. Investigation Portal

- Web-based interface for SOC analysts
- Key features:
  - View alerts from file and C&C sensors
  - Investigate network forensics data
  - Manage investigations (timeline of alerts + network recordings)
  - View ACI-generated automatic investigations
  - Dashboard and reports
  - User management: up to 50 users, each with access only to their own investigations

## Non-Functional Requirements

### Availability

- **99.9% availability required**

### Deployment

- On-premises installation at company sites
- **Cloud-native architecture** (container-based, VMs acceptable)

### Sizing - Three Company Tiers

| Tier   | Endpoints           | Peak IP Traffic |
| ------ | ------------------- | --------------- |
| Small  | 200 laptops/devices | 1 Gbps          |
| Medium | 1,000 endpoints     | 5 Gbps          |
| XLarge | 10,000 endpoints    | 50 Gbps         |

### Scalability & Monitoring

- All components must be scalable
- Health dashboard for all components
- Central log collection service

## Deliverables & Milestones

### Required Documentation

- **Full High Level Design (HLD) document** based on provided template

### HLD Document Structure

1. **Assumptions and Constraints**
2. **Requirements** (Functional & Non-Functional)
3. **Design**:
   - Component identification
   - Flow diagrams
   - Persistence/data storage decisions
   - Security considerations
   - Performance diagrams

### Submission Milestones

- **Week 5 (MS1)**: Preliminary solution diagram
- **Week 9 (MS2)**: Requirements document
- **Week 13 (MS3)**: HLD + Data + Security + Performance Diagrams
- **Final (MS4)**: Complete submission by end of course

### Recommended Diagramming Tools

- Draw.io / Diagrams.net
- Excalidraw
- Lucidchart
- Microsoft Visio / PowerPoint
- Gliffy for Confluence
- StarUML
- WebSequenceDiagrams
- Eraser.io
- Archi

## Technology Considerations

### Preferred Technologies

- **Containerization**: Docker, Kubernetes
- **Languages**: Python (ML algorithms), any suitable for REST APIs
- **Message Queuing**: Consider for sensor data collection
- **Databases**:
  - Time-series for forensics data
  - Relational for user management and investigations
  - NoSQL for flexible alert/event storage
- **API Design**: RESTful services
- **Monitoring**: Prometheus, Grafana, ELK stack, or similar

### Architecture Patterns to Consider

- Microservices architecture
- Event-driven architecture
- CQRS (Command Query Responsibility Segregation) for forensics
- Message broker patterns (Kafka, RabbitMQ, etc.)

## Key Design Principles

1. **Scalability First**: Design must handle 3 different sizing tiers
2. **Cloud-Native**: Container-based, stateless where possible
3. **High Availability**: 99.9% uptime requirement
4. **Security by Design**: This is a cybersecurity product
5. **Observable**: Comprehensive monitoring and logging
6. **Modular**: Clear separation of concerns between components
7. **Data Retention**: 3-month forensics data requirement
8. **Multi-tenancy**: Support for 50 users with data isolation

## Assistance Guidelines

When helping with this project:

1. Always refer back to these requirements
2. Consider the three sizing tiers in all design decisions
3. Validate designs against non-functional requirements
4. Suggest industry-standard tools and patterns for cybersecurity systems
5. Focus on HLD-level details, not implementation code
6. Remember: ONE question at a time
7. Help create clear, professional diagrams and documentation
8. Consider real-world enterprise deployment scenarios
9. Think about data flow, storage, and processing at scale
10. Address security, monitoring, and operational concerns

## Document Organization

Maintain the following structure in the repository:

```
/materials/          # Course materials and references
/docs/              # HLD documentation
  /diagrams/        # Architecture diagrams
  /requirements/    # Requirements documents
  /milestones/      # Milestone submissions
/notes/             # Architecture decisions and notes
```

## Current Status

- **Training**: Software Architecture course with Global Dev Experts
- **Instructor**: Avraham Poupko
- **Project Stage**: Initial setup and requirements gathering
- **Next Milestone**: Week 5 - Preliminary solution diagram

---

**Remember**: This is a learning project focused on architecture design, not implementation. Emphasis is on thoughtful, scalable, enterprise-grade design decisions.
