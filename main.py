#!/usr/bin/env python3
"""
Advanced Code Analyzer with Architecture & Rules
Built with CrewAI Framework
"""

import os
from dotenv import load_dotenv
from crew import CodeAnalyzerCrew
from tools import validate_tools

def main():
    # Load environment variables
    load_dotenv()
    
    print("🔍 Advanced Code Analyzer with Architecture & Rules")
    print("=" * 60)
    
    # Validate tools first
    print("🔧 Validating tools...")
    if not validate_tools():
        print("❌ Tool validation failed. Please check your configuration.")
        return
    
    # Get user inputs
    repository_path = input("\nRepository URL or Path: ") or "https://github.com/ManuNellutla/scrappad"
    programming_language = input("Programming Language: ") or "Python"
    project_name = input("Project Name: ") or "Scrappad Enhanced Analysis"
    
    # Create inputs dictionary
    inputs = {
        'repository_path': repository_path,
        'programming_language': programming_language,
        'project_name': project_name
    }
    
    # Initialize and run the crew
    print(f"\n🚀 Starting analysis for: {project_name}")
    print(f"📂 Repository: {repository_path}")
    print(f"💻 Language: {programming_language}")
    print("-" * 60)
    
    try:
        crew = CodeAnalyzerCrew()
        result = crew.run(inputs)
        
        # Save results
        output_file = f"outputs/reports/{project_name.replace(' ', '_')}_analysis.md"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        
        print(f"\n✅ Analysis complete!")
        print(f"📄 Report saved to: {output_file}")
        print(f"📊 Report size: {len(result)} characters")
        
    except Exception as e:
        print(f"\n❌ Analysis failed: {e}")
        print("Please check your API keys and network connection.")

if __name__ == "__main__":
    main()