# Architecture diagrams

### Full System Architecture
```mermaid
graph TB
    %% Input Layer
    INPUT[📊 User Inputs<br/>repository_path<br/>programming_language<br/>project_name]
    
    %% Tools Layer
    subgraph TOOLS [🛠️ Tools Layer]
        T1[ScrapeWebsiteTool<br/>📄 Repository Access]
        T2[ScrapeElementTool<br/>🔍 Targeted Extraction]
        T3[SerperDevTool<br/>🔍 Research & Best Practices]
    end
    
    %% Agents Layer
    subgraph AGENTS [🤖 AI Agents Layer]
        A1[👤 Code Analyzer<br/>📁 Structure Analysis]
        A2[👤 Advanced Code Parser<br/>🔬 AST & Deep Analysis]
        A3[👤 Quality Inspector<br/>🛡️ Security & Quality]
        A4[👤 Rules Extractor<br/>📋 Business Logic]
        A5[👤 Architecture Generator<br/>🏗️ Visual Diagrams]
        A6[👤 Report Writer<br/>📝 Final Compilation]
    end
    
    %% Task Execution Flow
    subgraph TASKS [📋 Task Execution Layer]
        TASK1[Task 1: Analyze Codebase Structure<br/>📊 Repository mapping, dependencies, structure]
        TASK2[Task 2: Deep Code Parsing & AST<br/>🔬 Functions, classes, complexity metrics]
        TASK3[Task 3: Assess Code Quality<br/>🛡️ Security, performance, best practices]
        TASK4[Task 4: Extract Business Rules<br/>📋 Validation logic, conventions, workflows]
        TASK5[Task 5: Generate Architecture Diagrams<br/>🏗️ Visual system design, component maps]
        TASK6[Task 6: Comprehensive Report<br/>📄 Executive summary, recommendations]
    end
    
    %% Output Layer
    subgraph OUTPUTS [📊 Output Layer]
        O1[📊 Code Structure Analysis<br/>File inventory, dependencies<br/>Entry points, configurations]
        O2[🔬 AST Analysis Report<br/>Function signatures, class hierarchies<br/>Design patterns, complexity metrics]
        O3[🛡️ Quality Assessment<br/>Security vulnerabilities, code smells<br/>Performance issues, recommendations]
        O4[📋 Business Rules Documentation<br/>Validation logic, decision trees<br/>Workflow patterns, standards]
        O5[🏗️ Architecture Diagrams<br/>System diagrams, component maps<br/>Data flow charts, UML diagrams]
        O6[📄 Final Report<br/>Executive summary, integrated findings<br/>Prioritized roadmap, action plan]
    end
    
    %% Connections
    INPUT --> AGENTS
    
    %% Tool assignments
    T1 --> A1
    T1 --> A2
    T2 --> A5
    T3 --> A3
    T3 --> A4
    
    %% Agent to Task mapping
    A1 --> TASK1
    A2 --> TASK2
    A3 --> TASK3
    A4 --> TASK4
    A5 --> TASK5
    A6 --> TASK6
    
    %% Task dependencies and flow
    TASK1 --> TASK2
    TASK1 --> TASK3
    TASK2 --> TASK4
    TASK2 --> TASK5
    TASK3 --> TASK6
    TASK4 --> TASK6
    TASK5 --> TASK6
    
    %% Task to Output mapping
    TASK1 --> O1
    TASK2 --> O2
    TASK3 --> O3
    TASK4 --> O4
    TASK5 --> O5
    TASK6 --> O6
    
    %% Context flow between tasks
    O1 -.-> TASK2
    O1 -.-> TASK3
    O2 -.-> TASK4
    O2 -.-> TASK5
    O1 -.-> TASK6
    O2 -.-> TASK6
    O3 -.-> TASK6
    O4 -.-> TASK6
    O5 -.-> TASK6
    
    %% Styling
    classDef inputClass fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef toolClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef agentClass fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef taskClass fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef outputClass fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    
    class INPUT inputClass
    class T1,T2,T3 toolClass
    class A1,A2,A3,A4,A5,A6 agentClass
    class TASK1,TASK2,TASK3,TASK4,TASK5,TASK6 taskClass
    class O1,O2,O3,O4,O5,O6 outputClass
```


### 📊 Detailed Sequential Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant System
    participant CA as Code Analyzer
    participant ACP as Advanced Parser
    participant QI as Quality Inspector
    participant RE as Rules Extractor
    participant AG as Architecture Generator
    participant RW as Report Writer
    
    User->>System: Input repository_path, language, project_name
    
    Note over System: Phase 1: Initial Analysis
    System->>CA: Analyze repository structure
    CA->>CA: Scrape repository, identify files
    CA-->>System: Structure analysis complete
    
    Note over System: Phase 2: Deep Analysis
    System->>ACP: Parse code with AST analysis
    ACP->>ACP: Extract functions, classes, patterns
    ACP-->>System: Deep parsing complete
    
    par Parallel Quality & Rules Analysis
        System->>QI: Assess code quality
        QI->>QI: Research best practices, analyze security
        QI-->>System: Quality assessment complete
    and
        System->>RE: Extract business rules
        RE->>RE: Identify validation logic, workflows
        RE-->>System: Rules extraction complete
    end
    
    Note over System: Phase 3: Visualization
    System->>AG: Generate architecture diagrams
    AG->>AG: Create visual representations
    AG-->>System: Diagrams generated
    
    Note over System: Phase 4: Final Report
    System->>RW: Compile comprehensive report
    RW->>RW: Integrate all findings
    RW-->>System: Final report complete
    
    System-->>User: Complete analysis delivered
```

### 🔄 Data Flow Architecture
```mermaid
graph LR
    subgraph INPUT_DATA [📥 Input Data]
        I1[Repository URL]
        I2[Programming Language]
        I3[Project Name]
    end
    
    subgraph PROCESSING_PIPELINE [🔄 Processing Pipeline]
        
        subgraph STAGE1 [Stage 1: Ingestion]
            P1[Repository Scraping]
            P2[File Classification]
            P3[Dependency Mapping]
        end
        
        subgraph STAGE2 [Stage 2: Analysis]
            P4[AST Parsing]
            P5[Pattern Recognition]
            P6[Complexity Analysis]
            P7[Quality Metrics]
            P8[Security Scanning]
        end
        
        subgraph STAGE3 [Stage 3: Extraction]
            P9[Business Rules]
            P10[Validation Logic]
            P11[Configuration Rules]
            P12[Workflow Patterns]
        end
        
        subgraph STAGE4 [Stage 4: Visualization]
            P13[System Architecture]
            P14[Component Diagrams]
            P15[Data Flow Charts]
            P16[UML Diagrams]
        end
        
        subgraph STAGE5 [Stage 5: Reporting]
            P17[Data Integration]
            P18[Report Generation]
            P19[Recommendation Engine]
        end
    end
    
    subgraph OUTPUT_DATA [📤 Output Data]
        O1[Structure Report]
        O2[Quality Assessment]
        O3[Architecture Diagrams]
        O4[Business Rules Doc]
        O5[Final Report]
    end
    
    INPUT_DATA --> STAGE1
    STAGE1 --> STAGE2
    STAGE2 --> STAGE3
    STAGE2 --> STAGE4
    STAGE3 --> STAGE5
    STAGE4 --> STAGE5
    STAGE5 --> OUTPUT_DATA
```

### 🏛️ System Architecture - Component View
```mermaid
graph TB
    subgraph EXTERNAL [🌐 External Services]
        EXT1[GitHub Repository]
        EXT2[OpenAI API]
        EXT3[Serper Search API]
    end
    
    subgraph APPLICATION [🖥️ Application Layer]
        APP1[main.py - CLI Interface]
        APP2[crew.py - Orchestration]
        APP3[agents.py - Agent Definitions]
        APP4[tasks.py - Task Management]
        APP5[tools.py - Tool Configuration]
    end
    
    subgraph AGENTS_DETAILED [🤖 Agents - Detailed View]
        subgraph A1_DETAIL [Code Analyzer Agent]
            A1T[ScrapeWebsiteTool]
            A1F[Repository Analysis]
            A1O[Structure Mapping]
        end
        
        subgraph A2_DETAIL [Advanced Parser Agent]
            A2T[ScrapeWebsiteTool]
            A2F[AST Analysis]
            A2O[Code Complexity]
        end
        
        subgraph A3_DETAIL [Quality Inspector Agent]
            A3T[SerperDevTool]
            A3F[Best Practice Research]
            A3O[Quality Metrics]
        end
        
        subgraph A4_DETAIL [Rules Extractor Agent]
            A4T[SerperDevTool]
            A4F[Business Logic Detection]
            A4O[Rules Documentation]
        end
        
        subgraph A5_DETAIL [Architecture Generator Agent]
            A5T[ScrapeElementTool]
            A5F[Diagram Generation]
            A5O[Visual Architecture]
        end
        
        subgraph A6_DETAIL [Report Writer Agent]
            A6F[Content Integration]
            A6O[Final Report]
        end
    end
    
    subgraph STORAGE [💾 Storage Layer]
        S1[outputs/reports/]
        S2[Configuration Files]
        S3[Temporary Data]
    end
    
    %% Connections
    EXTERNAL --> APPLICATION
    APPLICATION --> AGENTS_DETAILED
    AGENTS_DETAILED --> STORAGE
    
    %% External service connections
    EXT1 --> A1T
    EXT1 --> A2T
    EXT1 --> A5T
    EXT2 --> A1F
    EXT2 --> A2F
    EXT2 --> A6F
    EXT3 --> A3T
    EXT3 --> A4T
```

### 📈 Performance & Scaling Architecture
```mermaid
graph TB
    subgraph PERFORMANCE [⚡ Performance Considerations]
        PERF1[Parallel Agent Execution<br/>Quality Inspector || Rules Extractor]
        PERF2[Caching Layer<br/>Repository data, API responses]
        PERF3[Rate Limiting<br/>API call management]
        PERF4[Memory Management<br/>Large repository handling]
    end
    
    subgraph SCALING [📈 Scaling Options]
        SCALE1[Batch Processing<br/>Multiple repositories]
        SCALE2[Distributed Agents<br/>Cloud deployment]
        SCALE3[Database Integration<br/>Result persistence]
        SCALE4[Web Interface<br/>Multi-user access]
    end
    
    subgraph MONITORING [📊 Monitoring & Observability]
        MON1[Execution Metrics<br/>Time, cost, success rate]
        MON2[Quality Metrics<br/>Analysis accuracy, completeness]
        MON3[Error Tracking<br/>Failures, retries, recovery]
        MON4[Usage Analytics<br/>Popular features, patterns]
    end
```
