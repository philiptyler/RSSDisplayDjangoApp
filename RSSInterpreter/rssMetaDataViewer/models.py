# Model for storing video meta data from an RSS feed
class RssVideo():

    def __init__(self, codec="", duration=0, bitrate=0):

        # REQUIRED: codec
        # Codec of video (MIME type) contained in RSS feed (Ex: "video/mp4")
        # If the codec is not in media:content, media:player must be defined
        if (codec == ""):
            raise Exception("Codec is a required RssVideo property")
        self.codec = codec
        
        # Length of movie clip in seconds (Ex: "225")
        self.duration = duration
        
        # Data rate of movie clip in kb/s (Ex: "128")
        self.bitrate = bitrate
