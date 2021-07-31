# APT iOS Repository

Python library for retrieve APT Repositories from iOS Jailbreak community

## Example

```python
from apt_ios_repo import APTiOSSources, APTiOSRepository

sources =  APTiOSSources([APTiOSRepository('https://evynw.github.io/'),APTiOSRepository('https://repo.twickd.com/'),APTiOSRepository('https://repo.packix.com/'),APTiOSRepository('http://apt.thebigboss.org/repofiles/cydia/'),APTiOSRepository('http://junesiphone.com/supersecret/'),APTiOSRepository('https://www.yourepo.com/'),APTiOSRepository('https://ryleyangus.com/repo/'),APTiOSRepository('https://sparkdev.me'),APTiOSRepository('https://repo.cpdigitaldarkroom.com/'),APTiOSRepository('https://cokepokes.github.io/'),APTiOSRepository('http://rpetri.ch/repo/'),APTiOSRepository('http://beta.unlimapps.com/'),APTiOSRepository('https://creaturecoding.com/repo/'),APTiOSRepository('http://xnu.science/repo/'),APTiOSRepository('https://cydia.angelxwind.net/'),APTiOSRepository('https://julioverne.github.io/'),APTiOSRepository('https://repo.dynastic.co/')])

print([(package.package, package.version) for package in sources.get_packages_by_author('Ivano Bilenchi')])

[('org.altervista.exilecom.icleaner', '7.9.1'), 
 ('com.exile90.icleanerpro', '7.5.6'), 
 ('com.exile90.icleanerpro', '7.6.0'), 
 ('com.exile90.icleanerpro', '7.6.1'), 
 ('com.exile90.icleanerpro', '7.6.2'), 
 ('com.exile90.icleanerpro', '7.6.4'), 
 ('com.exile90.icleanerpro', '7.7.0'), 
 ('com.exile90.icleanerpro', '7.7.1'), 
 ('com.exile90.icleanerpro', '7.7.5'), 
 ('com.exile90.icleanerpro', '7.8.3'), 
 ('com.exile90.icleanerpro', '7.9.0'),
 ('com.exile90.icleanerpro', '7.9.1'), 
 ('com.ivanobilenchi.icleanerdarktheme', '1.0.2'), 
 ('com.ivanobilenchi.icleanerdarktheme', '1.0.2')]

```