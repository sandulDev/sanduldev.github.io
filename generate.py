import os

import yaml
from jinja2 import Environment, FileSystemLoader


def load_config():
    with open('config.yml', 'r') as file:
        return yaml.safe_load(file)

def generate_site(config):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    output = template.render(profile=config['profile'], links=config['links'])

    os.makedirs('build', exist_ok=True)

    with open('build/index.html', 'w') as file:
        file.write(output)

    os.makedirs('build/static', exist_ok=True)

    for root, dirs, files in os.walk('static'):
        relative_path = os.path.relpath(root, 'static')
        build_path = os.path.join('build/static', relative_path)

        os.makedirs(build_path, exist_ok=True)

        for file_name in files:
            src = os.path.join(root, file_name)
            dest = os.path.join(build_path, file_name)

            with open(src, 'rb') as f_src:
                with open(dest, 'wb') as f_dest:
                    f_dest.write(f_src.read())

if __name__ == "__main__":
    config = load_config()
    generate_site(config)