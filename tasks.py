from crewai import Task

def create_tasks(agents):
    """Create all tasks for the code analysis workflow"""
    
    analyze_structure = Task(
        description='''Analyze the codebase at {repository_path} to understand its structure, identify main files and directories, detect the primary {programming_language} files, find configuration files, and catalog dependencies. Provide an overview of the project organization and key components.''',
        expected_output='''A structured analysis containing:
- Project directory structure overview
- List of main source files and their purposes  
- Identified configuration files (package.json, requirements.txt, etc.)
- Dependencies and external libraries used
- Programming language distribution
- Entry points and main modules''',
        agent=agents['code_analyzer']
    )
    
    deep_parsing = Task(
        description='''Perform comprehensive code parsing and Abstract Syntax Tree (AST) analysis on the {programming_language} codebase. Extract detailed function signatures, class hierarchies, inheritance patterns, dependency graphs, design patterns, and complex code relationships. Analyze code complexity, coupling, and cohesion metrics.''',
        expected_output='''Detailed code parsing report including:
- Complete AST analysis with code structure breakdown
- Function and method signatures with parameter types
- Class hierarchy and inheritance relationships  
- Dependency graph showing module interconnections
- Design patterns identified (Singleton, Factory, Observer, etc.)
- Coupling and cohesion analysis
- Code complexity metrics (cyclomatic, cognitive)
- Interface and abstract class usage analysis''',
        agent=agents['advanced_parser'],
        context=[analyze_structure]
    )
    
    assess_quality = Task(
        description='''Review the analyzed codebase for {project_name} to identify quality issues, potential security vulnerabilities, code smells, and areas for improvement. Research best practices for {programming_language} and compare against the codebase findings.''',
        expected_output='''A quality assessment report including:
- Code quality score and key metrics
- Identified code smells and anti-patterns
- Security vulnerabilities and concerns
- Best practices violations
- Performance considerations
- Prioritized improvement recommendations''',
        agent=agents['quality_inspector'],
        context=[analyze_structure, deep_parsing]
    )
    
    extract_rules = Task(
        description='''Extract and document all business rules, validation logic, configuration rules, coding standards, and implicit rules embedded in the {project_name} codebase. Identify decision logic, constraints, business workflows, and rule patterns that govern the application behavior.''',
        expected_output='''Comprehensive rules documentation containing:
- Business rules and logic extracted from code
- Validation rules and data constraints identified
- Configuration rules and environment-specific logic
- Coding standards and conventions in use
- Implicit decision trees and conditional logic
- Workflow rules and process logic
- Security and authorization rules
- Data processing and transformation rules
- Rule categorization by priority and business impact''',
        agent=agents['rules_extractor'],
        context=[deep_parsing]
    )
    
    generate_diagrams = Task(
        description='''Create comprehensive visual architecture diagrams for {project_name} including system architecture, component relationships, data flow diagrams, and interaction charts. Generate multiple diagram types to visualize different aspects of the system architecture and design.''',
        expected_output='''Complete architecture diagram package including:
- High-level system architecture diagram with components
- Component relationship and dependency diagrams  
- Data flow diagrams showing information movement
- Class relationship diagrams (UML style)
- Module interaction and communication patterns
- Database schema and entity relationship diagrams
- API interaction and endpoint flow diagrams
- Deployment and infrastructure architecture diagrams
- Sequence diagrams for key workflows
- Diagram descriptions and architectural explanations''',
        agent=agents['architecture_generator'],
        context=[deep_parsing, extract_rules]
    )
    
    final_report = Task(
        description='''Compile all analysis findings into a comprehensive technical report for {project_name}. Integrate codebase analysis, quality assessment, deep parsing results, business rules documentation, and architecture diagrams into a unified, actionable report with executive summary and prioritized recommendations.''',
        expected_output='''Complete enhanced analysis report including:
- Executive summary with key findings and insights
- Project overview with structure and technology analysis
- Deep code analysis with AST findings and complexity metrics
- Extracted business rules and technical rules documentation
- Architecture diagrams with system design visualization
- Code quality assessment with detailed recommendations
- Security and performance analysis
- Prioritized improvement roadmap with timelines
- Technical debt analysis and remediation plan
- Maintenance and monitoring recommendations''',
        agent=agents['report_writer'],
        context=[analyze_structure, assess_quality, deep_parsing, extract_rules, generate_diagrams]
    )
    
    return [analyze_structure, deep_parsing, assess_quality, extract_rules, generate_diagrams, final_report]
