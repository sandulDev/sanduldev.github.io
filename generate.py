from jinja2 import Environment, FileSystemLoader
import yaml
import os


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
    for image in os.listdir('static'):
        src = os.path.join('static', image)
        dest = os.path.join('build/static', image)
        with open(src, 'rb') as f_src:
            with open(dest, 'wb') as f_dest:
                f_dest.write(f_src.read())


if __name__ == "__main__":
    config = load_config()
    generate_site(config)