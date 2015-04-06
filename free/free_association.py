'''
Created on Oct 8, 2014

A class for accessing The University of South Florida Free Association
http://w3.usf.edu/FreeAssociation/

@author: teon
'''


import os
import os.path as op
import inspect


fields = {
    
    'CUE':	'Normed Word',
    'TARGET':	'Response to Normed Word',
    'NORMED?':	'Is Response Normed?',
    '#G':	'Group size',
    '#P':	'Number of Participants Producing Response',
    'FSG':	'Forward Cue-to-Target Strength',
    'BSG':	'Backward Target-to-Cue Strength',
    'MSG':	'Mediated Strength',
    'OSG':	'Overlapping Associate Strength',
    '#M':	'Number of Mediators',
    'MMIA':	'Number of Non-Normed Potential Mediating Associates',
    '#O':	'Number of Overlapping Associates',
    'OMIA':	'Number of Non-Normed Overlapping Associates',
    'QSS':	'Cue: Set Size',
    'QFR':	'Cue: Frequency',
    'QCON':	'Cue: Concreteness',
    'QH':	'Cue is a Homograph?',
    'QPS':	'Cue: Part of Speech',
    'QMC':	'Cue: Mean Connectivity Among Its Associates',
    'QPR':	'Cue: Probability of a Resonant Connection',
    'QRSG':	'Cue: Resonant Strength',
    'QUC':	'Cue: Use Code',
    'TSS':	'Target: Set Size',
    'TFR':	'Target: Frequency',
    'TCON':	'Target: Concreteness',
    'TH':	'Target is a Homograph?',
    'TPS':	'Target: Part of Speech',
    'TMC':	'Target: Mean Connectivity Among Its Associates',
    'TPR':	'Target: Probability of a Resonant Connection',
    'TRSG':	'Target: Resonant Strength',
    'TUC':	'Target: Use Code'
}


class Free(dict):

    def __init__(self):
        with open('free_association.txt') as f:
            self.fields = [x.strip() for x in f.readline().split(',')]
            db = [dict(zip(self.fields, [y.strip() for y in x.split(',')]))
                  for x in f.readlines()]
        self._free = db
        self.cues = set([x['CUE'].lower() for x in db])

    def __getitem__(self, word):
        return [x for x in self._free if x['CUE'] == word.upper()]
        
    def field_lookup(self, field):
        return fields[field]
    
    # def info(self, word):
    #     if word in self.cues:
    #         idx = self.cues.index(word.upper())
    #     else:
    #         raise ValueError("'%s' not found. :( " %word)
    #     return self._free[idx]
