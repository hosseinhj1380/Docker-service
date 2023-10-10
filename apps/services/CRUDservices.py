import subprocess



def create_docker_app(parameters):
    pass

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




