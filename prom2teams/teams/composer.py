import logging
import os

from jinja2 import Environment, FileSystemLoader

from prom2teams import root
from prom2teams.app.exceptions import MissingTemplatePathException


log = logging.getLogger('prom2teams')


class _Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class TemplateComposer(metaclass=_Singleton):

    DEFAULT_TEMPLATE_PATH = os.path.abspath(os.path.join(root, 'resources/templates/teams.j2'))

    def __init__(self, template_path=DEFAULT_TEMPLATE_PATH):
        log.info(template_path)
        if not os.path.isfile(template_path):
            raise MissingTemplatePathException('Template {} not exists'.format(template_path))

        template_dir = os.path.dirname(template_path)
        template_name = os.path.basename(template_path)
        loader = FileSystemLoader(template_dir)
        environment = Environment(loader=loader, trim_blocks=True)
        self.template = environment.get_template(template_name)

    def compose_all(self, alarms_json):
        rendered_templates = [self.template.render(status=json_alarm['status'], msg_text=json_alarm)
                              for json_alarm in alarms_json]
        return rendered_templates
