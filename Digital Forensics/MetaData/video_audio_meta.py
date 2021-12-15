import argparse
import json
import mutagen

'''
id3 Definitions https://id3.org/id3v2.4.0-frames
mp4 Definitions http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/QuickTime.html
                http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/QuickTime.html#GenreID
'''

'''
Description:  
        --> This script will analyze mp4 mp3. 
To run this script--> python video_audio.meta.py
example --> python video_audio.meta.py  <video-audio.json>
'''
__authors__ = ["Gokan Bektas"]
__date__ = 20211214
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = ' '

def handle_id3(id3_file):
    
    id3_frames = {
        'TIT2': 'Title', 'TPE1': 'Artist', 'TALB': 'Album',
        'TXXX': 'Custom', 'TCON': 'Content Type', 'TDRL': 'Date Released',
        'COMM': 'Comments', 'TDRC': 'Recording Date'}
    print("{:15} | {:15} | {:38} | {}".format("Frame", "Description", "Text", "Value"))
    print("-" * 85)
    
    for frames in id3_file.tags.values():
        frame_name = id3_frames.get(frames.FrameID, frames.FrameID)
        desc = getattr(frames, 'desc', "N/A")
        text = getattr(frames, 'text', ["N/A"])[0]
        value = getattr(frames, 'value', "N/A")
        if "date" in frame_name.lover():
            text = str(text)
            
        print("{:15} | {:15} | {:38} | {}".format(frame_name, desc, text, value))
        
def handle_mp4(mp4_file):
    
    cp_sym = u"\u00A9"
    qt_tag = {
        cp_sym + 'nam': 'Title', cp_sym + 'art': 'Artist',
        cp_sym + 'alb': 'Album', cp_sym + 'gen': 'Genre',
        'cpil': 'Compilation', cp_sym + 'day': 'Creation Date',
        'cnID': 'Apple Store Content ID', 'atID': 'Album Title ID',
        'plIB': 'Playlist ID', 'geID': 'Genre ID', 'pcst': 'Podcast',
        'purl': 'Podcast URL', 'egid': 'Episode Global ID',
        'cmID': 'Camera ID', 'sfID': 'Aplle Store Country',
        'desc': 'Description', 'ldes': 'Long Description'}
    
    genre_ids = json.load(open('genres.json'))
    
    print("{:22} | {}".format('Name', 'Value'))
    print("-" * 40)
    for name, value in mp4_file.tags.items():
        tag_name = qt_tag.get(name, name)
        if isinstance(value, list):
            value = "; ".join([str(x) for x in value])
        if name == 'geID':
            value ="{}: {}".format(
                value, genre_ids[str(value)].replace("|", " - "))
        print("{:22} | {}".format(tag_name, value))
            
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__description__, epilog="Develop by {} on {}".format(", ".join(__authors__),__date__))
    parser.add_argument("AV_FILE", help="File to extract metadata from")
    args = parser.parse_args()
    av_file = mutagen.File(args.AV_FILE)
    
    file_ext = args.AV_FILE.rsplit('.', 1)[-1]
    if file_ext.lower() == 'mp3':
        handle_id3(av_file)
        
    elif file_ext.lower() == 'md4':
        handle_mp4(av_file)