# Requirements

## Functional Requirements

#### FR-1 File Analysis Malware Detection

- **What**: Scan all inbound files/emails for malware
- **Input**: REST API - file path in json. Max file size 2GB.
- **Output**: REST API - json report in response. Response includes verdict (clean/malware/suspicious). Produces alert with file hash, source IP, timestamp if malware or suspicious.
- **Performance**:
  - Scan completion: < 2 minutes for 95% of files
  - Alert generation: < 30 seconds after malware detection
  - Max queue time: < 5 minutes during peak load
