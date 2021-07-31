import posixpath
import re
import bz2
import gzip
import requests
import lzma

__headers = {
    'User-Agent': 'Sileo/1 CFNetwork/976 Darwin/18.2.0',
    'X-Firmware': '12.1.2',
    'X-Machine': 'iPhone10,3',
    'X-Unique-ID': 'df2b5bc80c02907c03dc65e9f38eedfa350711bb',
    'Accept': '*/*',
    'Keep-Alive': 'True'
}

def _get_value_from_content(content: str, key: tuple):
    """
    Get value from content of file, can be release of package
    # Arguments
    content (str): the content of the Packages/Release file
    key (tuple): the key to return the value for
    """
    for key_value in key:
        content = content + '\n'
        pattern = key_value + ': (.*)\n'
        match = re.search(pattern, content)
        try:
            return match.group(1)
        except AttributeError:
            continue

    raise KeyError(content, key)


def __download_binary(url: str):
    """
    Downloads a binary file
    """
    response = requests.get(url, headers=__headers)
    return response.content


def _download(url: str):
    """
    Downloads a UTF-8 encoded file
    """
    return __download_binary(url).decode('utf-8')


def _download_compressed(base_url: str, target: str, dist: str = 'main', arch: str = "iphoneos-arm"):
    """
    Downloads a compressed file
    """
    decompress = {
        f'{target}.bz2': lambda c: bz2.decompress(c),
        f'{target}.gz': lambda c: gzip.decompress(c),
        f'{target}.xz': lambda c: lzma.decompress(c),
        f'{target}.bzip2': lambda c: bz2.decompress(c),
        f'{target}': lambda c: c,
    }

    for suffix, method in decompress.items():
        url = posixpath.join(base_url, suffix)
        print(url)
        try:
            req = requests.get(url, headers=__headers)

            if req.status_code != 200:
                raise Exception('Wrong URL')

        except Exception as err:
            print(err)
            try:
                url = posixpath.join(
                    base_url,
                    'dists',
                    'stable',
                    dist,
                    'binary-' + arch,
                    suffix
                )
                print(url)
                req = requests.get(url, headers=__headers)
                if req.status_code != 200:
                    raise Exception('Wrong URL')
            except Exception as err:
                print(err)
                continue
        try:
            return method(req.content).decode('utf-8')
        except Exception as err:
            print('Could not decode, trying latin-1', err)
            try:
                return method(req.content).decode('latin-1')
            except Exception as error:
                print('Nope, going back', error)
                continue
