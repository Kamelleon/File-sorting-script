import glob
import os
import shutil

# Get current location
current_location=os.getcwd()

def sortfiles(file_extension):
    try:
        if glob.glob("*."+file_extension):
            try:
                # Make empty directory with the name of extension
                os.mkdir(file_extension)
            except Exception:
                pass
            # Move every file with extension to the specified folder
            for file in glob.glob("*."+file_extension):
                 if os.path.isfile(file):
                     # Copy files to dirs
                     shutil.copy2(file, current_location+'\\'+file_extension)
                     # Remove copied files from original source
                     os.remove(file)
    except Exception:
        pass


def sortpythonfiles(file_extension):
        if glob.glob("*."+file_extension):
            try:
                # Make empty directory with the name of extension
                os.mkdir(file_extension)
            except Exception:
                pass
            for file in glob.glob("*."+file_extension):
                # Don't move this script to specified folder
                if file==os.path.basename(__file__):
                    continue
                else:
                    os.path.isfile(file)
                    shutil.copy2(file, current_location+'\\'+file_extension)
                    os.remove(file)


if __name__ == "__main__":
    print("[~] Sorting...")
    sortpythonfiles("py")
    sortfiles('3dm')
    sortfiles('3ds')
    sortfiles('7z')
    sortfiles('aif')
    sortfiles('au')
    sortfiles('asp')
    sortfiles('apk')
    sortfiles('aspx')
    sortfiles('accde')
    sortfiles('accdb')
    sortfiles('aac')
    sortfiles('avi')
    sortfiles('bat')
    sortfiles('bz2')
    sortfiles('bookmarks')
    sortfiles('bmp')
    sortfiles('class')
    sortfiles('java')
    sortfiles('csv')
    sortfiles('cpp')
    sortfiles('css')
    sortfiles('crx')
    sortfiles('cer')
    sortfiles('cmd')
    sortfiles('cc')
    sortfiles('ccit')
    sortfiles('dbf')
    sortfiles('docx')
    sortfiles('docm')
    sortfiles('dotm')
    sortfiles('dot')
    sortfiles('dif')
    sortfiles('dll')
    sortfiles('dotx')
    sortfiles('doc')
    sortfiles('eps')
    sortfiles('exe')
    sortfiles('fm3')
    sortfiles('flv')
    sortfiles('gif')
    sortfiles('hqx')
    sortfiles('htm')
    sortfiles('html')
    sortfiles('iso')
    sortfiles('ini')
    sortfiles('index')
    sortfiles('jpg')
    sortfiles('jpeg')
    sortfiles('jar')
    sortfiles('js')
    sortfiles('jsp')
    sortfiles('lnk')
    sortfiles('log')
    sortfiles('m4a')
    sortfiles('mac')
    sortfiles('map')
    sortfiles('mdb')
    sortfiles('midi')
    sortfiles('mov')
    sortfiles('mp3')
    sortfiles('msi')
    sortfiles('mp4')
    sortfiles('mpeg')
    sortfiles('max')
    sortfiles('mpg')
    sortfiles('mtb')
    sortfiles('odp')
    sortfiles('ods')
    sortfiles('odt')
    sortfiles('url')
    sortfiles('pdf')
    sortfiles('p65')
    sortfiles('png')
    sortfiles('ppt')
    sortfiles('pdb')
    sortfiles('pptx')
    sortfiles('potx')
    sortfiles('potm')
    sortfiles('ppsx')
    sortfiles('pot')
    sortfiles('pptm')
    sortfiles('pps')
    sortfiles('psd')
    sortfiles('php')
    sortfiles('psp')
    sortfiles('sql')
    sortfiles('svg')
    sortfiles('qxd')
    sortfiles('ra')
    sortfiles('rle')
    sortfiles('rtf')
    sortfiles('rb')
    sortfiles('sit')
    sortfiles('sqlite3')
    sortfiles('sh')
    sortfiles('sav')
    sortfiles('sql')
    sortfiles('tar')
    sortfiles('tif')
    sortfiles('tiff')
    sortfiles('torrent')
    sortfiles('txt')
    sortfiles('ttf')
    sortfiles('tga')
    sortfiles('vsd')
    sortfiles('vss')
    sortfiles('vssm')
    sortfiles('vst')
    sortfiles('vcd')
    sortfiles('vstx')
    sortfiles('wav')
    sortfiles('wma')
    sortfiles('wk3')
    sortfiles('wks')
    sortfiles('wpd')
    sortfiles('wmv')
    sortfiles('xls')
    sortfiles('xlsx')
    sortfiles('xlsm')
    sortfiles('xltm')
    sortfiles('xlt')
    sortfiles('xlam')
    sortfiles('xla')
    sortfiles('xll')
    sortfiles('xml')
    sortfiles('xlr')
    sortfiles('xltx')
    sortfiles('xps')
    sortfiles('zip')
    sortfiles('zipx')
    sortfiles('rar')
    print("[+] Finished")
