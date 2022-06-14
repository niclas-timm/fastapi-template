import yaml
SSH_CONFIG_PATH = "app/config/ssh.config.yml"


def get_ssh_config():
    with open(SSH_CONFIG_PATH) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return False
