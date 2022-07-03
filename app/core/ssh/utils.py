import yaml
SSH_CONFIG_PATH = "app/config/ssh.config.yml"


def get_ssh_config():
    """Get ssh settings from config.yml"""
    with open(SSH_CONFIG_PATH, encoding='utf-8') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return False
