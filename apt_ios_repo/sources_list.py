import posixpath

from apt_ios_repo.packages import PackagesFile
from apt_ios_repo.utils import _get_value_from_content, _download, _download_compressed
import urllib.parse as urlparse


class ReleaseFile:
    def __init__(self, content):
        self.__content = content.strip()

    @property
    def origin(self):
        return _get_value_from_content(self.__content, ('Origin',))

    @property
    def label(self):
        return _get_value_from_content(self.__content, ('Label',))

    @property
    def suite(self):
        return _get_value_from_content(self.__content, ('Suite',))

    @property
    def version(self):
        return _get_value_from_content(self.__content, ('Version',))

    @property
    def codename(self):
        return _get_value_from_content(self.__content, ('Codename',))

    @property
    def date(self):
        return _get_value_from_content(self.__content, ('Date',))

    @property
    def architectures(self):
        return _get_value_from_content(self.__content, ('Architectures',)).split()

    @property
    def components(self):
        return _get_value_from_content(self.__content, ('Components',)).split()

    @property
    def description(self):
        return _get_value_from_content(self.__content, ('Description',))


class APTiOSRepository:
    """
    This class represents a ios repository of tweaks

    example:
    '''python
        APTiOSRepository('https://repo.packix.com/')
    '''
    """

    def __init__(self, url: str, dist: str = 'stable'):
        self.url = url
        self.dist = dist
        self.packages_list = None
        self.release = None

    def __repr__(self):
        return self.url

    def get_binary_packages_by_component(self, arch='iphoneos-arm'):
        """
        Returns all binary packages of this repository for a given component
        # Arguments
        component (str): the component to return packages for
        arch (str): the architecture to return packages for, default: 'amd64'
        """
        packages_file = _download_compressed(base_url=self.url, target='Packages', arch=arch)

        return PackagesFile(packages_file).packages

    @property
    def release_file(self):
        """
        Retrieve the release file for that repository
        Returns:
            ReleaseFile()
        """
        if self.release:
            return self.release

        url = urlparse.urljoin(self.url, 'Release')
        release_content = _download(url)
        self.release = ReleaseFile(release_content)
        return self.release

    @property
    def packages(self, arch: str = 'iphoneos-arm'):
        """
        Returns all binary packages of this repository
        # Arguments
        arch (str): the architecture to return packages for, default: 'iphoneos-arm'
        """

        if self.packages_list:
            return self.packages_list
        packages = []
        packages.extend(self.get_binary_packages_by_component(arch))
        self.packages_list = packages
        return self.packages_list

    def get_package(self, name: str, version: str):
        """
        Returns a single binary package
        """
        for package in self.packages:
            if package.package == name and package.version == version:
                return package

        raise KeyError(name, version)

    def get_package_url(self, name: str, version: str):
        """
        Returns the URL for a single binary package
        """
        package = self.get_package(name, version)

        return posixpath.join(self.url, package.filename)

    def get_packages_by_package_name(self, name: str):
        """
        Returns the list of available packages (and it's available versions) for a specific package name
        """

        packages = []

        for package in self.packages:
            if package.package == name:
                packages.append(package)

        return packages

    def get_packages_by_author(self, name: str):
        """
        Returns the list of available packages (and it's available versions) for a specific package name
        """

        packages = []

        for package in self.packages:
            try:
                if name in package.author:
                    packages.append(package)
            except TypeError:
                continue
        return packages

    def search_package(self, keyword: str):
        packages = []

        for package in self.packages:
            if package.name and (keyword.lower() in package.name.lower() or keyword.lower() in package.package):
                packages.append(package)

        return packages


class APTiOSSources:
    """
    Class that represents a collection of APT repositories
    """
    def __init__(self, repositories):
        self.__repositories = repositories
        self.packages_list = None

    def __getitem__(self, item):
        return self.get_packages_by_name(item)

    @property
    def repositories(self):
        return self.__repositories

    @property
    def packages(self):
        """Returns all binary packages of all APT repositories"""

        if self.packages_list:
            return self.packages_list

        packages = []
        for repo in self.__repositories:
            packages.extend(repo.packages)

        self.packages_list = packages
        return packages

    def get_package(self, name, version):
        """
        Returns a single binary package
        """
        for repo in self.__repositories:
            try:
                return repo.get_package(name, version)
            except KeyError:
                pass

        raise KeyError(name, version)

    def get_package_url(self, name, version):
        """
        Returns the URL of a single binary package
        """
        for repo in self.__repositories:
            try:
                return repo.get_package_url(name, version)
            except KeyError:
                pass

        raise KeyError(name, version)

    def get_packages_by_name(self, name):
        """
        Returns the list of available packages (and it's available versions) for a specific package name
        """

        packages = []

        for repo in self.__repositories:
            packages.extend(repo.get_packages_by_package_name(name))

        return packages

    def get_packages_by_author(self, name):
        """
        Returns the list of available packages (and it's available versions) for a specific package name
        """

        packages = []

        for repo in self.__repositories:
            packages.extend(repo.get_packages_by_author(name))

        return packages

    def search_package(self, name):
        """
        Returns the list of available packages (and it's available versions) that match the keyword
        """

        packages = []

        for repo in self.__repositories:
            packages.extend(repo.search_package(name))

        return packages
