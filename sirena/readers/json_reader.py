# Copyright (c) 2020 SMHI, Swedish Meteorological and Hydrological Institute 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2020-04-07 15:41

@author: a002028

"""
import json
import numpy as np
from sirena import utils


class JSONreader(dict):
    """
    - Import json
    - Export to json
    - Find dictionary within json file based on a specific key
    - Add elements to dictionary
    - Fill up json/dictionary structure with relevant/desired information
    """
    def _export_json(self, data_dict=None, out_source='', indent=4):
        """ """
        with open(out_source, "w") as outfile:
            json.dump(
                data_dict,
                outfile,
                indent=indent
            )

    def _initiate_attributes(self):
        """ """
        pass

    def _initiate_outfile(self):
        """ json files can save multiple dictionaries stored in a list
        """
        self.out_file = []

    def _get_dictionary_reference(self, dictionary=None, dict_path=None):
        """"""
        if not dictionary:
            dictionary = {}
        for key in dict_path:
            if isinstance(key, str) and key not in dictionary:
                return None
            dictionary = dictionary[key]
        return dictionary

    def export(self, out_source='', out_file=None):
        """ """

        if out_file:
            self._export_json(out_source=out_source, data_dict=out_file)

        elif hasattr(self, 'out_file'):
            self._export_json(out_source=out_source, data_dict=self.out_file)

        elif hasattr(self, 'config'):
            self._export_json(out_source=out_source, data_dict=self.config)

        else:
            raise UserWarning('No outfile specified for export to .json')

    def load_json(self, config_files=[], return_dict=False):
        """ array will be either a list of dictionaries or one single dictionary
            depending on what the json file includes
        """
        if not isinstance(config_files, (list, np.ndarray)):
            config_files = [config_files]

        for config_file in config_files:
            with open(config_file, 'r') as fd:
                self = utils.recursive_dict_update(self, json.load(fd))

        if return_dict:
            return self
