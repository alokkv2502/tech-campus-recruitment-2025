## Approaches Considered
### 1. **Full File Load (Not Used)**
- Loads the full log file into memory and filters data.
- **Disadvantage**: Memory-intensive, unsuitable for 1TB files.

### 2. **Line-by-Line Streaming (Final Choice)**
- Reads logs line by line and writes matching entries to an output file.
- **Advantage**: Uses minimal memory.
- **Optimization**: Uses buffered reading and regex.

### 3. **Using grep (Unix-based)**
- Simple but not cross-platform.
- Example:
  ```bash
  grep "^2024-12-01" logs.txt > output/output_2024-12-01.txt

  ### **Step 4: Running the Project**
#### **1. Navigate to the Project Directory**
```bash
cd log_extractor
cd tech-campus-recruitment-2025
run the below command in terminal:
python src/extract_logs.py logs_2024.log 2024-12-01  