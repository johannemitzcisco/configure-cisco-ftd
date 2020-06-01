# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service


# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------
class ServiceCallbacks(Service):

    # The create() callback is invoked inside NCS FASTMAP and
    # must always exist.
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info('Service create(service=', service._path, ')')

        vars = ncs.template.Variables()
        template = ncs.template.Template(service)
        template.apply('policy', vars)
   
#        for template in service.template:
#            input = root.devices.device[service.device].apply_template.get_input()
#            input.template_name = template.name
#            for variable in template.variable:
#              var = input.variable.create(variable.name)
#              var.value = variable.value
#            root.devices.device[service.device].apply_template(input)

            # Save template and it's variable names for later use
 #           if template.name in root.service_templates.ftd:
#               saved_template = root.service_templates.ftd[template.name]
#            else:
#               saved_template = root.service_templates.ftd.create(template.name)
#               del saved_template.variable
#            for variable in template.variable:
#              var = save_template.variable.create(variable.name)
#              var.value = variable.value
         


# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        self.log.info('Main RUNNING')
        self.register_service('configure-cisco-fmc-servicepoint', ServiceCallbacks)

    def teardown(self):
        self.log.info('Main FINISHED')
