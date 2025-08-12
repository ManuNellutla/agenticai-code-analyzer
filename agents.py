from crewai import Agent, LLM
from tools import create_tool_set
import os


def setup_gemini_flash():
    """Fast and free Gemini model"""
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
    return LLM(

        model="gemini/gemini-2.0-flash",
        temperature=0.1,
        api_key=api_key
)

def create_agents():
    """Create all the agents for code analysis"""
    
    # Get centralized tools
    tools = create_tool_set()
    
    code_analyzer = Agent(
        role='Code Analyzer',
        goal='Analyze the codebase at {repository_path} to identify file structure, main components, dependencies, and basic code patterns in {programming_language}.',
        backstory='''You are a software engineer with expertise in code analysis across multiple programming languages. You can quickly scan codebases to understand their structure, identify key files, and extract basic metrics and patterns.''',
        tools=[tools['repository_scraper']],  # Using specialized tool
        llm=setup_gemini_flash(),
        verbose=True
    )
    
    quality_inspector = Agent(
        role='Quality Inspector',
        goal='Review the analyzed code for quality issues, security vulnerabilities, best practices violations, and provide improvement recommendations for {project_name}.',
        backstory='''You are a senior code reviewer with extensive experience in software quality assurance. You can identify common code smells, security issues, and provide practical recommendations for improvement based on industry best practices.''',
        tools=[tools['quality_researcher']],  # Using specialized tool
        llm=setup_gemini_flash(),
        verbose=True
    )
    
    advanced_parser = Agent(
        role='Advanced Code Parser',
        goal='Perform deep code parsing and AST analysis of {programming_language} files, extracting function signatures, class hierarchies, dependency graphs, design patterns, and complex code relationships for {project_name}.',
        backstory='''You are a compiler engineer and static analysis expert with deep knowledge of Abstract Syntax Trees (AST), code parsing techniques, and program analysis. You can dissect code at the deepest level, understanding complex inheritance patterns, dependency chains, and architectural patterns that others might miss.''',
        tools=[tools['scrape_tool']],
        llm=setup_gemini_flash(),
        verbose=True
    )
    
    rules_extractor = Agent(
        role='Rules Extractor',
        goal='Extract business rules, validation logic, configuration rules, coding standards, and implicit rules from the {programming_language} codebase at {repository_path}, documenting them clearly for {project_name}.',
        backstory='''You are a business analyst and code archaeologist with expertise in identifying and documenting business logic embedded in source code. You have a keen eye for spotting validation rules, business constraints, configuration patterns, and implicit decision logic that often goes undocumented.''',
        tools=[tools['search_tool']],
        llm=setup_gemini_flash(),
        verbose=True
    )
    
    architecture_generator = Agent(
        role='Architecture Diagrams Generator',
        goal='Generate visual architecture diagrams, component relationship maps, data flow diagrams, and system interaction charts for {project_name} based on the analyzed codebase structure.',
        backstory='''You are a software architect and technical illustrator with expertise in creating clear, informative system diagrams. You excel at visualizing complex software architectures, data flows, and component relationships using various diagramming standards like UML, C4 model, and flowcharts.''',
        tools=[tools['architecture_analyzer']],  # Using specialized tool
        llm=setup_gemini_flash(),
        verbose=True
    )
    
    report_writer = Agent(
        role='Report Writer',
        goal='Create a comprehensive analysis report for {project_name} summarizing code structure, quality findings, and actionable recommendations in a clear, professional format.',
        backstory='''You are a technical writer specializing in software analysis reports. You excel at synthesizing complex technical findings into clear, actionable reports that serve both developers and stakeholders.''',
        llm=setup_gemini_flash(),
        verbose=True
    )
    
    return {
        'code_analyzer': code_analyzer,
        'quality_inspector': quality_inspector,
        'advanced_parser': advanced_parser,
        'rules_extractor': rules_extractor,
        'architecture_generator': architecture_generator,
        'report_writer': report_writer
    }
    
