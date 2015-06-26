import os

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ELFINDER_OPTIONS = {
    ## required options
    'root': '/home/ukrainem/domains/tkr.od.ua/public_html/media/uploads',
    'URL': '/media/uploads/',
}

CKEDITOR_OPTIONS = {
    'skin': 'moono',
    'toolbar': [
        { 'name': 'document', 'items': [ 'Source', '-', 'Preview', '-', 'Templates' ] }, #// Defines toolbar group with name (used to create voice label) and items in 3 subgroups.
        { 'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ], 'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
        { 'name': 'editing', 'groups': [ 'find', 'selection', 'spellchecker' ], 'items': [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
        { 'name': 'insert', 'items': [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ] },
        '/',                                                                                    #// Line break - next group will be placed in new line.
        { 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ], 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ] },
        { 'name': 'links', 'items': [ 'Link', 'Unlink', 'Anchor' ] },
        { 'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ], 'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl' ] },
        '/',
        { 'name': 'styles', 'items': [ 'Styles', 'Format', 'Font', 'FontSize' ] },
        { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
        { 'name': 'tools', 'items': [ 'Maximize', 'ShowBlocks' ] },
        { 'name': 'others', 'items': [ '-' ] },
        { 'name': 'about', 'items': [ 'About' ] }
        ],
    # 'filebrowserWindowWidth': 940,
    # 'filebrowserWindowHeight': 750,
    'height': 600,
    'language': 'ru',
}
