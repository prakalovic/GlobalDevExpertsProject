# CyberFortNexus - Key Terms & Concepts

## System Components

### Detection System

- **What**: Only detects threats, does NOT block or prevent
- **Like**: Security camera that watches and alerts, not a guard that takes action

### On-Premises

- Installed at customer's location (their data center)
- NOT in the cloud
- Customer owns/controls the hardware

### Gateway

- Border between company's internal network and internet
- All internet traffic passes through here
- Where sensors monitor traffic

## Sensors & Detection

### File Analysis Sensor

- Scans inbound files/emails for malware/viruses
- Uses 3rd party anti-virus engine via REST API
- You build the sensor wrapper around it

### C&C (Command & Control) Detector

- Monitors outbound traffic for compromised machines "phoning home"
- Uses ML to detect suspicious patterns
- Example: Laptop connecting to hacker server every 5 minutes

### Network Forensics / Netflow Collector

- Records metadata of ALL traffic (both directions - duplex)
- Stores for 3 months for investigation
- Does NOT store packet content, only metadata

## Core Components

### ACI (Automatic Cyber Investigator)

- The "brain" of the system
- Correlates data from all sensors
- Automatically creates investigations by connecting related alerts
- Example: Links malware alert + C&C alert + forensics = "5 machines compromised"

### Investigation Portal

- Web interface for SOC analysts
- View alerts, investigate threats, manage cases
- Up to 50 users, each sees only their investigations

### SOC (Security Operations Center)

- Team/workspace where cybersecurity analysts work
- The people who USE your system
- Monitor threats 24/7, investigate incidents

## Technical Concepts

### IP (Internet Protocol)

- Addressing system for computers
- Example IPs: 192.168.1.50 (internal), 8.8.8.8 (Google)
- IP Traffic = data packets flowing between addresses

### Netflow / IP Flow Metadata

- Connection records (who talked to whom, when)
- Includes: Timestamp, Source IP, Dest IP, Ports, Protocol
- Does NOT include packet content
- Like phone records vs. actual conversations

### Port Mirroring

- Gateway switch copies all traffic to monitoring port
- Your sensors receive the duplicate copy
- Original traffic continues unaffected
- Like a security camera - watches but doesn't interfere

## Data Storage Strategy

### What Gets Stored Long-Term (3 months)

- ✅ Netflow metadata (feasible size)
- ✅ Alert records
- ✅ Investigation data

### What Gets Discarded After Analysis

- ❌ Full packet content (too large)
- Process → Extract what's needed → Delete packets

## Data Flow Summary

```
Mirrored Traffic → Network Forensics + C&C Detector
Inbound Files → File Analysis Sensor
All Sensors → Databases (Alerts + Forensics)
Databases → ACI (correlates) + Portal (displays)
```

## Sizing Tiers

- **Small**: 200 endpoints, 1 Gbps
- **Medium**: 1,000 endpoints, 5 Gbps
- **XLarge**: 10,000 endpoints, 50 Gbps

**Key Assumption**: 100 IP flows per minute per endpoint
