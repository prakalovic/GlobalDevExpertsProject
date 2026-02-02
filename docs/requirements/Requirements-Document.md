# Requirements

## Functional Requirements

#### FR-1 File Analysis Malware Detection

- **What**: Scan all inbound files/emails for malware.
- **Input**: REST API - file path in json.
- **Output**:
  - REST API - json report in response. Response includes verdict (clean/malware/suspicious).
  - Asynchronuous. Produces alert with file hash, source IP, timestamp if malware or suspicious.

#### FR-2 Command and Control Detector Trafic Analysis

- **What**: Read all outbound traffic metadata and produce alerts on unusual behavior.
- **Input**: REST API - source, destination and message size in json.
- **Output**: Asynchronuous. Produces alert with summarized details (suspicious activity type, related traffic details).

## Non Functional Requirements

#### NFR-1 File Analysis Malware Detection

#### NFR-2 Command and Control Detector Trafic Analysis

- In-memory cache should be able to store recent metadata (30 minutes)
