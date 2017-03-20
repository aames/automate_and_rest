import json
import jinja2
import uuid
import redis

"""
utils.py
--------

Description:
A set of general utilities that are likely to be used throughout tests.

"""

# Assuming you're using the docker-compose provided redis instance...
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'


def merge_headers(defaults, custom):
    """
    Take two dictionaries and merge defaults with custom values;
        custom will take precedence if there are any duplicates.
    :param defaults:       is a dictionary of headers
    :param custom:         is a dictionary of headers
    :return:               merged dictionary where custom takes precedence
    """
    merged = defaults.copy()
    merged.update(custom)
    return merged


def json_file_to_string(file_path_name):
    """
    Convert a the contents of a file that contains a JSON object to a plain old
        string, that can then be interpreted as a JSON object in a request or assertion.
    :param file_path_name:     is the fully qualified path to the file, including its extension
    :return:                   a String of JSON
    """
    with open(file_path_name, 'r') as json_file:
        json_data = json.load(json_file)
    return json.dumps(json_data)


def replace_json_tags(template_file_path, output_file_path, template_name, dict_of_variables):
    """
    Replace JSON Tags in a given template file and output a JSON object in a flat file.
    :param  template_file_path:     The directory in which to look for template files (full path with trailing /).
    :param  output_file_path:       The directory in which to place converted JSON files (full path with trailing /).
    :param  template_name:          The name of the template file to look for and the name of the output file.
    :param  dict_of_variables:      The name of the dictionary containing JSON key:values that should be rendered
                                        at runtime to build the JSON file.
    :return:                        True if the file write is successful, False if the file cannot be written.
    """
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=template_file_path))
    template = environment.get_template(template_name + ".jt")
    json_as_string = template.render(dict_of_variables)
    try:
        with open(output_file_path + template_name + ".json", 'w') as output_file:
            output_file.write(json_as_string)
    except OSError as e:
        return False
    return True


def get_uuid():
    """
    Get a UUID to use in a random variable or some such method.
    :return:        A (pseudo random) type-4 UUID that has had its hyphens removed
    """
    return str(uuid.uuid4()).replace("-", "")


def get_transient_variable(identifier):
    """
    Get a variable out of the transient data store (Redis or similar)

    :param identifier:      The key to retrieve.
    :return:                A String representing the value or 'None' if no key exists.
    """
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    return str(r.get(identifier))


def set_transient_variable(identifier, value):
    """
    Set a variable in the transient data store.

    :param identifier:      The key to set in the transient data store.
    :param value:           The value to set to the key in the transient data store.
    :return:                True if successful, 'None' if not.
    """
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    return str(r.set(identifier, value))
