

class ExtractionData():
    def __init__(self) -> None:
        self.worksheetId = None 
        self.studnetId = None 
        self.questionsId = None 
        pass

class ExtractionDataBuilder():
    def __init__(self, extraction_data = ExtractionData()) -> None:
        self.extraction_data = extraction_data
    
    def set_worksheet(self, worksheetId):
        self.extraction_data.worksheetId  = worksheetId
        return self
    
    def build(self):
        return self 