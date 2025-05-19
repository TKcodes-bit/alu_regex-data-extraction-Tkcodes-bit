#!/usr/bin/env python3
#Import re

import re
sample_text = """
 anjaojane@gmail.com
 https://www.goole.com
 123-456-7890
 <div>hello</div>
 $100.00
 """
class datamine:
    def __init__(self):
        self.regex_rubric = {
            "Email addressess" :  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
            "URLs" : r'(?i)\b((?:https?://|www\.)[^\s]+)',
            "Phone numbers" : r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b',
            "Credit card numbers" : r'\b(?:\d{4}[-.\s]?){3}\d{4}\b',
            "Time" : r'\b(?:[01]\d|2[0-3]):[0-5]\d\b',
            "HTML tags" : r'<[^>]+>',
            "Hash tags" : r'#\w+',
            "Currency amounts" : r'\$\d+(?:\.\d{2})?',
        }
    def mine_data(self, text: str):
        results = {}
        for label, pattern in self.regex_rubric.items():
            matches = re.findall(pattern, text)
            results[label] = matches
        return results
    def display_results(self, results): 
        print("Data Mining Results:")
        for label, matches in results.items():
            print(f"{label}:")
            if matches:
                for match in matches:
                    print(f"  - {match}")
            else:
                print("  No matches found.")
    def run(self):  
        results = self.mine_data(sample_text)
        self.display_results(results)
if __name__ == "__main__":
    datamine_instance = datamine()
    datamine_instance.run()
# Python script that defines a class for data mining using regular expressions.
