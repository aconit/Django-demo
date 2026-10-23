from django.db import models
from django.contrib.auth.models import User

def is_employee_group(self):
    # Safe check: looks at the first group name, defaults to False if no groups exist
    first_group = self.groups.first()
    is_in_group = first_group.name == "Medewerker" if first_group else False
          
    return is_in_group or self.is_superuser or self.is_staff

User.isEmployee = property(is_employee_group)