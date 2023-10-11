import subprocess



def create_docker(parameters):
    text=["docker", "run"]
    environment=parameters["envs"]
    if environment:
        for env in environment:
            text.append("-e")
            text.append(f"{env}={environment[env]}")

    text.append(parameters["image"])
    if parameters["command"]:
        text.append(parameters["command"])
    
    shell_result=subprocess.run(text,capture_output=True,text=True)
    return{"message":shell_result.stdout,
            "error":shell_result.stderr}


def docker_app_lists():
    result=subprocess.run(["docker","images"],capture_output=True,text=True)
    images_info=result.stdout.split("\n")
    result=[]
    
    for info in images_info[1:]:
        items=info.split("  ")
        filtered_list = [item for item in items if item != '']
        if filtered_list:
            result.append({
                        "REPOSITORY":filtered_list[0],
                        "TAG":filtered_list[1],
                        "IMAGE_ID":filtered_list[2],
                        "CREATED":filtered_list[3],
                        "SIZE":filtered_list[4]
                        })
    return result

def docker_single_app_info(repository):

    result=subprocess.run(["docker","images",repository],capture_output=True,text=True)
    images_info=result.stdout.split("\n")
    try:
        items=images_info[1].split("  ")
        filtered_list = [item for item in items if item != '']
        if filtered_list is not None:
            return ({
                        "REPOSITORY":filtered_list[0],
                        "TAG":filtered_list[1],
                        "IMAGE_ID":filtered_list[2],
                        "CREATED":filtered_list[3],
                        "SIZE":filtered_list[4]
                        })
    except:
        return({"message":"image with this repository is not found "})


def delete_docker_app(repository):
    shell_result=subprocess.run(["docker","rmi","-f",repository],capture_output=True,text=True) 
    
    if shell_result.stderr =="" :
        
        delete_info=shell_result.stdout.split("\n")
        result=[]
        for info in delete_info[:-1]:
            item=info.split(": ")
            if item  :
                
                result.append({item[0]:item[1]})
        return(result)
    
    else:
        
        return{"message":shell_result.stderr}
    
    # for info in delete_info:


# param={
# "name": "my-app",
# "image": "hello-world",
# "envs": {},
# "command": ""
# }
# create_docker_app(parameters=param)



