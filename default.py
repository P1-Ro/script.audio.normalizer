#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys

import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()


def get_settings():
    vol_down = addon.getSetting("vol_down")
    vol_amp = addon.getSetting("vol_amp")
    vol_old = addon.getSetting("vol_old")
    return vol_down, vol_amp, vol_old


def jsonrpc_command(method, params):
    data = {"jsonrpc": "2.0", "method": method, "id": 1, "params": params}
    string_data = json.dumps(data)
    result = xbmc.executeJSONRPC(string_data)
    print(result)
    return json.loads(result)


def save_old_volume():
    result = jsonrpc_command("Application.GetProperties", {"properties": ["volume"]})
    old_vol = result["result"]["volume"]
    addon.setSetting("vol_old", str(old_vol))
    pass


def normalization_on():
    volumes = get_settings()
    save_old_volume()
    jsonrpc_command("Application.SetVolume", {"volume": int(volumes[0])})
    for i in range(0, int(volumes[1])):
        jsonrpc_command("Input.ExecuteAction", {"action": "volampup"})

    addon.setSetting("normalization", "1")
    return "Success"


def normalization_off():
    volumes = get_settings()
    for i in range(0, int(volumes[1])):
        jsonrpc_command("Input.ExecuteAction", {"action": "volampdown"})
    jsonrpc_command("Application.SetVolume", {"volume": int(volumes[2])})

    addon.setSetting("normalization", "0")
    return "Success"


if len(sys.argv) == 2:

    param = str(sys.argv[1]).split("=")[1]
    normalization = addon.getSetting("normalization")

    if param == "on":
        if normalization == "" or normalization == "0":
            normalization_on()
    else:
        if normalization == "1":
            normalization_off()
