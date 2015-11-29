from chef.base import ChefObject, ChefAPI
from chef.exceptions import ChefServerNotFoundError

class Cookbook(ChefObject):
    """A Chef Cookbook object."""

    url = '/cookbooks'

    attributes = {
        'definitions': list,
        'name': str,
        'attributes': list,
        'files': list,
        'json_class': str,
        'providers': list,
        'metadata': dict,
        'libraries': list,
        'templates': list,
        'resources': list,
        'cookbook_name': str,
        'version': str,
        'recipes': list,
        'root_files': list,
        'chef_type': str,
    }


    def __getitem__(self, attr):
         return self.__dict__[attr]

