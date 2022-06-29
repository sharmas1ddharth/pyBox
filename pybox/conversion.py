import json
import yaml
import os


def json_to_yaml(file, name=None):
    # load json data
    with open('a.json') as f:
        data = f.read()
        json_data = json.loads(data)
        # convert unicode to string
        converted_json_data = json.dumps(json_data)

    # output yaml
    if name == None:
        name_, _ = os.path.splitext(file)
        yaml_data = open(f"{name_}.yaml", 'w')
        yaml_data.write(yaml.dump(yaml.safe_load(converted_json_data), default_flow_style=False))
        yaml_data.close()

    elif name != None:
        name_, _ = os.path.splitext(name)
        yaml_data = open(f"{name_}.yaml", 'w')
        yaml_data.write(yaml.dump(yaml.safe_load(converted_json_data), default_flow_style=False))
        yaml_data.close()
