# Kodi audio normalizer
Scripts that when turned on normalizes volume of current playing content.
Great for watching movies at night.

## Usage:
If normalization should be used is based on  `"state" : "off"` or  `"state" : "on"`

### From [Yatse](https://play.google.com/store/apps/details?id=org.leetzone.android.yatsewidgetfree&hl=en)

1. Add JSONRPC command
2. Set name to `Normalization ON`
3. Set JSON-RPC "method" to `Addons.ExecuteAddon`
4. Set JSON-RPC "params" to `{"addoni":"script.audio.normalizer", "params":{"state": "on"}}`
5. Repeat same procedure with `"state" : "off"`


### Sending JSON

Send following json to `kodiUrl/jsonrpc`

    {
        "jsonrpc": "2.0",
        "method": "Addons.ExecuteAddon",
        "params": {
            "addonid" : "script.audio.normalizer",
            "params": {
                "state" : "off"
            }
        },
        "id": 1
    }