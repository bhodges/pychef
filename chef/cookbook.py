from chef.base import ChefObject, ChefAPI
from chef.exceptions import ChefServerNotFoundError

class Cookbook(ChefObject):
    """
    A Chef Cookbook object.
    """

    url = '/cookbooks'

    attributes = {
        'definitions': list,
        'name': str,
        'attributetes': list,
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
        'chef_type': str
    }


    @staticmethod
    def versions(name, api=None):
        """
        Get a list of versions for the named cookbook
        """
        api = api or ChefAPI.get_global()
        url = "{0}/{1}".format(Cookbook.url, name)
        try:
            data = api[url]
        except ChefServerNotFoundError:
            return list()
        return list([ rev['version'] for rev in data[name]['versions'] ])


    def __getitem__(self, attr):
         return self.__dict__[attr]

