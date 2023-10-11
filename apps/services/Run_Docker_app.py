import subprocess

def run_docker(parameters):
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

    running_result=subprocess.run(["docker","ps",f"--filter=ancestor={parameters['image']}"],capture_output=True,text=True)
    images_info=running_result.stdout.split("\n")
    try:
        items=images_info[1].split("  ")
        filtered_list = [item for item in items if item != '']
        if filtered_list is not None:
            if "Up" in filtered_list[4]:
                status="Running"
    except:
        status="Finished"

    return{"message":shell_result.stdout,
            "error":shell_result.stderr,
            "parameters":text,
            "status":status
            }


print(run_docker(parameters={
"name": "my-app",
"image": "hello-world",
"envs": {"key1": "val1","key2": "val2"},
"command": "sleep 1000"
}))

