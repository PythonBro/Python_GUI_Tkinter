# -*- mode: python -*-

block_cipher = None


a = Analysis(['20171102_prototype/GraphViewer_Ver.1.0.1.py'],
             pathex=['/Users/masazumi/Dropbox/GitHub/Python_GUI_Tkinter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='GraphViewer_Ver.1.0.1',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='GraphViewer_Ver.1.0.1.app',
             icon=None,
             bundle_identifier=None)
