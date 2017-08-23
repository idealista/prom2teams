import os

from jinja2 import Environment, FileSystemLoader


DEFAULT_TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEMPLATE_NAME = 'template.j2'


def compose(template_path, msg_text):
    template = get_template(template_path)
    rendered_template = template.render(
        alert_status=msg_text['alert_status'],
        msg_text=msg_text)
    return rendered_template


def get_template(template_path):
    template_dir = DEFAULT_TEMPLATE_DIR
    template_name = DEFAULT_TEMPLATE_NAME

    if template_path:
        template_dir = os.path.dirname(template_path)
        template_name = os.path.basename(template_path)
    loader = FileSystemLoader(template_dir)
    environment = Environment(loader=loader, trim_blocks=True)
    template = environment.get_template(template_name)
    return template
