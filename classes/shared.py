class Any(str):
    def __eq__(self, __value: object) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return False

class AllTrue(str):
    def __init__(self, representation=None) -> None:
        self.repr = representation
        pass
    def __ne__(self, __value: object) -> bool:
        return False
    # isinstance, jsonserializable hijack
    def __instancecheck__(self, instance):
        return True
    def __subclasscheck__(self, subclass):
        return True
    def __bool__(self):
        return True
    def __str__(self):
        return self.repr
    # jsonserializable hijack
    def __jsonencode__(self):
        return self.repr
    def __repr__(self) -> str:
        return self.repr
    def __eq__(self, __value: object) -> bool:
        return True

FILE_EXTENSIONS = {
    "images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".ico",
        ".svg",
        ".webp",
        ".psd",
        ".ai",
        ".eps",
        ".indd",
        ".cdr",
        ".raw",
        ".cr2",
        ".nef",
        ".orf",
        ".sr2",
        ".pef",
        ".x3f",
        ".dng",
        ".raf",
        ".rw2",
        ".arw",
        ".mef",
        ".mrw",
        ".fff",
        ".srf",
        ".kdc",
        ".mos",
        ".rwl",
        ".dcr",
        ".erf",
        ".3fr",
        ".srw",
        ".bay",
        ".nrw",
        ".ptx",
        ".cap",
        ".iiq",
        ".eip",
        ".rwz",
        ".r3d",
        ".qtk",
        ".dcs",
        ".rw1",
        ".rpp",
        ".fff",
        ".rwl",
        ".pef",
        ".xmp"
    ],
    "audio": [
        ".mp3",
        ".wav",
        ".flac",
        ".aac",
        ".ogg",
        ".wma",
        ".m4a",
        ".ape",
        ".alac",
        ".aiff",
        ".mid",
        ".opus",
        ".amr",
        ".pcm",
        ".mp2",
        ".ac3",
        ".ra",
        ".au",
        ".mka",
        ".snd"
    ],
    "video": [
        ".mp4",
        ".avi",
        ".mkv",
        ".mov",
        ".wmv",
        ".flv",
        ".webm",
        ".mpg",
        ".mpeg",
        ".m4v",
        ".3gp",
        ".rmvb",
        ".divx",
        ".vob",
        ".ts",
        ".ogv",
        ".m2ts",
        ".mts",
        ".f4v",
        ".asf"
    ],
    "text": [
        ".txt",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".pdf",
        ".rtf",
        ".html",
        ".htm",
        ".xml",
        ".json",
        ".csv",
        ".dat",
        ".ini",
        ".cfg",
        ".inf",
        ".log",
        ".md",
        ".sql",
        ".php",
        ".cpp",
        ".java",
        ".py",
        ".c",
        ".h",
        ".hpp",
        ".js",
        ".css",
        ".asp",
        ".aspx",
        ".jsp",
        ".jspx",
        ".xhtml",
        ".rss",
        ".atom",
        ".pl",
        ".cgi",
        ".nfo",
        ".diz",
        ".reg",
        ".key",
        ".sfv",
        ".cue",
        ".url",
        ".bat",
        ".sh",
        ".ps1",
        ".vbs",
        ".asm",
        ".bak",
        ".tmp",
        ".temp"
    ],
    "tensors" : [".latent",".ckpt", ".pt", ".bin", ".pth", ".safetensors"],
}
