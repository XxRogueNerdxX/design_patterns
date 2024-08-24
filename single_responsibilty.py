

class Journal:
    def __init__(self) -> None:
        self.entries = [] 
        self.count = 0 
    
    def add_entry(self, text): 
        self.count +=1  
        self.entries.append(f"{self.count}: {text}")
    
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self) -> str:
        return "\n".join(self.entries)

    """
    These files are doing more than just 
    journaling hence we change the class
    """
    # def save_journal(self, filename): 
    #     #saves the journal 
    #     pass
    
    # def load_journal(self, filename): 
    #     #loads the journla 
    #     pass
    
    # def load_from_web(self, uri):
    #     pass
"""
creating a new class that handles persistenace
alone
"""
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename): 
        #saves to file 
        pass 
    @staticmethod
    def load_from_file(journal, filename):
        #load from file 
        pass


j = Journal()
j.add_entry("test")
j.add_entry("my name is")
print(j)
    


