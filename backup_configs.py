import os
from datetime import datetime
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

def backup_config(task: Task) -> Result:
    result = task.run(task=netmiko_send_command, command_string="show running-config")
    backup_directory = "backups"
    
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    backup_filename = os.path.join(backup_directory, f"{task.host.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    with open(backup_filename, 'w') as backup_file:
        backup_file.write(result.result)
    
    return Result(host=task.host, result=f"Yedek {backup_filename} olarak kaydedildi")

nr = InitNornir(config_file="config.yaml")

result = nr.run(task=backup_config)
print_result(result)
