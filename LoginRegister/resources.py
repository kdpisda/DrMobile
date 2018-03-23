from import_export import resources
from .models import CompanyDetails

class CompanyDetailsResource(resources.ModelResource):
    class Meta:
        model = CompanyDetails