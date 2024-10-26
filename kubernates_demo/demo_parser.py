import yaml
import pprint


with open("demo.yaml", "r") as yaml_parser:
    try:
        data = yaml.safe_load(yaml_parser)
        pprint.pprint(data)
    except yaml.YAMLError as exc:
        print(exc)


# Get the employee name
name = data[0]["Employee_Details"]["Employee"]["Name"]

print(name)
