from apt_ios_repo.utils import _get_value_from_content


class PackagesFile:
    """
    Class that represents a Packages file
    # Arguments
    content (str): the content of the Packages file
    """

    def __init__(self, content):
        self.__content = content.strip()

    @property
    def packages(self):
        """Returns all binary packages in this Packages files"""
        packages = []
        for package_content in self.__content.split('\n\n'):
            if not package_content:
                continue
            packages.append(BinaryPackageFile(package_content))

        return packages


class BinaryPackageFile:
    def __init__(self, content):
        self.__content = content

    def __repr__(self):
        return self.package + " - " + self.version

    @property
    def package(self):
        return _get_value_from_content(self.__content, ('Package',))

    @property
    def version(self):
        return _get_value_from_content(self.__content, ('Version',))

    @property
    def filename(self):
        return _get_value_from_content(self.__content, ('Filename',))

    @property
    def name(self):
        try:
            return _get_value_from_content(self.__content, ('Name',))
        except KeyError:
            return None

    @property
    def maintainer(self):
        try:
            return _get_value_from_content(self.__content, ('Maintainer',))
        except KeyError:
            return None

    @property
    def author(self):
        try:
            return _get_value_from_content(self.__content, ('Author',))
        except KeyError:
            return None

    @property
    def original_maintainer(self):
        try:
            return _get_value_from_content(self.__content, ('Original-Maintainer',))
        except KeyError:
            return None

    @property
    def architecture(self):
        try:
            return _get_value_from_content(self.__content, ('Architecture',))
        except KeyError:
            return None

    @property
    def icon(self):
        try:
            return _get_value_from_content(self.__content, ('Icon',))
        except KeyError:
            return None

    @property
    def multi_arch(self):
        try:
            return _get_value_from_content(self.__content, ('Multi-Arch',))
        except KeyError:
            return None

    @property
    def homepage(self):
        try:
            return _get_value_from_content(self.__content, ('Homepage',))
        except KeyError:
            return None

    @property
    def depiction(self):
        try:
            return _get_value_from_content(self.__content, ('Depiction',))
        except KeyError:
            return None

    @property
    def origin(self):
        try:
            return _get_value_from_content(self.__content, ('Origin',))
        except KeyError:
            return None

    @property
    def priority(self):
        try:
            return _get_value_from_content(self.__content, ('Priority',))
        except KeyError:
            return None

    @property
    def section(self):
        try:
            return _get_value_from_content(self.__content, ('Section',))
        except KeyError:
            return None

    @property
    def depends(self):
        try:
            field = _get_value_from_content(self.__content, ('Depends',))
        except KeyError:
            return None

        if field:
            depends = [d.strip() for d in field.split(',')]
        else:
            depends = []
        return depends

    @property
    def replaces(self):
        try:
            field = _get_value_from_content(self.__content, ('Replaces',))
        except KeyError:
            return None

        if field:
            replaces = [d.strip() for d in field.split(',')]
        else:
            replaces = []
        return replaces

    @property
    def breaks(self):
        try:
            field = _get_value_from_content(self.__content, ('Breaks',))
        except KeyError:
            return None

        if field:
            breaks = [d.strip() for d in field.split(',')]
        else:
            breaks = []
        return breaks

    @property
    def recommends(self):
        try:
            field = _get_value_from_content(self.__content, ('Recommends',))
        except KeyError:
            return None

        if field:
            recommends = [d.strip() for d in field.split(',')]
        else:
            recommends = []
        return recommends

    @property
    def suggests(self):
        try:
            field = _get_value_from_content(self.__content, ('Suggests',))
        except KeyError:
            return None

        if field:
            suggests = [d.strip() for d in field.split(',')]
        else:
            suggests = []
        return suggests

    @property
    def conflicts(self):
        try:
            field = _get_value_from_content(self.__content, ('Conflicts',))
        except KeyError:
            return None

        if field:
            conflicts = [d.strip() for d in field.split(',')]
        else:
            conflicts = []
        return conflicts

    @property
    def installed_size(self):
        try:
            return _get_value_from_content(self.__content, ('Installed-Size',))
        except KeyError:
            return None

    @property
    def size(self):
        try:
            return _get_value_from_content(self.__content, ('Size',))
        except KeyError:
            return None

    @property
    def md5(self):
        try:
            return _get_value_from_content(self.__content, ('MD5Sum', ('MD5sum',)))
        except KeyError:
            return None

    @property
    def sha1(self):
        try:
            return _get_value_from_content(self.__content, ('SHA1',))
        except KeyError:
            return None

    @property
    def sha256(self):
        try:
            return _get_value_from_content(self.__content, ('SHA256',))
        except KeyError:
            return None

    @property
    def description(self):
        try:
            return _get_value_from_content(self.__content, ('Description',))
        except KeyError:
            return None

    @property
    def description_md5(self):
        try:
            return _get_value_from_content(self.__content, ('Description-md5',))
        except KeyError:
            return None

    @property
    def built_using(self):
        try:
            return _get_value_from_content(self.__content, ('Built-Using',))
        except KeyError:
            return None

    @property
    def source(self):
        try:
            return _get_value_from_content(self.__content, ('Source',))
        except KeyError:
            return None

    @property
    def task(self):
        try:
            return _get_value_from_content(self.__content, ('Task',))
        except KeyError:
            return None

    @property
    def supported(self):
        try:
            return _get_value_from_content(self.__content, ('Supported',))
        except KeyError:
            return None

    def content(self):
        print(self.__content)
