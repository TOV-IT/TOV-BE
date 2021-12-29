from pages.models import Gallery, Banner, CompanyRecord



COMPONENT_TYPE = {
    'gallery': 'Gallery()',
    'banner': 'Banner()',
    'companyrecord': 'CompanyRecord()'
}


def construct_component(type):
    component = eval(COMPONENT_TYPE[type])
    return component
    
    