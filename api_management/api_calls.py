# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 08:42:49 2018

@author: A.DECOUDENHOVE
This script's goal is to get raw data from SLV API and write it in json format in the appropriate sub-files.
It can be easily modified but it's final purpose is to get switch on/off times each day for each controller and
the power consumption associated. These data are in .json format.

It is possible to make it extract data in xml format but it will no longer be able to process the data to the next step.

All files will be created in the sub-directory "data". they will be name according to their parameters and the name of
the function called in SLV API.
"""

from typing import Union, Tuple

import requests
from webob.multidict import MultiDict
from datetime import datetime
from os import path
from re import sub
from sys import argv
from raw_extractions.models import SubDevice

from .file_writing import write_request, read_json_file, write_to_json_file


def call_SLV_getAllControllers(url: str, authentication: tuple, format: str,
                               write_file_to: str = "") -> Union[Tuple[requests.request, str], requests.request]:
    """Call SLV with function 'getAllControllers'. Return obtained data in the demanded format
    :param url: the URL of the website
    :param authentication: tuple giving ('identifier','password')
    :param format: write 'json' if you want a json request or 'xml' if you want an XML request
    :param write_file_to: if you want a file to be written, write its path
    :return: the raw request from StreetLight Vision server
    :rtype: requests """
    api_method = 'getAllControllers'  # function which gets called on SLV server
    api_part = '/api/asset/'  # where the function is on SLV server
    # setting up parameters
    param = MultiDict([('ser', format)])
    # checking format input
    if not (
            format == 'json' or format == 'xml'):  # if format argument does not match expected input raises an error
        raise ValueError(
            "wrong input parameters for APIFinal.call_SLV_getAllControllers function : format must be either 'xml' or 'json' \n")
    print('calling ' + api_method + '...')
    r = requests.get(url + api_part + api_method, params=param, auth=authentication)  # call the request
    if write_file_to == "":  # if asked, writes file
        file_name = api_method  # the output file name if write_file is true
        write_request(r, param, write_file_to)
        return r, file_name
    return r


def call_SLV_searchGeozones(url: str, authentication: tuple, format: str, name: str, partialMatch: bool,
                            write_file_to: str = "") -> Union[Tuple[requests.request, str], requests.request]:
    """Call SLV with function 'searchGeozones'. Return obtained data in the demanded format
    :param url: the URL of the website
    :param authentication: tuple giving ('identifier','password')
    :param format: write 'json' if you want a json request or 'xml' if you want an XML request
    :param name: string name of the geoZone to work on
    :param partialMatch: boolean indicating if you want the name to match partially or fully
    :param write_file_to: if you want a file to be written, write its path
    :return: the raw request from StreetLight Vision server
    :rtype: requests """
    api_method = 'searchGeozones'  # function which gets called on SLV server
    api_part = '/api/asset/'  # where the function is on SLV server
    # setting up parameters
    param = MultiDict([('name', name), ('partialMatch', partialMatch), ('ser', format)])
    # checking format input
    if not (
            format == 'json' or format == 'xml'):  # if format argument does not match expected input raises an error
        raise ValueError(
            "wrong input parameters for APIFinal.call_SLV_getAllControllers function : format must be either 'xml' or 'json' \n")
    print('calling ' + api_method + '...')
    r = requests.get(url + api_part + api_method, params=param, auth=authentication)  # call the request
    if write_file_to:  # if asked, writes file
        file_name = api_method  # the output file name if write_file is true
        write_request(r, param, write_file_to)
        return r, file_name
    return r


def call_SLV_getGeozoneChildrenGeozones(url: str, authentication: tuple, format: str, geozoneId: int,
                                        computeHierarchyInfos: bool,
                                        write_file_to: str = "") -> Union[
    Tuple[requests.request, str], requests.request]:
    """Call SLV with function 'searchGeozones'. Return obtained data in the demanded format
    :param url: the URL of the website
    :param authentication: tuple giving ('identifier','password')
    :param format: write 'json' if you want a json request or 'xml' if you want an XML request
    :param geozoneId: give the ID of the geoZone of interest
    :param computeHierarchyInfos: make a tree of sub-zones.
    :param write_file_to: if you want a file to be written, write its path
    :return: the raw request from StreetLight Vision server
    :rtype: requests """
    api_method = 'getGeozoneChildrenGeozones'  # function which gets called on SLV server
    api_part = '/api/asset/'  # where the function is on SLV server
    # setting up parameters
    param = MultiDict([('geozoneId', geozoneId), ('computeHierarchyInfos', computeHierarchyInfos), ('ser', format)])
    # checking format input
    if not (
            format == 'json' or format == 'xml'):  # if format argument does not match expected input raises an error
        raise ValueError(
            "wrong input parameters for APIFinal.call_SLV_getAllControllers function : format must be either 'xml' or 'json' \n")
    print('calling ' + api_method + '...')
    r = requests.get(url + api_part + api_method, params=param, auth=authentication)  # call the request
    if write_file_to:  # if asked, writes file
        file_name = api_method  # the output file name if write_file is true
        write_request(r, param, file_name)
        return r, file_name
    return r


def call_SLV_getDeviceValueDescriptors(url: str, authentication: tuple, format: str, controllerStrId: str,
                                       idOnController: str, write_file_to: str = "") -> Union[
    Tuple[requests.request, str], requests.request]:
    """Call SLV with function 'searchGeozones'. Return obtained data in the demanded format
    :param url: the URL of the website
    :param authentication: tuple giving ('identifier','password')
    :param format: write 'json' if you want a json request or 'xml' if you want an XML request
    :param controllerStrId: controllerStrId as defined in SLV
    :param idOnController: idOnController as defined in SLV
    :param write_file_to: if you want a file to be written, write its path
    :return: the raw request from StreetLight Vision server
    :rtype: requests """
    api_method = 'getDeviceValueDescriptors'  # function which gets called on SLV server
    api_part = '/api/logging/'  # where the function is on SLV server
    # setting up parameters
    param = {'controllerStrId': controllerStrId, 'idOnController': idOnController, 'ser': format, 'time': 1540309949856}
    # checking format input
    if not (
            format == 'json' or format == 'xml'):  # if format argument does not match expected input raises an error
        raise ValueError(
            "wrong input parameters for APIFinal.call_SLV_getAllControllers function : format must be either 'xml' or 'json' \n")
    print('calling ' + api_method + '...')
    r = requests.get(url + api_part + api_method, params=param, auth=authentication)  # call the request
    if write_file_to:  # if asked, writes file
        file_name = api_method  # the output file name if write_file is true
        write_request(r, param, file_name)
        return r, file_name
    return r


def call_SLV_getControllerDevices(url: str, authentication: tuple, format: str, controllerStrId: Union[str, list],
                                  write_file_to: str = "") -> Union[Tuple[requests.request, str], requests.request]:
    """Call SLV with function 'getAllControllers'. Return obtained data in the demanded format
    :param url: the URL of the website
    :param authentication: tuple giving ('identifier','password')
    :param format: write 'json' if you want a json request or 'xml' if you want an XML request
    :param controllerStrId: the controllerStrId str matching the right name
    :param write_file_to: if you want a file to be written, write its path
    :return: the raw request from StreetLight Vision server
    :rtype: requests """
    api_method = 'getControllerDevices'  # function which gets called on SLV server
    api_part = '/api/asset/'  # where the function is on SLV server
    # setting up parameters
    param = MultiDict([('ser', format), ('controllerStrId', controllerStrId)])
    # checking format input
    if not (
            format == 'json' or format == 'xml'):  # if format argument does not match expected input raises an error
        raise ValueError(
            "wrong input parameters for APIFinal.call_SLV_getAllControllers function : format must be either 'xml' or 'json' \n")
    print('calling ' + api_method + ' ' + controllerStrId + '...')
    r = requests.get(url + api_part + api_method, params=param, auth=authentication)  # call the request
    if write_file_to:  # if asked, writes file
        if type(controllerStrId) is list:
            file_name = api_method  # the output file name if write_file is true and controllerStrId is a list
        else:
            file_name = api_method + param['controllerStrId']  # the output file name if write_file is true
        write_request(r, param, file_name)
        return r, file_name
    return r


def call_SLV_getDevicesLogValues(url: str, authentication: tuple, format: str, deviceId: Union[int, list],
                                 name: Union[str, list], from_date: str, to_date: str,
                                 write_file_to: str = "") -> Union[Tuple[requests.request, str], requests.request]:
    """
    Call SLV with function 'getDevicesLogValues'. Return obtained data in the demanded format
    :param url: the URL of the website
    :param authentication: tuple giving ('identifier','password')
    :param format: write 'json' if you want a json request or 'xml' if you want an XML request
    :param deviceId: string or list of string exactly equal to the device IDs in SLV server
    :param name: name or list of names of the values you want to get. Type 'TotalKWHPositive' to retrieve the index
    :param from_date: in the following format : dd/mm/yyyy hh:mm:ss
    :param to_date: in the following format : dd/mm/yyyy hh:mm:ss
    :param write_file_to: if you want a file to be written, write its path
    :return: the request
    """
    api_method = 'getDevicesLogValues'  # function which gets called on SLV server
    api_part = '/api/logging/'  # where the function is on SLV server
    # setting up parameters
    param = MultiDict([('ser', format), ('from', from_date), ('to', to_date)])
    param = add_to_parameters('deviceId', deviceId, param)
    param = add_to_parameters('name', name, param, 1)
    # checking format input
    if not (
            format == 'json' or format == 'xml'):  # if format argument does not match expected input raises an error
        raise ValueError(
            "wrong input parameters for APIFinal.call_SLV_getAllControllers function : format must be either 'xml' or 'json' \n")
    print('calling ' + api_method + '...')
    r = requests.post(url + api_part + api_method, data=param,
                      auth=authentication)  # post the request because there are several sub calls
    if write_file_to != "":  # if asked, writes file
        if type(deviceId) is list and type(name) is list:
            file_name = api_method  # the output file name if write_file is true and deviceId is a list
        elif type(name) is list:
            file_name = api_method + "_" + param[
                'deviceId']  # the output file name if write_file is true and name is a list
        elif type(deviceId) is list:
            file_name = api_method + "_" + param[
                'name']  # the output file name if write_file is true and deviceId and name are lists
        else:
            file_name = api_method + "_" + param['deviceId'] + "_" + param[
                'name']  # the output file name if write_file is true
        file_name = file_name + "_" + param['from'] + "_" + param['to']
        write_request(r, param, file_name)
        return r, file_name
    return r


def add_to_parameters(key: object, values: Union[list, object], multidictio: MultiDict, length: int = 1) -> MultiDict:
    """
    this function add a parameter to the parameter multidict for SLV API calls

    :param key: name of the parameter as str
    :param values: value or values corresponding to that parameter. If multiple values format must be a list
    :param multidictio: the parameter multidict
    :param length: number of parameters
    :return: the output parameter multidict
    """
    if type(values) is list:  # checking input types
        for elt in values:  # add several deviceId to param
            multidictio.add(key, elt)
    elif type(values):  # checking input types
        for i in range(0, length):
            multidictio.add(key, values)  # add only one deviceId to param
    return multidictio


def getAllControlers_request_to_data(r: requests.request) -> Tuple[list, list, list]:
    """
    Transform the input request, from getAllControllers function of SLV API to lists of interesting data for main script
    :param r: request from getAllControllers request.
    :return: a tuple of the lists of all controllers, all controllers ID and all geozones id.
    :rtype: tuple
    """
    output_json = r.json()  # get the data out of the request
    AllControllers = []  # initialize list of all controllers name
    ControllersID = []  # initialize list of all controllers ID
    GeoZoneId = []  # initialize list of all geo zones ID
    for elt in output_json:  # for each element in the data, add the appropriate element at the end of each list
        AllControllers.append(elt['controllerDevice']['controllerStrId'])
        ControllersID.append(elt['controllerDevice']['id'])
        GeoZoneId.append(elt['controllerDevice']['geoZoneId'])
    return AllControllers, ControllersID, GeoZoneId


def getControllerDevices_request_to_data(r: requests.request) -> Tuple[list, list]:
    """
    From the controllers list to read, with SLV url and authentication, return a list of electric meters and their IDs
    in a tuple of the 2 lists.
    :param r: request from getControllerDevices
    :return: returns a tuple of two list containing the ElectricCounter names and their respective IDs.
    """
    output_json = r.json()  # get the json out of the request
    for controller in output_json:
        if controller['categoryStrId'] == 'electricalCounter':  # all_counters_category =
            electric_counter_ID = controller['id']  # find the electriccounter id
            electric_counter_str = controller['controllerStrId']  # find the electriccounter strId
    return electric_counter_str, electric_counter_ID  # , all_counters_category


def historize_log_values(write_file_to: str, values: str):
    """
    hitorize all data for the given log value name on the given file which will end by history instead of its dates
    :param write_file_to: the path where to write the file
    :param filename:
    :param file_name_log_values: read the request file
    """
    if path.isfile(write_file_to ):
        historic = read_json_file(write_file_to)
        historic += values
        unique = []
        [unique.append(elem) for elem in historic if elem not in unique]
        unique.sort(key=lambda event: datetime.strptime(event["eventTime"], "%Y-%m-%d %H:%M:%S"))
        write_to_json_file(write_file_to, unique)
    else:
        write_to_json_file(write_file_to, values)

# def update_values_for_device(write_file_to: str, sub_device: SubDevice):
#     """
#     script which write requests return values (DigitalOutput1 and TotalKWHPositive) to json format
#     """
#
#     global error_stream  # initilize a string so that all errors will be written on that stream
#     error_stream = ""
#
#     (start_date, end_date, historization) = get_info_from_user()
#
#     request_all_controllers, file_name_control = call_SLV_getAllControllers(SLV_URL, logi, 'json',
#                                                                             True)
#     AllControllers, ControllersID, GeoZoneId = getAllControlers_request_to_data(
#         request_all_controllers)  # recover interesting data from previous request
#     ElectricCounters = []  # initialize list to save all ElectricCounters
#     ElectricCounterIDs = []  # initialize list to save all electric counters id
#     for controller in AllControllers:  # for each controllers
#         # demand to SLV Server the list of devices which parent is controller
#         request_controller_devices, file_name_devices = call_SLV_getControllerDevices(SLV_URL, logi, 'json', controller,
#                                                                                       True)
#         try:
#             electric_counter_str, electric_counter_ID = getControllerDevices_request_to_data(
#                 request_controller_devices)  # isolate the electric counters
#             ElectricCounters.append(electric_counter_str)  # add to the saving list
#             ElectricCounterIDs.append(electric_counter_ID)  # add to the saving list
#         except UnboundLocalError as error_caught:  # if no electric counters were found, write the error
#             error_stream += "No electric devices could be found for {}. {}\n".format(controller, error_caught)
#     # demand all KWH log values between given dates
#     request_log_values, file_name_log_KWH = call_SLV_getDevicesLogValues(SLV_URL, logi, 'json', ElectricCounterIDs,
#                                                                          'TotalKWHPositive',
#                                                                          start_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                          end_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                          True)
#     if historization:
#         try:
#             historize_log_values(file_name_log_KWH)
#         except ValueError as error_caught:
#             error_stream += "Make sure that the code parameters are on json. Historize does not work on xml format.{}".format(
#                 error_caught)
#     # demand all on/off log values between given dates
#     request_onoff_values, file_name_log_Op1 = call_SLV_getDevicesLogValues(SLV_URL, logi, 'json', ControllersID,
#                                                                            'DigitalOutput1',
#                                                                            start_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                            end_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                            True)
#     if historization:
#         try:
#             historize_log_values(file_name_log_Op1)
#         except ValueError as error_caught:
#             error_stream += "Make sure that the code parameters are on json. Historize does not work on xml format.{}".format(
#                 error_caught)
#
#     error_file = open('errors//APIFinal_errors.txt', 'w')  # open in read mode the file were to write all errors
#     error_file.write(error_stream)  # write the errors
#     error_file.close()  # close the file

# def get_index_and_onoff_values():
#     """
#     script which write requests return values (DigitalOutput1 and TotalKWHPositive) to json format
#     """
#
#     global error_stream  # initilize a string so that all errors will be written on that stream
#     error_stream = ""
#
#     (start_date, end_date, historization) = get_info_from_user()
#
#     request_all_controllers, file_name_control = call_SLV_getAllControllers(SLV_URL, logi, 'json',
#                                                                             True)
#     AllControllers, ControllersID, GeoZoneId = getAllControlers_request_to_data(
#         request_all_controllers)  # recover interesting data from previous request
#     ElectricCounters = []  # initialize list to save all ElectricCounters
#     ElectricCounterIDs = []  # initialize list to save all electric counters id
#     for controller in AllControllers:  # for each controllers
#         # demand to SLV Server the list of devices which parent is controller
#         request_controller_devices, file_name_devices = call_SLV_getControllerDevices(SLV_URL, logi, 'json', controller,
#                                                                                       True)
#         try:
#             electric_counter_str, electric_counter_ID = getControllerDevices_request_to_data(
#                 request_controller_devices)  # isolate the electric counters
#             ElectricCounters.append(electric_counter_str)  # add to the saving list
#             ElectricCounterIDs.append(electric_counter_ID)  # add to the saving list
#         except UnboundLocalError as error_caught:  # if no electric counters were found, write the error
#             error_stream += "No electric devices could be found for {}. {}\n".format(controller, error_caught)
#     # demand all KWH log values between given dates
#     request_log_values, file_name_log_KWH = call_SLV_getDevicesLogValues(SLV_URL, logi, 'json', ElectricCounterIDs,
#                                                                          'TotalKWHPositive',
#                                                                          start_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                          end_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                          True)
#     if historization:
#         try:
#             historize_log_values(file_name_log_KWH)
#         except ValueError as error_caught:
#             error_stream += "Make sure that the code parameters are on json. Historize does not work on xml format.{}".format(
#                 error_caught)
#     # demand all on/off log values between given dates
#     request_onoff_values, file_name_log_Op1 = call_SLV_getDevicesLogValues(SLV_URL, logi, 'json', ControllersID,
#                                                                            'DigitalOutput1',
#                                                                            start_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                            end_date.strftime("%d/%m/%Y %H:%M:%S"),
#                                                                            True)
#     if historization:
#         try:
#             historize_log_values(file_name_log_Op1)
#         except ValueError as error_caught:
#             error_stream += "Make sure that the code parameters are on json. Historize does not work on xml format.{}".format(
#                 error_caught)
#
#     error_file = open('errors//APIFinal_errors.txt', 'w')  # open in read mode the file were to write all errors
#     error_file.write(error_stream)  # write the errors
#     error_file.close()  # close the file


# get_index_and_onoff_values()  # calls the script main function
# # call_SLV_getDeviceValueDescriptors(SLV_URL, logi, 'xml', 'CBC_BSM_A03', 'Mesure_BSM_A03', True)
# # call_SLV_getGeozoneChildrenGeozones(SLV_URL, logi, 'json', 3462, False, True)
