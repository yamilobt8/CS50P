def get_media_type(filename):
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    for ext, type in media_types.items():
        if filename.lower().endswith(ext):
            return type
    return 'application/octet-stream'

if __name__ == '__main__':
    file = input('File name: ').replace(' ', '')
    media_type = get_media_type(file)
    print(media_type)
