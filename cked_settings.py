import os

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ELFINDER_OPTIONS = {
    ## required options
    'root': os.path.join(PROJECT_ROOT, 'media', 'uploads'),
    'URL': '/media/uploads/',
}
print ELFINDER_OPTIONS

CKEDITOR_OPTIONS = {
    'skin': 'bootstrapck',
    'toolbar': [
        { 'name': 'document', 'items': [ 'Source', '-', 'Preview', '-', 'Templates' ] },
        { 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ], 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ] },
         #// Defines toolbar group with name (used to create voice label) and items in 3 subgroups.
        
        { 'name': 'insert', 'items': [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'PageBreak', 'Iframe' ] },
        { 'name': 'links', 'items': [ 'Link', 'Unlink', 'Anchor' ] },
        '/',                                                                                    #// Line break - next group will be placed in new line.
        { 'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ], 'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
        { 'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ], 'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl' ] },
        # { 'name': 'styles', 'items': [ 'Styles', 'Format', 'Font', 'FontSize' ] },
        { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
        { 'name': 'tools', 'items': [ 'Maximize', 'ShowBlocks' ] },
        { 'name': 'others', 'items': [ '-' ] },
        ],
    # 'filebrowserWindowWidth': 940,
    # 'filebrowserWindowHeight': 750,
    'height': 600,
    'language': 'ru',
}
