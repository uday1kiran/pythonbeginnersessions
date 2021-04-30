#pip install pyyaml
import yaml

def yaml_loader(filepath):
    with open(filepath,'r')as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath,data):
    with open(filepath,"w") as file_descriptor:
        yaml.dump(data, file_descriptor)


if __name__ == "__main__":
    file_path1 = "configmap-safety-stock-streamer.yaml"
    data1 = yaml_loader(file_path1)
    file_path2 = "inner.yaml"
    data2 = yaml_loader(file_path2)
    data1['data']['application.yml'] = data2
    print(data1)
    yaml_dump("final.yml",data1)

