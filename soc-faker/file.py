import random, requests, pendulum, hashlib, string

__EXTENSIONS__ = [
    '.DOC',
    '.DOCX',
    '.LOG',
    '.MSG',
    '.ODT',
    '.PAGES',
    '.RTF',
    '.TEX',
    '.TXT',
    '.WPD',
    '.WPS',
    '.CSV',
    '.DAT',
    '.GED',
    '.KEY',
    '.KEYCHAIN',
    '.PPS',
    '.PPT',
    '.PPTX',
    '.SDF',
    '.TAR',
    '.TAX2016',
    '.TAX2018',
    '.VCF',
    '.XML',
    '.AIF',
    '.IFF',
    '.M3U',
    '.M4A',
    '.MID',
    '.MP3',
    '.MPA',
    '.WAV',
    '.WMA',
    '.3G2',
    '.3GP',
    '.ASF',
    '.AVI',
    '.FLV',
    '.M4V',
    '.MOV',
    '.MP4',
    '.MPG',
    '.RM',
    '.SRT',
    '.SWF',
    '.VOB',
    '.WMV',
    '.3DM',
    '.3DS',
    '.MAX',
    '.OBJ',
    '.BMP',
    '.DDS',
    '.GIF',
    '.HEIC',
    '.JPG',
    '.PNG',
    '.PSD',
    '.PSPIMAGE',
    '.TGA',
    '.THM',
    '.TIF',
    '.TIFF',
    '.YUV',
    '.AI',
    '.EPS',
    '.PS',
    '.SVG',
    '.INDD',
    '.PCT',
    '.PDF',
    '.XLR',
    '.XLS',
    '.XLSX',
    '.ACCDB',
    '.DB',
    '.DBF',
    '.MDB',
    '.PDB',
    '.SQL',
    '.APK',
    '.APP',
    '.BAT',
    '.CGI',
    '.COM',
    '.EXE',
    '.GADGET',
    '.JAR',
    '.WSF',
    '.B',
    '.DEM',
    '.GAM',
    '.NES',
    '.ROM',
    '.SAV',
    '.DWG',
    '.DXF',
    '.GPX',
    '.KML',
    '.KMZ',
    '.ASP',
    '.ASPX',
    '.CER',
    '.CFM',
    '.CSR',
    '.CSS',
    '.DCR',
    '.HTM',
    '.HTML',
    '.JS',
    '.JSP',
    '.PHP',
    '.RSS',
    '.XHTML',
    '.CRX',
    '.PLUGIN',
    '.FNT',
    '.FON',
    '.OTF',
    '.TTF',
    '.CAB',
    '.CPL',
    '.CUR',
    '.DESKTHEMEPACK',
    '.DLL',
    '.DMP',
    '.DRV',
    '.ICNS',
    '.ICO',
    '.LNK',
    '.SYS',
    '.CFG',
    '.INI',
    '.PRF',
    '.HQX',
    '.MIM',
    '.UUE',
    '.7Z',
    '.CBR',
    '.DEB',
    '.GZ',
    '.PKG',
    '.RAR',
    '.RPM',
    '.SITX',
    '.TAR.GZ',
    '.ZIP',
    '.ZIPX',
    '.BIN',
    '.CUE',
    '.DMG',
    '.ISO',
    '.MDF',
    '.TOAST',
    '.VCD',
    '.C',
    '.CLASS',
    '.CPP',
    '.CS',
    '.DTD',
    '.FLA',
    '.H',
    '.JAVA',
    '.LUA',
    '.M',
    '.PL',
    '.PY',
    '.SH',
    '.ps1',
    '.SLN',
    '.SWIFT',
    '.VB',
    '.VCXPROJ',
    '.XCODEPROJ',
    '.BAK',
    '.TMP',
    '.CRDOWNLOAD',
    '.ICS',
    '.MSI',
    '.PART',
    '.TORRENT'
]

class File(object):

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        return "%s-%s-%s%s" % (random.choice(WORDS), random.choice(WORDS), random.choice(WORDS), random.choice(__EXTENSIONS__))

    @property
    def size(self):
        file_size_list = []
        precision = 2
        size = random.randint(1, 3221225472)
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
            file_size_list.append("%.*f%s"%(precision,size,suffixes[suffixIndex]))
        
        return file_size_list

    @property
    def timestamp(self):
        return pendulum.now().subtract(
            years=random.randint(0, 8),
            days=random.randint(1,365),
            hours=random.randint(1,24),
            minutes=random.randint(1, 60), 
            seconds=random.randint(1, 60)
        ).to_datetime_string()

    @property
    def hashes(self):
        random_val = ''.join(random.choice(string.ascii_uppercase) for i in range(256))
        return {
            'md5': hashlib.md5(str(random_val)).hexdigest(),
            'sha1': hashlib.sha1(str(random_val)).hexdigest(),
            'sha256': hashlib.sha256(str(random_val)).hexdigest()
        }