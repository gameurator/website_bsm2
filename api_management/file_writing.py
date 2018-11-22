import json
import xml.etree.ElementTree as ET
from os import path, makedirs
from re import sub
from typing import Union

import requests
from webob.multidict import MultiDict


def read_json_file(file_path: str, file_name: str):
    """write a json file
    :param file_path: data_path where to write as string. The data_path must exist, it must end by backslashes
    :param file_name: name of file as string
    :param data: the data to be written
    """
    full_name = file_path + file_name + '.json'  # path and name of file to be read
    return json.load(open(full_name))  # to print the json file in a clean way with an indent of 4


def write_to_json_file(file_path: str, file_name: str, data: str):
    """write a json file
    :param file_path: data_path where to write as string. The data_path must exist, it must end by backslashes
    :param file_name: name of file as string
    :param data: the data to be written
    """
    full_name = file_path + file_name + '.json'
    with open(full_name, 'w') as fp:
        json.dump(data, fp, indent=4)  # to print the json file in a clean way with an indent of 4


def write_to_xml_file(file_path: str, file_name: str, data: str):
    """write a XML file
    :param file_path: data_path where to write as string. The data_path must exist, it must end by backslashes
    :param file_name: name of file as string
    :param data: the data to be written    """
    tree = ET.ElementTree(ET.fromstring(data))
    tree.write(file_path + file_name + ".xml")


def write_request(request: requests.Response, params: Union[dict, MultiDict], file_name: str, path_to_write: str):
    """
    from a request, using its parameters (in the SLV format), a file name and a path_for_data, writes the output document in the
    appropriate format.
    :param request: input request from which we want to write the file
    :param params: the parameters of the request
    :param file_name: name of the file to be created
    :param path_to_write: where to write the file
    """
    file_name = sub(r'[\\/:"*?<>|]+', "", file_name)  # rename the file to delete all forbidden caracters
    if not path.isdir(path_to_write):  # if the data_path does not exist
        makedirs(path_to_write)  # create it
    if params['ser'] == 'json':  # if it's a json request write the json file
        write_to_json_file(path_to_write, file_name, request.json())
    elif params['ser'] == 'xml':  # if it's an xml request write an xml file
        write_to_xml_file(path_to_write, file_name, request.text)
