"""
Tool configurations for the Code Analyzer
Centralized tool setup with custom parameters
"""

from crewai_tools import (
    ScrapeWebsiteTool, 
    ScrapeElementFromWebsiteTool, 
    SerperDevTool
)
import os

class AnalyzerTools:
    """Centralized tool management for code analysis"""
    
    def __init__(self):
        self._scrape_tool = None
        self._scrape_element_tool = None
        self._search_tool = None
    
    @property
    def scrape_tool(self):
        """Web scraping tool for repository analysis"""
        if self._scrape_tool is None:
            self._scrape_tool = ScrapeWebsiteTool()
        return self._scrape_tool
    
    @property
    def scrape_element_tool(self):
        """Element-specific scraping tool"""
        if self._scrape_element_tool is None:
            self._scrape_element_tool = ScrapeElementFromWebsiteTool()
        return self._scrape_element_tool
    
    @property
    def search_tool(self):
        """Internet search tool for research"""
        if self._search_tool is None:
            # Check if API key is available
            if not os.getenv('SERPER_API_KEY'):
                print("⚠️  Warning: SERPER_API_KEY not found. Search functionality may be limited.")
            self._search_tool = SerperDevTool()
        return self._search_tool

# Custom tool configurations
def get_repository_scraper():
    """Specialized tool for repository analysis"""
    return ScrapeWebsiteTool(
        # Add any custom parameters here
    )

def get_code_quality_researcher():
    """Specialized tool for code quality research"""
    return SerperDevTool(
        # Custom search parameters for code quality research
    )

def get_architecture_analyzer():
    """Tool for analyzing architecture patterns"""
    return ScrapeElementFromWebsiteTool(
        # Custom parameters for architecture analysis
    )

# Tool factory function
def create_tool_set():
    """Create a complete set of tools for code analysis"""
    tools = AnalyzerTools()
    
    return {
        'scrape_tool': tools.scrape_tool,
        'scrape_element_tool': tools.scrape_element_tool,
        'search_tool': tools.search_tool,
        'repository_scraper': get_repository_scraper(),
        'quality_researcher': get_code_quality_researcher(),
        'architecture_analyzer': get_architecture_analyzer()
    }

# Validation function
def validate_tools():
    """Validate that all required tools can be initialized"""
    try:
        tools = create_tool_set()
        print("✅ All tools initialized successfully")
        
        # Check API keys
        #required_keys = ['SERPER_API_KEY']
        required_keys = ['GOOGLE_API_KEY']
        missing_keys = []
        
        for key in required_keys:
            if not os.getenv(key):
                missing_keys.append(key)
        
        if missing_keys:
            print(f"⚠️  Missing API keys: {', '.join(missing_keys)}")
            print("   Some tools may have limited functionality")
        
        return True
        
    except Exception as e:
        print(f"❌ Tool validation failed: {e}")
        print("   Please ensure all dependencies and API keys are correctly set up.")
        return False

if __name__ == "__main__":
    # Test tools when run directly
    print("🔧 Testing Code Analyzer Tools...")
    validate_tools()