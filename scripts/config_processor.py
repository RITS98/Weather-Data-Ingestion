import configparser

class config_reader:
    """
    A class to read and parse .ini files
    
    Parameters:
    file_path (str) : The path to the .ini file
    config (configparser.ConfigParser) : The ConfigParser object to parse .ini files
    """
    
    def __init__(self, file_path):
        """
        Initialize the configparser with the path to the .ini files
        
        Parameters
        file_path (str): The path to the .ini file.
        """
        self.config = configparser.ConfigParser()
        self.file_path = file_path
        self.config.read(file_path)
        
    def get_sections(self):
        """
        Get all sections in the .ini file.
        
        Returns:
        list : A list of section names
        """
        
        return self.config.sections()
    
    def get_options(self, section):
        """
        Get alloptions under a specific section
        
        Parameters:
        section (str) : The name of the section
        
        Returns:
        list : A list containing names of options under a specific section
        
        Raises:
        ValueError : If the specified section is not found in the .ini file.
        """
        
        if section in self.config:
            return self.config.options(section)
        else:
            raise ValueError(f"Section '{section}' not found in the .ini file")
        
    
    def get_value(self, section, option):
        """
        Get the value of a specific option under a specific section
        
        Parameters:
        section (str) : The name of the section
        option (str) : The name of the option
        
        
        Returns:
        str : Value of the specified option
        
        Raises:
        ValueError : If the specified section or option is not found in the .ini files
        """
        
        if section in self.config:
            if option in self.config[section]:
                return self.config.get(section, option)
            
            else:
                raise ValueError(f"Option '{option}' not found in section '{section}'")
            
        else:
            raise ValueError(f"Section '{section}' not found in the ini file.")
        
        
    def has_section(self, section):
        """
        Check if the .ini file has a specfic section
        
        Parameters:
        section (str) : The name of the section
        
        Returns:
        bool : True if the section exists, False otherwise
        """
        
        return self.config.has_section(section)
    
    
    def has_option(self, section, option):
        """
        Check if the .ini file has a specidfic option under a specific section
        
        Parameters:
        section (str) : The name of the section
        option (str) : The name of the option
        
        Returns:
        bool : True if the optionexists in the section, False otherwise. 
        """
        
        return self.config.has_option(section, option)
        
    