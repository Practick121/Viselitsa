# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['maincode.py'],
    pathex=[r'C:\Users\Dany\python_c++\виселица'],
    binaries=[],
    datas=[(r'images/виселица2.png', 'images'),
    (r'images/виселица3.png', 'images'),
    (r'images/виселица4.png', 'images'),
    (r'images/виселица5.png', 'images'),
    (r'images/виселица6.png', 'images'),
    (r'images/виселица7.png', 'images'),
    (r'images/виселица8.png', 'images'),
    (r'images/виселица9.png', 'images'),
    (r'images/виселица10.png', 'images'),
    (r'images/виселица11.png', 'images'),
    (r'images/заднийфон.jpg', 'images'),
    (r'images/победа.jpg', 'images'),
    (r'images/поражение.jpg', 'images'),
    (r'fonts/arial.ttf', 'fonts'),
    (r"texts/russian_nouns.txt", "texts")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ВИСЕЛИЦА',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
