from moviepy.editor import VideoFileClip

# Input video file
input_file = "roidcat.mp4"

# Load the video clip
clip = VideoFileClip(input_file)

# Extract audio and save as MP3
audio = clip.audio
audio.write_audiofile(input_file+"_audio.mp3")

# Remove audio from video and save as video-only MP4
video_no_audio = clip.without_audio()
video_no_audio.write_videofile(input_file+"_video.mp4")

print("video and audio separated")