import os

from jinja2 import Environment, FileSystemLoader


DEFAULT_TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEMPLATE_NAME = 'template.j2'


def compose_all(template_path, alarms_json):
    template = get_template(template_path)
    rendered_templates = [template.render(status=json_alarm['status'], msg_text=json_alarm)
                          for json_alarm in alarms_json]
    return rendered_templates


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
