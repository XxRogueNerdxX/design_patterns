""""
You are developing a web scraper that needs to:

Visit a series of web pages.
Extract structured data such as product information (title, price, description).
Build a customized report based on the extracted data (JSON, XML, or HTML formats).
The web scraper should allow flexibility in how the web interactions are handled (e.g., using Selenium, Playwright, or manual HTTP requests).
Additionally:

The scraper may need to visit different websites with varying structures, so it should support customization for different scraping strategies.
It should be flexible enough to support future changes, such as modifying the steps for data extraction, altering the format of the final report, or changing the web interaction mechanism (e.g., switching from Playwright to another tool).
Task:
Design a solution using the Builder pattern to construct the scraping process step by step, allowing customization for different websites and report formats.
Use the Flyweight pattern to efficiently reuse objects for repetitive tasks like scraping similar sections of multiple pages or
"""



from abc import ABC, abstractmethod



class AbstractDataBuilder(ABC): 
    @abstractmethod
    def handle_data(self, data): 
        pass

class AbstractScaperToolBuilder(ABC): 
    @abstractmethod
    def start_scapping(self, data): 
        pass

class AbstractScaperFactory(ABC): 
    @abstractmethod
    def scrap(self, data): 
        pass
    @abstractmethod
    def store_scrapped_data(data): 
        pass


class XMLDataBuilder(AbstractDataBuilder): 
    def __init__(self, save_dir) -> None:
        self.save_dir = save_dir
    
    def handle_data(self, data):
        #stores the data 
        print(f"Storing the XML data {data}")
        pass

class JSONDataFacade(AbstractDataBuilder): 
    def __init__(self, save_dir) -> None:
        self.save_dir  = save_dir
    
    def handle_data(self, data):
        print(f"Storing JSON data {data}")
    

class BeautifulSoupScapperTool(AbstractScaperToolBuilder): 
    def __init__(self, data) -> None:
        self.data = data 

    def start_scapping(self, data):
        print(f"Starting to scrap {data} using BeautifulSoap API")

class ScarpyScapperTool(AbstractScaperToolBuilder): 
    def __init__(self, data) -> None:
        self.data = data 
    
    def start_scapping(self, data):
        print(f"Starting to scrap {data} using Scapy API")

class ScaperFactory(AbstractScaperFactory): 
    @classmethod
    def create(**)

# https://chatgpt.com/share/d502c4cb-2c7c-427f-a427-34cd907aede3


