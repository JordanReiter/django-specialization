import sys

from django.template.loader import BaseLoader
from django.template import TemplateDoesNotExist
from specialization.middleware import get_current_host

#from django.template.loaders import 

from django.conf import settings
import os

class Loader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        spec_temp_root = getattr(settings, 'SPECIALIZATION_DIR','')
        hostname = get_current_host()
        if hostname:
            templ_path = os.path.join(spec_temp_root,hostname, template_name)

            if os.path.exists(templ_path):
                try:
                    template_file = open(templ_path)
                    return template_file.read().decode(settings.FILE_CHARSET), os.path.join(hostname,template_name)
                finally:
                    template_file.close()

        raise TemplateDoesNotExist(template_name)
