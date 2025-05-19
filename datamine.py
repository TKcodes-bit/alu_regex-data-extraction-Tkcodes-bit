#!/usr/bin/env python3
#Import re

import re

class datamine:
    def__init__(self):
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