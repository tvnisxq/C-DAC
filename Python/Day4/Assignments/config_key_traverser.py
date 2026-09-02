def traverse_nested_config(config_dict, path_str, default=None):
    # An empty path gives us nothing to traverse, so return the fallback value
    if not path_str:
        return default

    # The traversal expects the starting configuration object to be a dictionart
    if type(config_dict) is not dict:
        return default


    try:
        # Current keeps track of our current key while navigating through the nested dictionary
        current = config_dict

        '''
        Convert a dot separated path such as:
        "server.ssl.cert_path" into ["server", "ssl", "cert_path"],
        then traverse one key at a time
        '''
        for key in path_str.split("."):
            '''
            Directly attempt to access the next key instead of checking 
            whether it exists beforehand.Any invalid lookup is handled
            by the exception block below.
            '''
            current = current[key]

        # If every key was successfully traversed return the final value
        return current

    # KeyError: A key in the path doesn't exist
    # TypeError: Attempting dictionary-style indexing on a primitive value
    # AttributeError: handles invalid attribute/indexing operations if encountered
    except(KeyError, TypeError, AttributeError):
        return default

config = {
"server": {
    "host": "127.0.0.1",
    "port": 8080,
    "ssl": {
        "enabled": True,    
        "cert_path": "/etc/ssl/certs"
    }
},
"database": "postgresql://localhost:5432"
}

# Test Case 1: Valid Path
print(traverse_nested_config(config, "server.ssl.cert_path"))

# Test Case 2: Missing Key (Triggers KeyError)
print(traverse_nested_config(config, "server.database.username", "guest"))

# Test Case 3: Indexing Non-Dictionary value (Triggers TypeError)
# Here config["database"] is a string, which cannot be indexed with "host"
print(traverse_nested_config(config, "database.host", "localhost"))