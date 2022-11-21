import logging

# likely a good idea to set up a default logger at the app
# level and import around as necessary

def simple_log():
    # using the built in logger is idea as it will format to a
    # nice standard and you can also set default log level to only
    # log at say warn or error
    logging.warning('Warning message')
    return